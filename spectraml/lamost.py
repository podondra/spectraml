import numpy as np
from astropy.io import fits
from click import progressbar
from .preprocessing import N_WAVELENGTHS, interp_flux, preprocess_spectrum
from .utils import gen_files_with_ext


def read_spectrum(filename):
    """Read a LAMOST spectrum from a FITS file."""
    with fits.open(filename) as hdulist:
        # assert wavelengths are vacuum
        header = hdulist[0].header
        assert header['VACUUM']
        # the FITS in LAMOST DR2 has 1 HDU the primary HDU
        # the data unit contains Flux, Inverse Variance,
        #   Wavelength, Andmask, Ormask
        flux = hdulist[0].data[0]
        wave = hdulist[0].data[2]
    return wave, flux


def preprocess_spectra(path, the_ext='.fits'):
    fits_files = list(gen_files_with_ext(path, the_ext))
    spectra = np.zeros((len(fits_files), N_WAVELENGTHS))
    with progressbar(enumerate(fits_files)) as bar:
        for idx, f in bar:
            wave, flux = read_spectrum(f)
            _, spectra[idx] = preprocess_spectrum(wave, flux)
    return spectra
