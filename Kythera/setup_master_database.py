from database_init_planets import database_init_planets
from database_init_star import database_init_star
from database_eclipses import database_init_eclipse

from database_init_satellite import database_init_satellite

# Call this function to reset the database or initialize it


def setup_master_database():
    #initialize the database tables
    database_init_star()
    database_init_planets()
    database_init_eclipse()
    database_init_satellite()


