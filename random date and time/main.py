import random
import time
def getRandomDate(startDate, endDate):
    print("print random date beetween", startDate, "and", endDate)
    randomGenerator=random.random()
    dateFormat='%m/%d/%y'
    starTime=time.mktime(time.strptime(startDate,dateFormat))
    endTime=time.mktime(time.strptime(endDate, dateFormat))
    
    randomTime= startTime + randomGenerator*(endTime - startTime)
    randomDate=time.strfttime(dateFormat, time.localTime(randomTime))
    return randomDate
print("random date =", getRandomDate("1/1/2010"),("12/12/2023"))
