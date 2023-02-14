import tiledb.cloud
from .error import DataError
from .util import getDBType


class Cursor:
    def __init__(self):
        self.results = None
        self.row_index = 0

    def executemany(self, query, size):
        pass

    def execute(self, query):
        self.results = tiledb.cloud.sql.exec(query=query)

    def fetchmany(self, size):
        pass

    def nextset(self):
        pass

    def arraysize(self, size):
        pass

    def setinputsizes(self, sizes):
        pass

    def setoutputsize(self, sizes):
        pass

    def fetchone(self):
        if self.results is None:
            raise DataError("The query results are null")
        if self.row_index < len(self.results):
            row = self.results.iloc[self.row_index]
            self.row_index += 1
            return tuple(row)
        else:
            return None

    def description(self):
        return [(column, getDBType(dtype)) for column, dtype in self.results.dtypes.iteritems()]

    def rowcount(self):
        if self.results is None or len(self.results) == 0:
            return -1
        return len(self.results)

    def fetchall(self):
        if self.results is None:
            raise DataError("The query results are null")
        return list(map(tuple, self.results.values))

    def close(self):
        pass
