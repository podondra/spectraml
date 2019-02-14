def get_mag_r(header):
    """Return r magnitude from FITS header or None."""
    # get magtype to locate r magnitude
    magtype = header['MAGTYPE']
    try:
        # get value of the r magnitude
        return header['MAG' + str(magtype.index('r') + 1)]
    except ValueError:
        # on exception return None
        return None
