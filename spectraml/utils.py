import os


def gen_files_with_ext(path, the_ext):
    # check if path exists
    if not os.path.exists(path):
        raise FileNotFoundError
    # walk given path to find all FITS files
    for root, dirs, files in os.walk(path):
        for f in files:
            # get f's extension
            name, ext = os.path.splitext(f)
            if ext == the_ext:
                yield os.path.join(root, f)
