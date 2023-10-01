"""Version information about this library."""

from importlib.metadata import PackageNotFoundError, version


def get_version():
    """Returns a version string to the caller."""
    semver = "0.0.0:Not-Packaged-DEVELOPMENT-VERSION"
    __version__ = f"{semver}"
    try:
        __version__ = version("pronom-tools")
    except PackageNotFoundError:
        # package is not installed
        pass
    return __version__
