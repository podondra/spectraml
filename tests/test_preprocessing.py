import numpy as np
from spectraml import preprocessing


def test_convert_air2vacuum():
    """Test that air Halpha wavelenght is converted to vacuum wavelenght."""
    air_halpha = np.array([6562.801])
    vaccum_halpha = preprocessing.convert_air2vacuum(air_halpha)
    assert np.allclose(vaccum_halpha, [6564.614])
