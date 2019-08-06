import sqlite3
from orbitModeling import planet

#This function returns a list of planet objects populated from whatever is in the database


def load_planet_database():
    # database file connection & setup
    database = sqlite3.connect("Database")
    cursor = database.cursor()


    planet_list = []


    cursor.execute("""SELECT * FROM PLANET""")
    query_result = cursor.fetchall()
    for i in query_result:
        temp = planet(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7],i[8],i[9])
        planet_list.append(temp)

    #function is READ-ONLY so no changes are made
    database.close()
    return planet_list
