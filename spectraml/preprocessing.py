"""Preprocessing module with different tools to manipulate spectra."""
import os
import warnings
from astropy import convolution
from astropy.utils.exceptions import AstropyWarning
import click
import h5py
import numpy as np


def interp_flux(wave, flux, new_wave):
    """Interpolates flux from old wavelengths to new wavelengths."""
    # TODO write a test
    return new_wave, np.interp(new_wave, wave, flux)


def convert_air2vacuum(air_wave):
    """Convert air wavelengths to vacuum wavelengths according to
    http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion.
    """
    s_square = ((10 ** 4) / air_wave) ** 2
    return air_wave * (1 + 0.00008336624212083 + 0.02408926869968 / \
            (130.1065924522 - s_square) + 0.0001599740894897 / \
            (38.92568793293 - s_square))


def convolve_flux(flux, kernel=convolution.Gaussian1DKernel(stddev=7)):
    """Perform convolution with kernel of spectrum's fluxes.

    Default is Gaussian kernel with standard deviation of value 7.
    """
    # TODO write a test
    return convolution.convolve(flux, kernel, boundary='extend')


def preprocess_spectrum(
        wave, flux, new_wave, air2vacuum=False, convolve=False
    ):
    """Wrapper function which applies preprocessing functions according
    to provided parameters.
    """
    # TODO write a test
    if air2vacuum:
        wave = convert_air2vacuum(wave)
    if convolve:
        flux = convolve_flux(flux)
    wave, flux = interp_flux(wave, flux, new_wave)
    return wave, flux


def preprocess_spectra(
        hdf5_group, new_group,
        fits_list, fits_reader,
        start, end, n_wavelengths
    ):
    """Preprocess spectra from fits_list using fits_reader function to
    extract identifier, wavelengths and fluxes. Save the spectra
    is hdf5_group group of a hdf5 file. Spectra are resampled according to
    start, end and n_wavelengths parameters."""
    # disable astropy's warnings
    warnings.simplefilter('ignore', category=AstropyWarning)

    # create group and datasets in the hdf5 file
    n_fits = len(fits_list)
    group = hdf5_group.create_group(new_group)
    str_dt = h5py.special_dtype(vlen=str)
    filenames = group.create_dataset('filenames', (n_fits,), str_dt)
    spectra = group.create_dataset('spectra', (n_fits, n_wavelengths), np.float)
    corrupted = group.create_dataset('corrupted', (n_fits,), dtype=np.bool_)

    # wavelengths to resample to
    new_wave = np.linspace(start, end, n_wavelengths, dtype=np.float)
    wavelengths = group.create_dataset('wavelengths', (n_wavelengths,), np.float)
    wavelengths[...] = new_wave
    with click.progressbar(fits_list) as fits_list_bar:
        for idx, filename in enumerate(fits_list_bar):
            # if file does not exist raise Exception
            if not os.path.isfile(filename):
                raise Exception('{} does not exists'.format(filename))
            try:
                identifier, wave, flux = fits_reader(filename)
            # WARNING: File may have been truncated
            # results in TypeError: buffer is too small for requested array
            except (OSError, TypeError):
                filenames[idx] = os.path.basename(filename)
                corrupted[idx] = True
                continue
            filenames[idx] = identifier
            _, spectra[idx] = preprocess_spectrum(wave, flux, new_wave)
