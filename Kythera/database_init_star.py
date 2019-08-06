import sqlite3

# this is the database initialization file
# run this file if you want to reset/initialize the Star database

def database_init_star():
    # database file connection
    database = sqlite3.connect("Database")
    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    #This unit will drop the Star Table
    sql_command = """
    DROP TABLE IF EXISTS STAR;"""
    cursor.execute(sql_command)

    sql_command = """CREATE TABLE IF NOT EXISTS STAR (  
    Name 		    TEXT 	PRIMARY KEY 	NOT NULL,
    Mass            REAL,
    X_pos           REAL,
    Y_pos           REAL
    )
    ;"""
    cursor.execute(sql_command)

    cursor.execute("""
        INSERT INTO STAR VALUES('Sun', 1.989e+30, 0, 0);
        """)

    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    database.commit()
    # close the connection
    database.close()
