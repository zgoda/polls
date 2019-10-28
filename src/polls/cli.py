import click
from dotenv import load_dotenv, find_dotenv


@click.group()
def cli():
    pass


def main():
    load_dotenv(find_dotenv())
    cli()
