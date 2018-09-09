"""Module for manipulation with LAMOST's spectra."""
from astropy import wcs
from astropy.io import fits
import numpy


def read_spectrum(filename):
    """Read a LAMOST spectrum from a FITS file."""
    with fits.open(filename) as hdulist:
        # assert wavelengths are vacuum
        header = hdulist[0].header
        assert header['VACUUM']
        # the FITS in LAMOST DR2 has 1 HDU the primary HDU
        # the data unit contains Flux, Inverse Variance,
        #   Wavelength, Andmask, Ormask
        identifier = header['FILENAME']
        flux = hdulist[0].data[0]
        wave = hdulist[0].data[2]
    return identifier, wave, flux


def read_dr1_spectrum(filename):
    """Read a LAMOST DR1 spectrum from a FITS file."""
    with fits.open(filename) as hdulist:
        header = hdulist[0].header
        identifier = header['FILENAME']
        # flux is first row of data unit
        flux = hdulist[0].data[0]
        # lenght of first data axis
        naxis1 = header['NAXIS1']
        # pixels that such be tranformed to wavelengths
        # has to have shape (naxis1, naxis) where naxis is number of axis in
        # the FITS file
        pixcr = numpy.arange(naxis1).reshape(-1, 1)[:, [0, 0]]
        # compute the wavelenghts and get first column
        # note that wavelenghts are logarithmic thefore they have to be
        # transformed to linear wavelenghts
        wave = 10 ** wcs.WCS(header).wcs_pix2world(pixcr, 0)[:, 0]
    return identifier, wave, flux
