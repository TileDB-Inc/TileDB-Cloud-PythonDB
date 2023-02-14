# This file includes the datatype mapping from pandas to the types required by the Python DB API 2.0
import pandas as pd
from pandas.api.types import is_numeric_dtype
from pandas.api.types import is_string_dtype
from pandas.api.types import is_bool_dtype
from pandas.api.types import is_datetime64_dtype
from pandas.api.types import is_datetime64_any_dtype
from pandas.api.types import is_datetime64_ns_dtype
from pandas.api.types import is_datetime64tz_dtype
from pandas.api.types import is_timedelta64_dtype
from pandas.api.types import is_timedelta64_ns_dtype


def getDBType(dtype):
    if is_datetime64_any_dtype(dtype):
        return 'DATETIME'
    if is_datetime64_dtype(dtype):
        return 'DATETIME'
    if is_datetime64_ns_dtype(dtype):
        return 'DATETIME'
    if is_datetime64tz_dtype(dtype):
        return 'DATETIME'
    if is_timedelta64_dtype(dtype):
        return 'DATETIME'
    if is_timedelta64_ns_dtype(dtype):
        return 'DATETIME'
    elif is_bool_dtype(dtype):
        return 'BOOLEAN'
    elif is_string_dtype(dtype):
        return 'STRING'
    elif is_numeric_dtype(dtype):
        return 'NUMBER'
    else:
        return 'UNKNOWN'
