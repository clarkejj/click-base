
import pytest
from StringIO import StringIO

from yycli._cli import _load_data, _find_towns


def test_basic():
    assert bool(1) is True


def test_load_file():
    data = StringIO("{}\n")
    d = _load_data(data)
    assert len(d) == 1
    assert d[0] == {}


def test_load_invalid_data():
    data = StringIO("{}\nblammo")
    data.name = 'a fake filename'

    try:
        d = _load_data(data)
        got_error = False
    except Exception as e:
        got_error = True
    assert got_error
    assert 'a fake filename' in str(e)


def test_find_duplicate_towns():
    data = [
        {
            "placeDetails": {
                "place": {
                    "type": "town",
                    "name": "foo",
                }
            }
        },
        {
            "placeDetails": {
                "place": {
                    "type": "Town",
                    "name": "foo",
                }
            }
        },
    ]

    towns = _find_towns(data)
    assert len(towns) == 1
