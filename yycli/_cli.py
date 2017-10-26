from __future__ import print_function
import click


@click.group()
def cli():
    pass


@cli.command()
def example():
    """
    An example sub-command
    """
    print("The example command was run")
