import numpy
from astropy import convolution


START = 6519
END = 6732
N_WAVELENGTHS = 140


def interp_flux(
        wave, flux, new_wave=numpy.linspace(START, END, N_WAVELENGTHS)
        ):
    # TODO write a test
    return new_wave, numpy.interp(new_wave, wave, flux)


def air2vacuum(air_wave):
    """Convert air wavelengths to vacuum wavelengths according to
    http://www.astro.uu.se/valdwiki/Air-to-vacuum%20conversion.
    """
    # TODO write a test
    s = ((10 ** 4) / air_wave) ** 2
    return air_wave * (1 + 0.00008336624212083 + 0.02408926869968 / \
            (130.1065924522 - s) + 0.0001599740894897 / (38.92568793293 - s))


def convolve_flux(flux, kernel=convolution.Gaussian1DKernel(stddev=7)):
    """Perform convolution with kernel of spectrum's fluxes.

    Default is Gaussian kernel with standard deviation of value 7.
    """
    # TODO write a test
    return convolution.convolve(flux, kernel, boundary='extend')


def preprocess_spectrum(wave, flux, air2vacuum=False, convolve=False):
    # TODO write a test
    if air2vacuum:
        wave = air2vacuum(wave)
    if convolve:
        flux = convolve_flux(flux)
    wave, flux = interp_flux(wave, flux)
    return wave, flux
