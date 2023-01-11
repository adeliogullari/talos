import os
import json
from typing import AnyStr, Dict
from robot.api import logger
from robotlibcore import keyword


class FileKeywords:

    def __init__(self):
        pass

    def _create_file_if_not_exists(self, file: AnyStr) -> None:
        if not os.path.exists(os.path.dirname(file)):
            try:
                os.makedirs(os.path.dirname(file))
            except OSError as e:
                logger.error(f"OSError Code: {e.errno}")
                logger.error(f"OSError Message: {e.strerror}")
                raise

    @keyword
    def read_from_file(self,
                       file: str,
                       mode: str = 'r',
                       buffering=None,
                       encoding: str = 'UTF-8',
                       errors=None,
                       newline=None,
                       closefd=True) -> str:

        if os.path.isfile(file) and os.access(file, os.R_OK):
            try:
                with open(file=file,
                          mode=mode,
                          buffering=buffering,
                          encoding=encoding,
                          errors=errors,
                          newline=newline,
                          closefd=closefd) as f:
                    return f.read()
            except IOError as e:
                logger.error(f"IOError Code: {e.errno}")
                logger.error(f"IOError Message: {e.strerror}")
                raise

    @keyword
    def write_to_file(self,
                      data: str,
                      file: str,
                      mode: str = 'w+',
                      buffering=None,
                      encoding: str = 'UTF-8',
                      errors=None,
                      newline=None,
                      closefd=True) -> None:

        self._create_file_if_not_exists(file)
        try:
            with open(file=file,
                      mode=mode,
                      buffering=buffering,
                      encoding=encoding,
                      errors=errors,
                      newline=newline,
                      closefd=closefd) as f:
                f.write(data)
        except IOError as e:
            logger.error(f"IOError Code: {e.errno}")
            logger.error(f"IOError Message: {e.strerror}")
            raise

    @keyword
    def load_from_json_file(self,
                            file: str,
                            mode: str = 'r',
                            buffering=None,
                            encoding: str = 'UTF-8',
                            errors=None,
                            newline=None,
                            closefd=True) -> Dict:
        if os.path.isfile(file) and os.access(file, os.R_OK):
            try:
                with open(file=file,
                          mode=mode,
                          buffering=buffering,
                          encoding=encoding,
                          errors=errors,
                          newline=newline,
                          closefd=closefd) as f:
                    return json.load(f)
            except json.decoder.JSONDecodeError as e:
                logger.error(f"JSONDecodeError Message: {e.msg}")
                raise

# class FileOperationsKeywords:
#
#     def __init__(self):
#         pass
#
#     def _create_file_if_not_exists(self, file: AnyStr) -> None:
#         if not os.path.exists(os.path.dirname(file)):
#             try:
#                 os.makedirs(os.path.dirname(file))
#             except OSError as e:
#                 logger.error(f"OSError Code: {e.errno}")
#                 logger.error(f"OSError Message: {e.strerror}")
#                 raise
#
#     @keyword
#     def read_from_file(self, file: AnyStr, mode: AnyStr = 'r', encoding: AnyStr = 'UTF-8') -> AnyStr:
#         if os.path.isfile(file) and os.access(file, os.R_OK):
#             try:
#                 with open(file=file, mode=mode, encoding=encoding) as f:
#                     return f.read()
#             except IOError as e:
#                 logger.error(f"IOError Code: {e.errno}")
#                 logger.error(f"IOError Message: {e.strerror}")
#                 raise
#
#     @keyword
#     def write_to_file(self, data: AnyStr, file: AnyStr, mode: AnyStr = 'w+', encoding: AnyStr = 'UTF-8') -> None:
#         self._create_file_if_not_exists(file)
#         try:
#             with open(file=file, mode=mode, encoding=encoding) as f:
#                 f.write(data)
#         except IOError as e:
#             logger.error(f"IOError Code: {e.errno}")
#             logger.error(f"IOError Message: {e.strerror}")
#             raise
#
#     @keyword
#     def load_from_json_file(self, file: AnyStr, mode: AnyStr = 'r', encoding: AnyStr = 'UTF-8') -> Dict:
#         if os.path.isfile(file) and os.access(file, os.R_OK):
#             try:
#                 with open(file=file, mode=mode, encoding=encoding) as f:
#                     return json.load(f)
#             except json.decoder.JSONDecodeError as e:
#                 logger.error(f"JSONDecodeError Message: {e.msg}")
#                 raise
#
#     @keyword
#     def dump_to_json_file(self, data: Dict, file: AnyStr, mode: AnyStr = 'w+', encoding: AnyStr = 'UTF-8') -> None:
#         self._create_file_if_not_exists(file)
#         try:
#             with open(file=file, mode=mode, encoding=encoding) as f:
