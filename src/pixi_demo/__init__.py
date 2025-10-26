# src/my_awesome_package/__init__.py

try:
    from ._version import __version__
except ImportError:
    # Fallback for development without building
    __version__ = "0.0.0.dev0"

# Expose version in package
__all__ = ["__version__"]

#Now users can check version:
#>>> import my_awesome_package
#>>> print(my_awesome_package.__version__)
#1.2.3