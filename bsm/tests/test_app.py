from bsm.app import add, sub  # pylint: disable=import-error
import pytest


def test_add():
    """Tests add."""
    assert add(1, 1) == 2


def test_sub():
    """Tests sub."""
    assert sub(1, 1) == 0
