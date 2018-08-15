import os
import warnings
import pandas
import pytest
from astropy.io import fits
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
    with fits.open(lamost_fits) as hdulist:
        naxis1 = hdulist[0].header['NAXIS1']
        fits_flux = hdulist[0].data[0]
        fits_wave = hdulist[0].data[2]
    identifier, wave, flux = lamost.read_spectrum(lamost_fits)
    # check identifier
    assert identifier == os.path.split(lamost_fits)[1]
    assert wave.shape[0] == naxis1 and flux.shape[0] == naxis1
    assert flux == pytest.approx(fits_flux)
    assert wave == pytest.approx(fits_wave)


def test_read_dr1_spectrum(lamost_dr1_fits):
    """Test if a LAMOST DR1 FITS file can be read."""
    with fits.open(lamost_dr1_fits) as hdulist:
        header = hdulist[0].header
        naxis1 = header['NAXIS1']
        crval1 = header['CRVAL1']
        cd1_1 = header['CD1_1']
        fits_flux = hdulist[0].data[0]
    # disable astropy warnings
    warnings.simplefilter('ignore', category=AstropyWarning)
    identifier, wave, flux = lamost.read_dr1_spectrum(lamost_dr1_fits)
    assert identifier == os.path.split(lamost_dr1_fits)[1]
    assert wave.shape[0] == naxis1 and flux.shape[0] == naxis1
    assert flux == pytest.approx(fits_flux)
    assert wave[0] == 10 ** crval1 and wave[1] == 10 ** (crval1 + cd1_1)


def test_preprocess_spectra(data_dir):
    path = os.path.join(data_dir, 'LAMOST-DR2')
    spectra = lamost.preprocess_spectra(path)
    assert isinstance(spectra, pandas.DataFrame)
    # there is 140 wavelengths and a column idicating data corruption
    assert spectra.shape == (14, 141)
