import os
from tiledb.connector import TileDBConnection


def test_quickstart_sparse():
    tkn = os.environ.get('DB_TOKEN')
    connection = TileDBConnection(token=tkn)
    cursor = connection.cursor()
    cursor.execute("SELECT * from `tiledb://TileDB-Inc/nyc_tlc_yellow_trip_data_2019` limit 10")
    results = cursor.fetchall()
    for row in results:
        print(row)
    # do something with my_var
