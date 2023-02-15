import os

from tiledb.connector import TileDBConnection

tkn = os.environ.get('DB_TOKEN')
connection = TileDBConnection(token=tkn)
cursor = connection.cursor()
cursor.execute("SELECT * from `tiledb://TileDB-Inc/quickstart_dense`")
correct = [
    {'rows': 1, 'cols': 1, 'a': 1},
    {'rows': 1, 'cols': 2, 'a': 2},
    {'rows': 1, 'cols': 3, 'a': 3},
    {'rows': 1, 'cols': 4, 'a': 4},
    {'rows': 2, 'cols': 1, 'a': 5},
    {'rows': 2, 'cols': 2, 'a': 6},
    {'rows': 2, 'cols': 3, 'a': 7},
    {'rows': 2, 'cols': 4, 'a': 8},
    {'rows': 3, 'cols': 1, 'a': 9},
    {'rows': 3, 'cols': 2, 'a': 10},
    {'rows': 3, 'cols': 3, 'a': 11},
    {'rows': 3, 'cols': 4, 'a': 12},
    {'rows': 4, 'cols': 1, 'a': 13},
    {'rows': 4, 'cols': 2, 'a': 14},
    {'rows': 4, 'cols': 3, 'a': 15},
    {'rows': 4, 'cols': 4, 'a': 16},
]


def test_fetchall():
    results = cursor.fetchall()
    assert results == correct