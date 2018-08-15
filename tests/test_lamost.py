import os
import warnings
import pandas
import pytest
from astropy.utils.exceptions import AstropyWarning
from spectraml import lamost


@pytest.fixture
def lamost_fits(data_dir):
    return os.path.join(data_dir, 'spec-55916-B5591606_sp01-001.fits')


@pytest.fixture
def lamost_dr1_fits(data_dir):
    return os.path.join(data_dir, 'spec-55939-B5593905_sp01-018.fits')


def test_read_spectrum(lamost_fits):
    """Test if a LAMOST FITS file can be read."""
    identifier, wave, flux = lamost.read_spectrum(lamost_fits)
    assert identifier == os.path.split(lamost_fits)[1]
    # TODO come up with better test
    assert wave is not None and flux is not None


def test_read_dr1_spectrum(lamost_dr1_fits):
    """Test if a LAMOST DR1 FITS file can be read."""
    # disable astropy warnings
    warnings.simplefilter('ignore', category=AstropyWarning)
    identifier, wave, flux = lamost.read_dr1_spectrum(lamost_dr1_fits)
    assert identifier == os.path.split(lamost_dr1_fits)[1]
    # TODO come up with better test
    assert wave is not None and flux is not None


def test_preprocess_spectra(data_dir):
    path = os.path.join(data_dir, 'LAMOST-DR2')
    spectra = lamost.preprocess_spectra(path)
    assert isinstance(spectra, pandas.DataFrame)
    # there is 140 wavelengths and a column idicating data corruption
    assert spectra.shape == (14, 141)
