from dotenv import find_dotenv, load_dotenv
from flask.cli import FlaskGroup

from .app import make_app


def create_app(_unused):  # pragma: no cover
    return make_app('dev')


cli = FlaskGroup(create_app=create_app, help='Polls management')


def main():  # pragma: no cover
    load_dotenv(find_dotenv())
    cli()
