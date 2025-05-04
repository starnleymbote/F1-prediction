__version__ = "0.1.0"

from .constant import BASE_URL, MAX_RETRIES
from .api_data import ApiData

__all__ = [
    "BASE_URL",
    "MAX_RETRIES",
    "ApiData",
]
# This module imports the BASE_URL and MAX_RETRIES constants from the constant.py file
# and makes them available for use in other parts of the application.
# The __all__ list specifies which names should be considered public and accessible
# when the module is imported with a wildcard import (e.g., from . import *).
# This is useful for encapsulating the module's public API and preventing
# accidental access to internal names.
# The __version__ variable is also defined to indicate the version of the module.
# This can be useful for versioning and tracking changes in the module.
