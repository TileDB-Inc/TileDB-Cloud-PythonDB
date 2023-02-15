apilevel = "2.0"
threadsafety = 2
paramstyle = "pyformat"

from .cursor import Cursor
from .connection import TileDBConnection
from .error import (
    DatabaseError,
    DataError,
    Error,
    IntegrityError,
    InterfaceError,
    InternalError,
    NotSupportedError,
    OperationalError,
    ProgrammingError,
    _Warning,
)


def Connect(**kwargs) -> TileDBConnection:
    return TileDBConnection(**kwargs)
