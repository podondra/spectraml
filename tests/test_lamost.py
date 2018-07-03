import os
from spectraml import lamost


DATA = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


def test_read_spectrum():
    """Test if a LAMOST FITS file can be read."""
    f = os.path.join(DATA, 'spec-55916-B5591606_sp01-001.fits')
    wave, flux = lamost.read_spectrum(f)
    # TODO come up with better test
    assert wave is not None and flux is not None


def test_preprocess_spectra():
    path = os.path.join(DATA, 'LAMOST-DR2')
    spectra = lamost.preprocess_spectra(path)
    assert spectra.shape == (14, 140)
