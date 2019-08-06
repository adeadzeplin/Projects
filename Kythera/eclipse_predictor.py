import datetime
import sqlite3

# connect to the database


def datetime_to_sql(date): #function used to convert a datetime object to a readable sql datetime statement
    sqlCommand = str(date.year) + str(date.month) + str(date.day) + ' ' + str(date.hour) + ':00:00'
    return sqlCommand

def sql_to_datetime(sqlResult): #funciton used to convert an sql datetime statemnt to a datetime object
    year = int(sqlResult[0] + sqlResult[1] + sqlResult[2] + sqlResult[3])
    month = int(sqlResult[4] + sqlResult[5])
    day = int(sqlResult[6] + sqlResult[7])
    if len(sqlResult) == 16: #fixes a small bug where the date is a shorter string
        hour = int(sqlResult[9])
    else:
        hour = int(sqlResult[9:-6])

    equivalentDate = datetime.datetime(year = year, month = month, day = day, hour = hour)
    return equivalentDate

def eclipse_predictor(year):
    conn = sqlite3.connect('Database')
    c = conn.cursor()

    #sets the starting frame
    startOfYear = datetime.datetime(year = year, month = 1, day = 1, hour = 0)
    endOfYear = datetime.datetime(year = year, month = 12, day = 31, hour = 23)

    #sets the database's frame
    DatabaseStart = datetime.datetime(year = 2001, month = 1, day = 1, hour = 0)
    DatabaseEnd = datetime.datetime(year = 2019, month = 1, day = 11, hour = 8)

    #sets the increment used to shift the starting frame
    offset = datetime.timedelta(days = 6585, hours = 8) # 18 years, 11 days, 8 hours
    times = 0 # variable that keeps track of how many times the frame is shifted

    # shift the starting frame until it is within the database's frame
    while startOfYear > DatabaseEnd or endOfYear < DatabaseStart:
        if startOfYear > DatabaseEnd:
            startOfYear -= offset
            endOfYear -= offset
            times +=1
        else:
            startOfYear += offset
            endOfYear += offset
            times -= 1

    sqlStartOfYear = datetime_to_sql(startOfYear)
    sqlEndOfYear = datetime_to_sql(endOfYear)

    #get all the results in that time frame from the database
    c.execute("Select * From Eclipse Where Date between '" + sqlStartOfYear +"' and '" + sqlEndOfYear + "'")
    queryResult = c.fetchall()
    #print("Select * From Eclipse Where Date between '" + sqlStartOfYear +"' and '" + sqlEndOfYear + "'")
    finalResult = []
    for result in queryResult:
        newResult = []
        print(result)
        newDateTime = sql_to_datetime(result[0]) + times * offset
        newResult.append(newDateTime)
        newResult.append(result[1])
        result = newResult
        finalResult.append("-> "+ result[1] + " eclipse on " + str(result[0].month) + "-" + str(result[0].day) + "-" + str(result[0].year) + " at " + str(result[0].hour))
        print(result[1], "eclipse on", result[0])

    #returns the result in the form of a 2D array where the datetime object is the first index and the eclipse type is the second index
    return finalResult
