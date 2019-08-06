import sqlite3
from orbitModeling import star

#This function returns a star object populated from whatever is in the database


def load_star_database():
    # database file connection & setup
    database = sqlite3.connect("Database")
    cursor = database.cursor()

    cursor.execute("""SELECT * FROM STAR""")
    query_result = cursor.fetchall()
    temp = 0
    for i in query_result:
        temp = star(i[0])
        #print(i[0])
    #function is READ-ONLY so no changes are made
    database.close()
    return temp
