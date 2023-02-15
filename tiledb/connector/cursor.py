import tiledb.cloud
from .error import DataError, _Warning, NotSupportedError, ProgrammingError
from .util import getDBType


class Cursor:
    def __init__(self):
        self.results = None
        self.row_index = 0
        self.inputarraysize = 1

    def executemany(self, query):
        self.execute(query)

    def execute(self, query):
        self.results = tiledb.cloud.sql.exec(query=query)

    def fetchmany(self, size=-1):
        if size == -1:
            size = self.inputarraysize

        if size + self.row_index > len(self.results):
            raise DataError("Index out of bounds. There are less values than the input parameter in fetchmany(size). "
                            "Values requested: " + str(size) + ". Values available: " + str(len(
                self.results) - self.row_index))
        rows = self.results.iloc[self.row_index:self.row_index + size]
        self.row_index += size
        return list(map(tuple, rows.values))

    def nextset(self):
        raise NotSupportedError("Operation not supported")

    def arraysize(self, size=1):
        if size < 0:
            raise ProgrammingError("The input parameter for the arraysize() funtion is invalid")
        self.inputarraysize = size

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
        if self.results is None or len(self.results) == 0:
            return None
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
