import os
import pandas
from spectraml import lamost


DATA = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data')


def test_read_spectrum():
    """Test if a LAMOST FITS file can be read."""
    f = os.path.join(DATA, 'spec-55916-B5591606_sp01-001.fits')
    identifier, wave, flux = lamost.read_spectrum(f)
    # TODO come up with better test
    assert isinstance(identifier, str)
    assert wave is not None and flux is not None


def test_preprocess_spectra():
    path = os.path.join(DATA, 'LAMOST-DR2')
    spectra = lamost.preprocess_spectra(path)
    assert isinstance(spectra, pandas.DataFrame)
    # there is 140 wavelengths and a column idicating data corruption
    assert spectra.shape == (14, 141)
