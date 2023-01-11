from typing import Optional
from cx_Oracle import Connection, Cursor, SessionPool, Var
from src.Talos.decorator import Singleton


@Singleton
class Oracle:

    def __init__(self):
        self.__connection: Optional[Connection] = None
        self.__cursor: Optional[Cursor] = None
        self.__session_pool: Optional[SessionPool] = None
        self.__var: Optional[Var] = None

    @property
    def connection(self) -> Connection:
        return self.__connection

    @connection.setter
    def connection(self, value: Connection):
        self.__connection = value

    @connection.deleter
    def connection(self):
        del self.__connection

    @property
    def cursor(self) -> Cursor:
        return self.__cursor

    @cursor.setter
    def cursor(self, value: Cursor):
        self.__cursor = value

    @cursor.deleter
    def cursor(self):
        del self.__cursor

    @property
    def session_pool(self) -> SessionPool:
        return self.__session_pool

    @session_pool.setter
    def session_pool(self, value: SessionPool):
        self.__session_pool = value

    @session_pool.deleter
    def session_pool(self):
        del self.__session_pool

    @property
    def var(self) -> Var:
        return self.__var

    @var.setter
    def var(self, value: Var):
        self.__var = value

    @var.deleter
    def var(self):
        del self.__var
