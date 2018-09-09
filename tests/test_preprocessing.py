import h5py
import numpy as np
import os
import pytest
from spectraml import lamost, preprocessing


def test_convert_air2vacuum():
    """Test that air Halpha wavelenght is converted to vacuum wavelenght."""
    air_halpha = np.array([6562.801])
    vaccum_halpha = preprocessing.convert_air2vacuum(air_halpha)
    assert np.allclose(vaccum_halpha, [6564.614])


@pytest.fixture
def lamost_dr2_fits_list(datadir):
    """Path to file with FITS files."""
    return os.path.join(datadir, 'lamost-dr2-fits.lst')


def test_preprocess_spectra(tmpdir, lamost_dr2_fits_list):
    """Test spectra preprocessing."""
    hdf5_file = h5py.File(tmpdir.join('spectra.hdf5'), 'w')
    with open(lamost_dr2_fits_list) as fits_list_file:
        fits_list = fits_list_file.read().splitlines()

    n_wavelengths = 100
    preprocessing.preprocess_spectra(
        hdf5_file, new_group='lamost_dr2',
        fits_list=fits_list, fits_reader=lamost.read_spectrum,
        start=6519, end=6732, n_wavelengths=100
    )

    the_group = hdf5_file['lamost_dr2']
    assert the_group['spectra'].shape == (13, n_wavelengths)
    assert the_group['filenames'].shape == (13,)
    assert the_group['filenames'][1] == 'spec-56257-GAC089N38V2_sp01-006.fits'

    hdf5_file.close()
