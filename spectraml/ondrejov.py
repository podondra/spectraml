import numpy
from astropy import wcs
from astropy.io import fits


def compute_wave(hdulist):
    """Compute spectrum's wavelengths from Ondřejov FITS file."""
    header = hdulist[0].header
    w = wcs.WCS(header)
    pixcrd = numpy.arange(header['NAXIS1'])
    return w.all_pix2world(pixcrd, 0)[0]


def read_spectrum(filename):
    """Return tuple of identifier, wavelengths and fluxes from Ondřejov
    FITS file.
    """
    with fits.open(filename) as hdulist:
        identifier = hdulist[0].header['OBJECT']
        wave = compute_wave(hdulist)
        flux = hdulist[0].data
    return identifier, wave, flux
