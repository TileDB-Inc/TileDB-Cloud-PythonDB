import os

from tiledb.connector import TileDBConnection

tkn = os.environ.get('DB_TOKEN')
connection = TileDBConnection(token=tkn)
cursor = connection.cursor()
cursor.execute("SELECT * from `tiledb://TileDB-Inc/quickstart_dense`")
correctData = [
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

correctDescription = [
    ('rows', 'NUMBER'),
    ('cols', 'NUMBER'),
    ('a', 'NUMBER'),
]


def test_fetchall():
    cursor.reset()
    results = cursor.fetchall()
    assert results == correctData


def test_fetchmany():
    cursor.reset()
    results = cursor.fetchmany(5)
    assert results == correctData[:5]
    results = cursor.fetchmany(2)
    assert results == correctData[5:7]


def test_fetchone():
    cursor.reset()
    results = cursor.fetchone()
    assert results == correctData[:1]


def test_fetchmix():
    cursor.reset()
    results = cursor.fetchmany(5)
    assert results == correctData[:5]
    results = cursor.fetchone()
    assert results == correctData[5:6]
    results = cursor.fetchall()
    assert results == correctData[6:]


def test_description():
    cursor.reset()
    desc = cursor.description()
    assert desc == correctDescription
