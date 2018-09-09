import os
import pytest
from astropy.io import fits
from spectraml import ondrejov


@pytest.fixture
def ondrejov_fits(datadir):
    """Ondrejov's FITS file fixture."""
    return os.path.join(datadir, 'oe270005.fits')


def test_read_spectrum(ondrejov_fits):
    """Test reading of Ondrejov's FITS file."""
    with fits.open(ondrejov_fits) as hdulist:
        header = hdulist[0].header
        fits_identifier = header['OBJECT']
        naxis1 = header['NAXIS1']
        fits_flux = hdulist[0].data
        crval1 = header['CRVAL1']
        cdelt1 = header['CDELT1']
    identifier, wave, flux = ondrejov.read_spectrum(ondrejov_fits)
    # check correct identifier
    assert identifier == fits_identifier
    # check correct shapes
    assert wave.shape[0] == naxis1 and flux.shape[0] == naxis1
    # check correct flux
    assert flux == pytest.approx(fits_flux)
    # check that first and second wavelenghts are correctly computed
    assert wave[0] == crval1 and wave[1] == crval1 + cdelt1
