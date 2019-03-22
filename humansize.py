SUFFIXES = ['KB', 'MB', 'GB', 'TB', 'PB', 'EB','ZB','YB']

def approximate_size(size=100000):
    """ Convert a file size to human-readable form.
    Keyword arguments:
    sisze -- file size in bytes

    Return: string
    """
    multiple = 1024
    for suffix in SUFFIXES:
        size /= multiple
        if size < multiple:
            return f'{size} {suffix}'
        raise ValueError('number too large')