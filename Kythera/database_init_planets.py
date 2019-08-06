import sqlite3

# this is the database initialization file
# run this file if you want to reset/initialize the planet database

def database_init_planets():

    # database file connection
    database = sqlite3.connect("Database")

    # cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers
    cursor = database.cursor()

    #This unit will drop the planet table
    sql_command = """
    DROP TABLE IF EXISTS PLANET;"""
    cursor.execute(sql_command)
    ######################################################################
    # SQL command to create a table in the database
    sql_command = """CREATE TABLE IF NOT EXISTS PLANET (
    Name 		    TEXT 	PRIMARY KEY 	NOT NULL,
    Mass            REAL,
    Semimajoraxis   REAL,
    Eccentricity    REAL,
    Periapsis       REAL,
    Period          REAL,
    Inclination     REAL,
    Ascending_node  REAL,
    Perihelion      REAL,
    Baseangle       REAL
    )
    ;"""

    # execute the statement1

    cursor.execute(sql_command)
    #Template for inserting into the database
    # INSERT INTO PLANET VALUES('Name', mass, semiMajorAxis, eccentricity, periapsis, period, Inclination, AscendingNode, Perihelion, baseAngle);

    cursor.execute("""INSERT INTO PLANET VALUES('Mercury',.33*1000000000000000000000000, 57909227, 0.206, 46001009, 87.95373149, 0.122173048, 0.843546774, 1.351870079, 3.936939194);""")
    cursor.execute("""INSERT INTO PLANET VALUES('Venus',  4867000000000000000000000 ,	108209475,	0.007,	107476170,224.7057127, 0.059166662, 1.338330513, 2.295683576, 2.447998809) """)
    cursor.execute("""INSERT INTO PLANET VALUES('Earth', (5.972*1000000000000000000000000),	149598262,	0.017,	147098291, 365.25636, 0, -0.196535244, 1.796767421, 1.749518042);""")
    cursor.execute("""INSERT INTO PLANET VALUES('Mars',   330100000000000000000000,	227943823.5,	0.093,	206655215,	687.0106875,	0.032288591,	0.865308761,	5.865019079,	0.7309438907    ) """)
    cursor.execute("""INSERT INTO PLANET VALUES('Jupiter',1899000000000000000000000000 ,	778340821,	0.048,	740679835,	4332.670942,	0.022863813,	1.755035901,	0.25750326,	4.307647127     ) """)
    cursor.execute("""INSERT INTO PLANET VALUES('Saturn', 568500000000000000000000000, 	1426666422,	0.056,	1349823615,	10759.72185,	0.043458698,	1.984701857,	1.613241687,	4.925668215    ) """)
    cursor.execute("""INSERT INTO PLANET VALUES('Uranus', 86820000000000000000000000 ,	2870658186,	0.046,	2734998229,	30685.1868,	0.013439035,	1.295555809,	2.983888891,	0.5572836302     ) """)
    cursor.execute("""INSERT INTO PLANET VALUES('Neptune',10240000000000000000000000 ,	4498396441,	0.01,	4459753056,	60190.59556,	0.030892328,	2.298977187,	0.784898127,	6.039362811     ) """)
    cursor.execute("""INSERT INTO PLANET VALUES('Pluto',  1471000000000000000000,	5906440628,	0.248,	4436756954,	90780.81571,	0.299323967,	1.925158728,	3.910702706,	5.07258305    ) """)
    
    # QUERY FOR ALL
    # print("ENTIRE DATA BASE\nPLANETS:")
    # cursor.execute("""SELECT * FROM PLANET""")
    # query_result = cursor.fetchall()
    #
    # for i in query_result:
    #     print(i)


    # To save the changes in the files. Never skip this.
    # If we skip this, nothing will be saved in the database.
    database.commit()
    # close the connection
    database.close()
