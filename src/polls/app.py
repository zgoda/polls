import os
from logging.config import dictConfig

from flask import render_template
from werkzeug.utils import ImportStringError

from .ext import csrf, msmw, pony
from .main import main_bp
from .models import db
from .utils.app import Application
from .utils.templates import extra_context, extra_filters


def make_app(env=None):
    flask_environment = os.environ.get('FLASK_ENV', '')
    if flask_environment == 'production':
        configure_logging()
    app = Application(__name__.split('.')[0])
    configure_app(app, env)
    configure_extensions(app)
    configure_templating(app)
    with app.app_context():
        configure_hooks(app)
        configure_blueprints(app)
        configure_error_handlers(app)
    return app


def configure_app(app, env):
    app.config.from_object('polls.config')
    if env is not None:
        try:
            app.config.from_object(f'polls.config_{env}')
        except ImportStringError:
            app.logger.info(f'no environment config for {env}')
    config_local = os.environ.get('CONFIG_LOCAL')
    if config_local:
        app.logger.info(f'local configuration loaded from {config_local}')
        app.config.from_envvar('CONFIG_LOCAL')
    config_secrets = os.environ.get('CONFIG_SECRETS')
    if config_secrets:
        app.logger.info(f'secrets loaded from {config_secrets}')
        app.config.from_envvar('CONFIG_SECRETS')


def configure_hooks(app):
    pass


def configure_blueprints(app):
    app.register_blueprint(main_bp)


def configure_extensions(app):
    pony.init_app(app)
    csrf.init_app(app)
    msmw.init_app(app)

    db.bind(**app.config['PONY_CONFIG'])
    db.generate_mapping(create_tables=True)


def configure_templating(app):
    ctx = {
        'debug': app.debug,
    }
    ctx.update(extra_context())
    app.jinja_env.globals.update(ctx)
    app.jinja_env.filters.update(extra_filters())


def configure_logging():
    dictConfig({
        'version': 1,
        'formatters': {
            'default': {
                'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
            }
        },
        'handlers': {
            'wsgi': {
                'class': 'logging.StreamHandler',
                'stream': 'ext://flask.logging.wsgi_errors_stream',
                'formatter': 'default',
            }
        },
        'root': {
            'level': 'INFO',
            'handlers': ['wsgi'],
        },
    })


def configure_error_handlers(app):

    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500
