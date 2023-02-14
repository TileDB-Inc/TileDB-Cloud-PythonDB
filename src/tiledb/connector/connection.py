import tiledb.cloud

from .error import NotSupportedError
from .cursor import Cursor


class TileDBConnection:
    def __init__(self, token):
        self.token = token
        tiledb.cloud.login(token=self.token)

    def cursor(self):
        return Cursor()

    def rollback(self):
        raise NotSupportedError("Operation not supported")

    def commit(self):
        raise NotSupportedError("Operation not supported")

    def close(self):
        pass

    def __exit__(self, type, value, traceback):
        pass
