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
