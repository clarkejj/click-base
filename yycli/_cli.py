from __future__ import print_function
import click
import json


def _load_data(f):
    data = []
    for line in f.readlines():
        data.append(json.loads(line))
    

@click.group()
def cli():
    pass


@cli.command()
@click.argument("f", type=click.File('r'))
def find_towns(f):
    """
    Find all towns in the given file
    """
    data = _load_data(f)
