"""Various utilities for spectra management."""
import os


def gen_files_with_ext(path, the_ext):
    """Generator of files with specific extension under path/ directory."""
    # check if path exists
    if not os.path.exists(path):
        raise FileNotFoundError
    # walk given path to find all FITS files
    for root, _, files in os.walk(path):
        for filename in files:
            # get f's extension
            _, ext = os.path.splitext(filename)
            if ext == the_ext:
                yield os.path.join(root, filename)


def split_according_to_profile(data):
    """Return 2 pandas.DataFrames. The first one contains only emission
    spectra and the second all others. Usually only double-peak profiles.

    The data pandas.DataFrame has to have a profile column.
    """
    emission_index = data['profile'] == 'emission'
    return data[emission_index], data[~emission_index]


def remove_duplicities(data, column):
    """Remove rows from data which has same values in a column.

    Keep the first entry and remove all others from data.

    data is a pandas.DataFrame and
    column is the column whete to look for duplicities.
    """
    return data[~data[column].duplicated()]
