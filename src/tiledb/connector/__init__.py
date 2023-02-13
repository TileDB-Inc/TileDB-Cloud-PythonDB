apilevel = "2.0"
threadsafety = 2
paramstyle = "pyformat"

from .Cursor import Cursor
from .Connection import TileDBConnection
from .Error import (
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
