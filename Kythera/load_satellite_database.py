import sqlite3
from orbitModeling import satellite


def load_satellite_database():
    # database file connection & setup
    database = sqlite3.connect("Database")
    cursor = database.cursor()

    satellite_list = []

    cursor.execute("""SELECT * FROM SATELLITE""")
    query_result = cursor.fetchall()
    for i in query_result:
        temp = satellite(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9],i[10])
        satellite_list.append(temp)

    # function is READ-ONLY so no changes are made
    database.close()
    return satellite_list
