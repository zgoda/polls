import os

import click
from dotenv import load_dotenv, find_dotenv
from simple_settings import settings


cli = click.Group()
cli.ignore_unknown_options = True


@cli.command()
@click.option(
    '--settings', '-s', 'settings_path', required=True,
    help='path to settings file',
)
def run(settings_path):
    os.environ.setdefault('SIMPLE_SETTINGS', settings_path)
    print(settings.as_dict())


def main():
    load_dotenv(find_dotenv())
    cli()
