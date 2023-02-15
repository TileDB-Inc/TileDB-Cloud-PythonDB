<a href="https://tiledb.com/"><img src="https://github.com/TileDB-Inc/TileDB/raw/dev/doc/source/_static/tiledb-logo_color_no_margin_@4x.png" alt="TileDB logo" width="400"></a>

# TileDB-Cloud-PythonDB

This package features the TileDB-Cloud-Python connector, which aligns with the Python DB API 2.0 specification. It offers a convenient way for Python developers to connect to TileDB-Cloud and perform all necessary operations. 
This can also be seen as an alternative to a JDBC or ODBC driver.

## Installation

```bash
pip install .
```

## Usage

```python
connection = TileDBConnection(token=<API_TOKEN>)
cursor = connection.cursor()
cursor.execute("SELECT * from `tiledb://TileDB-Inc/quickstart_dense`")

row = cursor.fetchone()
while row:
    print(row)
    row = cursor.fetchone()

print(cursor.description())

```
