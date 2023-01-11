import os
import json
from typing import Any
import cx_Oracle
from typing import AnyStr, Dict
from robot.api import logger
from robotlibcore import keyword
from ..database import Oracle


class OracleKeywords:

    def __init__(self):
        self.oracle = Oracle()

    @keyword
    def create_oracle_connection(self, *args: Any, **kwargs: Any) -> None:
        self.oracle.connection = cx_Oracle.Connection(*args, **kwargs)

    @keyword
    def close_oracle_connection(self, *args: Any, **kwargs: Any) -> None:
        self.oracle.connection.close(*args, **kwargs)

    @keyword
    def commit_oracle_connection(self, *args: Any, **kwargs: Any) -> None:
        self.oracle.connection.commit(*args, **kwargs)

    @keyword
    def oracle_connection_cursor(self, *args: Any, **kwargs: Any) -> None:
        self.oracle_base.cursor = self.oracle_base.connection.cursor(*args, **kwargs)
