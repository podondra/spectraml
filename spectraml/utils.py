"""Various utilities for spectra management."""


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
