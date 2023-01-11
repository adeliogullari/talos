from robotlibcore import DynamicCore
# from .keywords import PoolBuilderKeywords
# from .keywords import KafkaHandlerKeywords
# from .keywords import FileOperationsKeywords
# from .keywords import RequestManagerKeywords
# from .keywords import OracleDatabaseKeywords
# from .keywords import DictionaryHandlerKeywords
# from .keywords import RandomDataGeneratorKeywords


__version__ = "1.0.0"


class Talos(DynamicCore):

    ROBOT_LIBRARY_SCOPE = "GLOBAL"
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self):

        library_components = []

        # PoolBuilderKeywords(),
        # KafkaHandlerKeywords(),
        # FileOperationsKeywords(),
        # RequestManagerKeywords(),
        # OracleDatabaseKeywords(),
        # DictionaryHandlerKeywords(),
        # RandomDataGeneratorKeywords()

        DynamicCore.__init__(self, library_components)