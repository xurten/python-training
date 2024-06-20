class Error(Exception):
    """Base class for all exceptions"""


class InvalidDensityError(Error):
    """Density error"""


class InvalidVolumeError(Error):
    """Problem with volume"""


def determine_weight(volume, density):
    if density < 0:
        raise InvalidDensityError('Density bust be positive')
    if volume < 0:
        raise InvalidVolumeError('Volume must be positive')
    return volume/density
