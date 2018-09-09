import os
import pytest
import pandas as pd
from spectraml import xmatch


@pytest.fixture
def candidates_catalogue(datadir):
    return pd.read_csv(os.path.join(datadir, 'candidates-catalogue.csv'))


@pytest.fixture
def hou_catalogue(datadir):
    return pd.read_csv(os.path.join(datadir, 'hou-catalogue.csv'))


def test_xmatch(candidates_catalogue, hou_catalogue):
    """Test if xmatch produces correct results."""
    # do cross-matching
    result = xmatch.xmatch(candidates_catalogue, hou_catalogue)
    assert result.shape == (3, 18)
    true_designations = [
        'J064051.15+100137.8',
        'J064033.18+102233.7',
        'J051501.72+325139.6'
    ]
    assert all(result['designation'].values == true_designations)
