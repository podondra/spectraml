import os
import warnings
import numpy
import pandas
from astropy.io import fits
from astropy.utils.exceptions import AstropyWarning
import click
from .preprocessing import START, END, N_WAVELENGTHS, preprocess_spectrum
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
        identifier = header['FILENAME']
        flux = hdulist[0].data[0]
        wave = hdulist[0].data[2]
    return identifier, wave, flux


def read_dr1_spectrum(filename):
    # TODO read a LAMOST DR1 spectrum
    raise NotImplementedError


def preprocess_spectra(path, the_ext='.fits', verbose=False):
    fits_files = list(gen_files_with_ext(path, the_ext))

    # disable warnings
    warnings.simplefilter('ignore', category=AstropyWarning)

    identifiers = list()
    fluxes = numpy.zeros((len(fits_files), N_WAVELENGTHS))
    corrupted = numpy.zeros(len(fits_files), dtype=numpy.bool_)

    if verbose:
        fits_files = click.progressbar(fits_files)
        fits_files.__enter__()

    for idx, f in enumerate(fits_files):
        try:
            identifier, wave, flux = read_spectrum(f)
        # WARNING: File may have been truncated
        # results in TypeError: buffer is too small for requested array
        except (OSError, TypeError) as e:
            identifiers.append(os.path.basename(f))
            corrupted[idx] = True
            continue
        identifiers.append(identifier)
        _, fluxes[idx] = preprocess_spectrum(wave, flux)

    if verbose:
        fits_files.__exit__(None, None, None)

    # construct pandas DataFrame
    df = pandas.DataFrame(
            fluxes,
            index=identifiers,
            columns=numpy.linspace(START, END, N_WAVELENGTHS)
            )
    df['corrupted'] = corrupted
    df.index.name = 'identifier'
    return df
