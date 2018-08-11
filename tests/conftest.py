import os
import pytest


@pytest.fixture
def data_dir():
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


@pytest.fixture
def lamost_fits(data_dir):
    return os.path.join(data_dir, 'spec-55916-B5591606_sp01-001.fits')
