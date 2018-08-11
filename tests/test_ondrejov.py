import os
import pytest
from spectraml import ondrejov


@pytest.fixture
def ondrejov_fits(data_dir):
    return os.path.join(data_dir, 'oe270005.fits')


def test_read_spectrum(ondrejov_fits):
    identifier, wave, flux = ondrejov.read_spectrum(ondrejov_fits)
    # TODO come up with better test
    assert isinstance(identifier, str)
    assert wave is not None and flux is not None
