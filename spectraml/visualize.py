from matplotlib import pyplot as plt


def visualize_spectrum(wave, flux):
    plt.plot(wave, flux)
    plt.xlabel('wavelength')
    plt.ylabel('flux')
    plt.show()
