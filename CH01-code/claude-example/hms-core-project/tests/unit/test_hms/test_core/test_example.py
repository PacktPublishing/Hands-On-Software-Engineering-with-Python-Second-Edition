"""Example unit test for the HMS Core package."""

import pytest
from hms.core import __version__


def test_version():
    """Test that the version string is valid."""
    assert __version__ == '0.1.0'
