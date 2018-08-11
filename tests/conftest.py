import os
import pytest


@pytest.fixture
def data_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')
