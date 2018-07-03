import warnings
import numpy as np
from astropy.io import fits
from .preprocessing import N_WAVELENGTHS, interp_flux, preprocess_spectrum
from .utils import gen_files_with_ext


def read_spectrum(filename):
    """Read a LAMOST spectrum from a FITS file."""
    with fits.open(filename) as hdulist:
        # the FITS in LAMOST DR2 has 1 HDU the primary HDU
        # the data unit contains Flux, Inverse Variance,
        #   Wavelegth, Andmask, Ormask
        flux = hdulist[0].data[0]
        wave = hdulist[0].data[2]
    return wave, flux


def preprocess_spectra(path, the_ext='.fits'):
    fits_files = list(gen_files_with_ext(path, the_ext))
    spectra = np.zeros((len(fits_files), N_WAVELENGTHS))
    for idx, f in enumerate(fits_files):
        wave, flux = read_spectrum(f)
        _, spectra[idx] = preprocess_spectrum(wave, flux)
    return spectra


# TODO use click for CLI
def main():
    s = preprocess_spectra('/data/podondra/spectraml/tests/data/LAMOST-DR2')
    np.savetxt('spectra.csv', s, delimiter=',')
