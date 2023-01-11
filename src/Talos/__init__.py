from robotlibcore import DynamicCore
from .keywords import FileKeywords, OracleKeywords, RequestKeywords


__version__ = "1.0.0"


class Talos(DynamicCore):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):

        library_components = [FileKeywords(),
                              OracleKeywords(),
                              RequestKeywords()]

        DynamicCore.__init__(self, library_components)
