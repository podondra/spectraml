"""Package's command line interface."""
import click
import pandas as pd
from .lamost import read_spectrum, preprocess_spectra
from .visualize import visualize_spectrum
from .xmatch import xmatch as cross_match


@click.group()
def cli():
    """Base function for command line interface."""
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True))
@click.option(
    '-o', '--out-file', default='data.csv', type=click.File('w'),
    help='File in which to output preprocessing result.'
)
def preprocessing(path, out_file):
    """Preprocess spectra from FITS files in PATH/ directory and ouput them
    to file specified as out_file option.
    """
    # preprocess spectra
    preprocessed_spectra = preprocess_spectra(path, verbose=True)
    # write them to a out_file
    preprocessed_spectra.to_csv(out_file)


@cli.command()
@click.argument('filename', type=click.File('rb'))
def visualize(filename):
    """Plot spectrum from LAMOST DR2 FITS file."""
    visualize_spectrum(*read_spectrum(filename))


@cli.command()
@click.argument('left', type=click.File('r'))
@click.argument('right', type=click.File('r'))
@click.option(
    '--left-on', default='designation', help='Left column to cross-match on.'
)
@click.option(
    '--right-on', default='designation', help='Right column to cross-match on.'
)
def xmatch(left, right, left_on, right_on):
    """Cross-match two well formated CSV files on provided columns.
    It automatically removes duplicities. If no options are provided
    cross-match on 'designation' columns.
    """
    click.echo(cross_match(
        pd.read_csv(left), pd.read_csv(right),
        left_on=left_on, right_on=right_on
    ).to_csv(index=False), nl=False)
