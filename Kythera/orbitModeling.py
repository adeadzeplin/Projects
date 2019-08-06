'''
--------------------------------------------------------------------------------
Orbit Modeling Prototype:
--------------------------------------------------------------------------------
How to use this file for the GUI test:
- Import the file by adding "import orbit_modeling_v2" to the header
- Call "Jacob(time)" in a loop and use the outputted list for the GUI
- Refer to the function's documentation for more detail
--------------------------------------------------------------------------------
'''


import math
import datetime

class body:
    def __init__(self):
        mass = 0
        xPos = 0
        yPos = 0
        print("Celstial body added")

class star(body):
    def __init__(self, m):
        self.mass = m
        self.xPos = 0
        self.yPos = 0
        print("Star added")

class planet(body):
    def __init__(self, name, mass, semiMajorAxis, eccentricity, periapsis, timeToOrbit, maxInclination, longitudeAscendingNode, longitudePerihelion, baseAngle): #should also add some starting date to base the planet off of (Use NASA queries)
        #changing variables
        self.distance = periapsis
        self.xPos = 0
        self.yPos = 0
        self.zPos = 0
        self.angle = baseAngle
        self.inclination = 0
        #constant properties: (#) means used for calculations
        self.name = name
        self.mass = mass
        self.semiMajorAxis = semiMajorAxis #
        self.eccentricity = eccentricity #
        self.timeToOrbit = timeToOrbit #
        self.maxInclination = maxInclination #
        self.longitudeAscendingNode = longitudeAscendingNode #
        self.longitudePerihelion = longitudePerihelion #
        self.baseDate = datetime.date(2019, 1, 1) # this is the base date for the base angle (used to base the body on real world data)
        self.baseAngle = baseAngle # this is the base angle at said base time
        todayDate = datetime.date.today()
        self.simulate_orbit_date(todayDate.month, todayDate.day, todayDate.year, True)
        print("Planet added")

    def simulate_orbit(self, t): # Function that will determine the position of the planet with an stable increment t variable
        '''
        Function that simulates the orbit of the planet incrementally.

        Inputs:
            - The increment 't' in day units
        Outputs :
            - None, but the angle and coordinates of the celestial body are updated
        Uses :
            Can be used in a loop to continuously update the position of the body
        '''

        self.angle += (t * 2 * math.pi) / self.timeToOrbit# assuming the periapsis is the base start point
        if self.angle > 2 * math.pi: #correects the angle to be less than a full rotation
            self.angle -= 2 * math.pi
        self.inclination = self.maxInclination * math.sin(self.angle - self.longitudeAscendingNode) # gets the current inclination

        self.distance = (self.semiMajorAxis * (1 - math.pow(self.eccentricity, 2))) / (1 + self.eccentricity * math.cos(self.angle - self.longitudePerihelion)) # gets the distance from the sun
        self.xPos = math.cos(self.angle) * math.cos(self.inclination) * self.distance
        self.yPos = math.sin(self.angle) * math.cos(self.inclination) * self.distance
        self.zPos = math.sin(self.inclination)

    def simulate_orbit_date(self, month, day, year, AD):
        newDate = datetime.date(year, month, day)
        if AD:
            t = (newDate - self.baseDate).days
        else:
            t = - ((self.baseDate - datetime.date(1, 1, 1)).days + newDate.year * 365 - (newDate - datetime.date(1, 1, 1)).days)
        self.angle = self.baseAngle
        self.simulate_orbit(t)


class satellite(body): # STILL NEEDS MODIFICATIONS
    def __init__(self, name, mass, semiMajorAxis, eccentricity, periapsis, timeToOrbit, maxInclination, longitudeAscendingNode, longitudePerihelion, baseAngle, host): #should also add some starting date to base the planet off of (Use NASA queries)
        #changing variables
        self.distance = periapsis
        self.xPos = 0
        self.yPos = 0
        self.zPos = 0
        self.angle = baseAngle
        self.inclination = 0
        #constant properties: (#) means used for calculations
        self.name = name
        self.mass = mass
        self.semiMajorAxis = semiMajorAxis #
        self.eccentricity = eccentricity #
        self.timeToOrbit = timeToOrbit #
        self.maxInclination = maxInclination #
        self.longitudeAscendingNode = longitudeAscendingNode #
        self.longitudePerihelion = longitudePerihelion #
        self.baseDate = datetime.date(2019, 1, 1) # this is the base date for the base angle (used to base the body on real world data)
        self.baseAngle = baseAngle # this is the base angle at said base time
        self.host = host # the planet hosting the satellite
        todayDate = datetime.date.today()
        #self.simulate_orbit_date(todayDate.month, todayDate.day, todayDate.year, True, host)
        print("Planet added")

    def simulate_orbit(self, t, host): # Function that will determine the position of the planet with an stable increment t variable
        '''
        Function that simulates the orbit of the satellite incrementally.

        Inputs:
            - The increment 't' in day units
        Outputs :
            - None, but the angle and coordinates of the celestial body are updated
        Uses :
            Can be used in a loop to continuously update the position of the body
        '''

        self.angle += (t * 2 * math.pi) / self.timeToOrbit# assuming the periapsis is the base start point
        if self.angle > 2 * math.pi: #correects the angle to be less than a full rotation
            self.angle -= 2 * math.pi
        self.inclination = self.maxInclination * math.sin(self.angle - self.longitudeAscendingNode) # gets the current inclination

        self.distance = (self.semiMajorAxis * (1 - math.pow(self.eccentricity, 2))) / (1 + self.eccentricity * math.cos(self.angle - self.longitudePerihelion)) * 30 # gets the distance from the sun (the * 30 fixes a bug in the main program)
        self.xPos = math.cos(self.angle) * math.cos(self.inclination) * self.distance + host.xPos
        self.yPos = math.sin(self.angle) * math.cos(self.inclination) * self.distance + host.yPos
        self.zPos = math.sin(self.inclination) + host.zPos

    def simulate_orbit_date(self, month, day, year, AD, host):
        newDate = datetime.date(year, month, day)
        if AD:
            t = (newDate - self.baseDate).days
        else:
            t = - ((self.baseDate - datetime.date(1, 1, 1)).days + newDate.year * 365 - (newDate - datetime.date(1, 1, 1)).days)
        self.angle = self.baseAngle
        print(t)
        self.simulate_orbit(t, host)
