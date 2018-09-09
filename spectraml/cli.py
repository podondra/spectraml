"""Package's command line interface."""
import click
import h5py
import pandas as pd
from .lamost import read_spectrum
from .preprocessing import preprocess_spectra
from .visualize import visualize_spectrum
from .xmatch import xmatch as cross_match


@click.group()
def cli():
    """Base function for command line interface."""
    pass


@cli.command()
@click.argument('hdf5', type=click.Path())
@click.argument('group')
@click.argument('fits_list', type=click.File('r'))
@click.option(
    '-s', '--start', default=6519, help='Resampled wavelengths start.'
)
@click.option(
    '-e', '--end', default=6732, help='Resampled wavelengths end.'
)
@click.option(
    '-w', '--wavelenghts', default=140,
    help='Number of wavelenghts to resample to.'
)
def preprocessing(hdf5, group, fits_list, start, end, wavelenghts):
    """Preprocess FITS files from FITS_LIST into HDF5 file."""
    hdf5_file = h5py.File(hdf5, 'w')
    fits_files_list = fits_list.read().splitlines()
    preprocess_spectra(
        hdf5_file, group,
        fits_files_list, read_spectrum,
        start, end, wavelenghts
    )


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
