"""Module for manipulation with Ondrejov's spectra."""
import numpy
from astropy import wcs
from astropy.io import fits


def compute_wave(hdulist):
    """Compute spectrum's wavelengths from Ondřejov FITS file."""
    header = hdulist[0].header
    wcs_object = wcs.WCS(header)
    pixcrd = numpy.arange(header['NAXIS1'])
    return wcs_object.all_pix2world(pixcrd, 0)[0]


def read_spectrum(filename):
    """Return tuple of identifier, wavelengths and fluxes from Ondřejov
    FITS file.
    """
    with fits.open(filename) as hdulist:
        primary_hdu = hdulist[0]
        identifier = primary_hdu.header['OBJECT']
        wave = compute_wave(hdulist)
        flux = primary_hdu.data
    return identifier, wave, flux
