class Error(Exception):
    """Base class for exceptions in the DB API 2.0 implementation."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Generic error: " + self.message


class InterfaceError(Error):
    """Raised when the database encountered a programming error."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Interface error: " + self.message


class DatabaseError(Error):
    """Raised when the database encountered a programming error."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Database error: " + self.message


class _Warning(Exception):
    """Exception for important warnings."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Warning: " + self.message


class ProgrammingError(Error):
    """Raised when the database encountered a programming error."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Programming error: " + self.message


class DataError(Error):
    """Raised when the database encountered data-related errors."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Data error: " + self.message


class OperationalError(Error):
    """Raised when the database encountered operational errors."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Operational error: " + self.message


class IntegrityError(Error):
    """Raised when the database encountered an integrity constraint error."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Integrity error: " + self.message


class InternalError(Error):
    """Raised when the database encountered an internal error."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "Internal error: " + self.message


class NotSupportedError(Error):
    """Raised when the database encountered a feature not supported error."""

    def __init__(self, message):
        self.message = message

    def __str__(self):
        return "NotSupported error: " + self.message
