"""Function for cross-matching of spectra in form of pandas.DataFrames."""
import pandas as pd
from .utils import remove_duplicities


def xmatch(left, right, left_on='designation', right_on='designation'):
    """Cross-match data from left and right pandas.DataFrames on right_on
    and left_on columns. Use pd.merge's inner join.
    """
    return pd.merge(
        remove_duplicities(left, left_on),
        remove_duplicities(right, right_on),
        left_on=left_on, right_on=right_on
    )
