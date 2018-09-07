import os
import pytest


@pytest.fixture
def data_dir():
    """Path to directory with test data."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
