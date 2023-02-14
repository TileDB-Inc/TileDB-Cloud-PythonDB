import tiledb.cloud
from .error import DataError, _Warning, NotSupportedError
from .util import getDBType


class Cursor:
    def __init__(self):
        self.results = None
        self.row_index = 0
        self.fetchmanysize = 1

    def executemany(self, query):
        self.execute(query)

    def execute(self, query):
        self.results = tiledb.cloud.sql.exec(query=query)

    def fetchmany(self):
        if self.fetchmanysize + self.row_index > len(self.results):
            raise DataError("Index out of bounds. There are less values than the input parameter in fetchmany(size). "
                            "Values requested: " + str(self.fetchmanysize) + ". Values available: " + str(len(
                self.results) - self.row_index))
        rows = self.results.iloc[self.row_index:self.row_index + self.fetchmanysize]
        self.row_index += self.fetchmanysize
        return list(map(tuple, rows.values))

    def nextset(self):
        raise NotSupportedError("Operation not supported")

    def arraysize(self, size=1):
        self.fetchmanysize = size

    def setinputsizes(self, sizes):
        raise NotSupportedError("Operation not supported")

    def setoutputsize(self, sizes):
        raise NotSupportedError("Operation not supported")

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
