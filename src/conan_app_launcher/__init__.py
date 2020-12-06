"""
Contains global constants and basic/ui variables.
"""
__version__ = "0.6"

from pathlib import Path

# this allows to use forward declarations to avoid circular imports
from typing import TYPE_CHECKING, Optional
if TYPE_CHECKING:
    from .components import ConanWorker
    from PyQt5 import QtWidgets

### Global constants ###
PROG_NAME = "conan_app_launcher"
ICON_SIZE = 64

### Global variables ###
# 0: No debug, 1 = debug logging on
DEBUG_LEVEL = 0

# paths to find folders - points to the folder of this file
base_path: Path = Path(__file__).absolute().parent
default_icon: Path = base_path / "assets" / "default_app_icon.png"

# qt_application instance
qt_app: Optional["QtWidgets.QApplication"] = None
conan_worker: Optional["ConanWorker"] = None
