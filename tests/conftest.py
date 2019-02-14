import os
import pytest


@pytest.fixture
def datadir():
    """Path to directory with test data."""
    return os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


@pytest.fixture
def lamost_fits(datadir):
    """LAMOST DR2 FITS file fixture."""
    return os.path.join(datadir, 'spec-55916-B5591606_sp01-001.fits')


@pytest.fixture
def lamost_dr1_fits(datadir):
    """LAMOST DR1 FITS file fixture."""
    return os.path.join(datadir, 'spec-55939-B5593905_sp01-018.fits')
