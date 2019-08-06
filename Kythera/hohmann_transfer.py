import orbitModeling as orb
import math
import datetime

def orbital_transfer(launchPlanet, landPlanet): # function to determine the perfect time to efficiently launch a projectile to other orbits
    # The goal is to form a rough ellipse passing through both orbits, then use Kepler's principles to determine the rest

    if launchPlanet == landPlanet:
        return("These are the same planets :>")
    ###################################################################
    # START BY SIMULATING ALL THE PLANETS IN THE SYSTEM AT TODAY'S TIME
    ###################################################################

    a = (launchPlanet.semiMajorAxis + landPlanet.semiMajorAxis) / (2 * 149598000) # gets the the semimajor axis of the transfer ellipse. This value is in AU
    print(a)
    T = math.sqrt(math.pow(a, 3)) # from Kepler's a^3 = T^2, where a is the semimajor axis, and T is the orbital period
    travelTime = T / 2 # T includes the two way period (full rotation), this is a variable for a one way launch. This time is in years

    # Now we find what position the landing planet should be in at the time of launch
    angleDeviation = math.pi - 2 * math.pi * (travelTime / (landPlanet.timeToOrbit / 365)) # this is the angle difference between the two planets
    print(angleDeviation * 180 / math.pi)
    # Now we run the simulation until the angleDeviation is met
    increment = 0.5
    time = increment; # time in days
    while ((landPlanet.angle - launchPlanet.angle) < (angleDeviation - math.pi / 180)) or ((landPlanet.angle - launchPlanet.angle) > (angleDeviation + math.pi / 180)):
        launchPlanet.simulate_orbit(increment)
        landPlanet.simulate_orbit(increment)
        # print("earth angle:", launchPlanet.angle, " |  mars angle:", landPlanet.angle) for debugging
        time += increment

    ###################################################################
    # ADD A STATEMENT THAT SIMULATES THE OTHER PLANETS AT THAT TIME HERE
    ###################################################################

    nearestLaunchDate = datetime.date.today() + datetime.timedelta(days = math.floor(time))
    print(nearestLaunchDate)

    return (landPlanet.name + " should be at an angle of " + str(angleDeviation * 180 / math.pi) + " degrees from " + launchPlanet.name + "\nThe nearest date this occurs is " + str(nearestLaunchDate.month) + "/" + str(nearestLaunchDate.day) + "/" + str(nearestLaunchDate.year))

# testing
#Sun = orb.star(1.989 * math.pow(10, 30))
#Earth = orb.planet('Earth', 5.972 * math.pow(10, 24), 149598262.00, 0.017, 147098291.00, 365.25636, 0, -0.196535244, 1.796767421, 1.749518042)
#Mars = orb.planet('Mars', 5.972 * math.pow(10, 24), 227943823.5, 0.093, 206655215, 687.0106875, 0.032288591, 0.865308761, 5.865019079, 0.7309438907)
#print((Earth.angle - Mars.angle) * 180 / math.pi)
#orbital_transfer(Earth, Mars)
