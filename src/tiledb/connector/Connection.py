import tiledb.cloud
from Cursor import Cursor


class TileDBConnection:
    def __init__(self, token):
        self.token = token
        tiledb.cloud.login(token=self.token)

    def cursor(self):
        return Cursor()

    def rollback(self):
        pass

    def commit(self):
        pass

    def close(self):
        pass

    def __exit__(self, type, value, traceback):
        pass
