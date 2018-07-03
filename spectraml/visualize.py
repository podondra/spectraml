from matplotlib import pyplot as plt


def visualize_spectrum(identifier, wave, flux):
    plt.title(identifier)
    plt.plot(wave, flux)
    plt.xlabel('wavelength')
    plt.ylabel('flux')
    plt.show()
