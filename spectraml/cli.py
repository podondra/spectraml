import click
import numpy as np
from .lamost import read_spectrum, preprocess_spectra
from .visualize import visualize_spectrum


# TODO implement CLI
@click.group()
def cli():
    pass


@cli.command()
@click.argument('path', type=click.Path(exists=True))  # TODO document
# TODO help message
@click.option('-o', '--out-file', default='data.csv', type=click.File('w'))
def preprocessing(path, out_file):
    # preprocess spectra
    df = preprocess_spectra(path, verbose=True)
    # write them to a out_file
    df.to_csv(out_file)


@cli.command()
@click.argument('filename', type=click.File('rb'))
def visualize(filename):
    visualize_spectrum(*read_spectrum(filename))
