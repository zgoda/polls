import os

import click
from dotenv import find_dotenv, load_dotenv
from werkzeug.serving import run_simple
from pony.orm import db_session

from .app import application
from .data import Poll

cli = click.Group()
cli.ignore_unknown_options = True


@cli.command()
@click.option(
    '--settings', '-s', 'settings_path', required=True,
    help='path to settings file',
)
def run(settings_path):
    os.environ.setdefault('SIMPLE_SETTINGS', settings_path)
    run_simple(
        '127.0.0.1', 5000, application, use_reloader=True, use_debugger=True,
        reloader_type='watchdog',
    )


@cli.group(name='poll')
def poll_ops():
    pass


@poll_ops.command(name='create')
@click.option('--title', '-t', required=True, help='poll title')
@click.option('--description', '-d', help='poll description (optional)')
@click.option('--start-date', '-s', help='poll start date (optional)')
@click.option('--duration', '-r', help='poll duration (optional)')
@click.option(
    '--settings', '-s', 'settings_path', required=True,
    help='path to settings file',
)
def poll_create(title, description, start_date, duration, settings_path):
    os.environ.setdefault('SIMPLE_SETTINGS', settings_path)
    kw = {}
    with db_session:
        poll = Poll(title=title, description=description, **kw)
        click.echo(f'poll {poll.title} has been created')


def main():
    load_dotenv(find_dotenv())
    cli()
