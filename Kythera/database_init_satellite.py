import sqlite3

def database_init_satellite():
    # database file connection
    database = sqlite3.connect("Database")

    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    # This unit will drop the planet table
    sql_command = """
        DROP TABLE IF EXISTS SATELLITE;"""
    cursor.execute(sql_command)

    # SQL command to create a table in the database
    sql_command = """CREATE TABLE IF NOT EXISTS SATELLITE (
        Name   TEXT 	PRIMARY KEY 	NOT NULL,
        Mass                    REAL,
        semiMajorAxis           REAL,
        eccentricity            REAL,
        periapsis               REAL,
        timeToOrbit             REAL,
        maxInclination          REAL,
        longitudeAscendingNode  REAL,
        longitudePerihelion     REAL,
        baseAngle               REAL,
        host                    TEXT
        )
        ;"""

    # execute the statement1

    cursor.execute(sql_command)

    cursor.execute("""
        INSERT INTO SATELLITE VALUES('Moon',73476730900000000000000, 384400, 0.0549, 363300,27.3217, 0.08979719002, 2.024581932, 1.480032551, 3.881092281, 'Earth'   )
        """)

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    database.commit()
    # close the connection
    database.close()
