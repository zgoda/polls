import click
from dotenv import load_dotenv, find_dotenv


cli = click.Group()


@cli.command()
def run():
    pass


def main():
    load_dotenv(find_dotenv())
    cli()
