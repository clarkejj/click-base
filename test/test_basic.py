
import pytest
from StringIO import StringIO

from yycli._cli import _load_data


def test_basic():
    assert bool(1) is True


def test_load_file():
    data = StringIO("{}\n")
    d = _load_data(data)
    assert len(d) == 1
    assert d[0] == {}
