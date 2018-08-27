"""Package's command line interface."""
import click
from .lamost import read_spectrum, preprocess_spectra
from .visualize import visualize_spectrum


# TODO implement CLI
@click.group()
def cli():
    """Base function for command line interface."""
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True))  # TODO document
# TODO help message
@click.option('-o', '--out-file', default='data.csv', type=click.File('w'))
def preprocessing(path, out_file):
    """Preprocess spectra from FITS files in path/ directory and ouput them
    to file specified as out_file option.
    """
    # preprocess spectra
    preprocessed_spectra = preprocess_spectra(path, verbose=True)
    # write them to a out_file
    preprocessed_spectra.to_csv(out_file)


@cli.command()
@click.argument('filename', type=click.File('rb'))
def visualize(filename):
    """Plot spectrum from FITS file."""
    visualize_spectrum(*read_spectrum(filename))
