import tiledb.cloud
from .error import DataError, _Warning, NotSupportedError, ProgrammingError
from .util import getDBType


class Cursor:
    def __init__(self):
        self.results = None
        self.row_index = 0
        self.inputarraysize = 1
        self.description_cache = None

    def executemany(self, query):
        self.execute(query)

    def execute(self, query):
        try:
            self.results = tiledb.cloud.sql.exec(query=query, raw_results=True)
        except Exception as e:
            self.results = None
            raise DataError(f"Error executing query: {str(e)}")

    def fetchmany(self, size=-1):
        if self.results is None or len(self.results) == 0:
            return None

        if size == -1:
            size = self.inputarraysize

        if size + self.row_index > len(self.results):
            # give all that is remaining
            size = len(self.results) - self.row_index

        if size == 0:
            # There are no more records
            return None

        rows = self.results[self.row_index:self.row_index + size]
        self.row_index += size
        return rows.to_pylist()

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
        return self.fetchmany(1)

    def description(self):
        if self.description_cache is not None:
            return self.description_cache

        if self.results is None or len(self.results) == 0:
            return None

        description = [(field.name, getDBType(field.type)) for field in self.results.schema]
        self.description_cache = description
        return description

    def rowcount(self):
        if self.results is None or len(self.results) == 0:
            return -1
        return len(self.results)

    def fetchall(self):
        if self.row_index > 0:
            return self.fetchmany(len(self.results) - self.row_index)
        if self.results is None:
            raise DataError("The query results are null")
        return self.results.to_pylist()

    def close(self):
        self.row_index = 0
        self.inputarraysize = 1
