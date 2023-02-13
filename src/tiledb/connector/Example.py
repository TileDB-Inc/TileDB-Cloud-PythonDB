from connect import connect

if __name__ == '__main__':
    connection = connect(token ="TOKEN")
    cursor = connection.cursor()
    cursor.execute("SELECT * from `tiledb://TileDB-Inc/quickstart_dense`")
    # results = cursor.fetchall()
    # for row in results:
    #     print(row)
    row = cursor.fetchone()
    while row:
        print(row)
        row = cursor.fetchone()

    print(cursor.description())
