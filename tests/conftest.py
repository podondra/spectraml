import os
import pytest


@pytest.fixture
def datadir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
