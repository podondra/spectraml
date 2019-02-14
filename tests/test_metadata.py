from astropy.io import fits
from spectraml import metadata


def test_get_mag_r(lamost_fits):
    with fits.open(lamost_fits) as hdulist:
        mag_r = metadata.get_mag_r(hdulist[0].header)
    assert mag_r == 9.199999999999999
