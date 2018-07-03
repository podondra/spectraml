import numpy as np


START = 6519
END = 6732
N_WAVELENGTHS = 140


def interp_flux(wave, flux, new_wave=np.linspace(START, END, N_WAVELENGTHS)):
    return new_wave, np.interp(new_wave, wave, flux)


def preprocess_spectrum(wave, flux):
    new_wave, new_flux = interp_flux(wave, flux)
    return new_wave, new_flux
