# This file includes the datatype mapping from pandas to the types required by the Python DB API 2.0
import pyarrow as pa


def getDBType(dtype):
    if pa.types.is_timestamp(dtype):
        return 'DATETIME'
    elif pa.types.is_boolean(dtype):
        return 'BOOLEAN'
    elif pa.types.is_string(dtype):
        return 'STRING'
    elif pa.types.is_integer(dtype) or pa.types.is_floating(dtype):
        return 'NUMBER'
    else:
        return 'UNKNOWN'
