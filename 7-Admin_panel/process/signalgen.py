import random
import datetime

def randomDateValueJson(maxValue, minYear, maxYear, size) :
    sig = [random.randint(0, maxValue) for i in range(size)]
    dates = [datetime.date(random.randint(minYear, maxYear),
                    random.randint(1,12),
                    random.randint(1,25)) for i in range(size)]
    dates.sort()
    json = "[";
    # Ajoute a json une ligne de type : `["date":2018-11-04,"value":39],`
    for i in range(size):
        json += "{\"date\": \"" + str(dates[i]) + "\""
        json += ",\"value\":" + str(sig[i]) + "}"
        if (i < size - 1) :
            json += ","
        json += "\n"
    return json + "]"

print(randomDateValueJson(60,2015,2018,100))
userByTime = "userByTime = " randomDateValueJson(60,2015,2018,100) + ";"
