from __future__ import print_function
import click
import json


class Error(Exception):
    pass

def _load_data(f, ignore_errors=False):
    data = []
    for n, line in enumerate(f.readlines()):
        try:
            data.append(json.loads(line))
        except ValueError as e:
            if not ignore_errors:
                raise Error(
                    "Error loading '{}' at line {}: {}".format(
                        f.name, n, e,
                    )
                )

    return data


def _find_towns(data):
    towns = set()
    for d in data:
        try:
            if d['placeDetails']['place']['type'].lower().strip() == 'town':
                town_data = d
        except KeyError:
            continue
        towns.add(town_data['placeDetails']['place']['name'])
    return sorted(towns)


@click.group()
def cli():
    pass


@cli.command()
@click.argument("f", type=click.File('r'))
@click.option(
    '-i', '--ignore-errors',
    help='ignore per-line errors in JSON file',
    is_flag=True,
)
def find_towns(f, ignore_errors):
    """
    Find all towns in the given file
    """
    try:
        data = _load_data(f, ignore_errors)
    except Error as e:
        print("Error: {}".format(e))
        return 1

    towns = _find_towns(data)
    print("Found {} towns:".format(len(towns)))
    for t in towns:
        print("  {}".format(t))

