import random
import datetime

def moy(cur, last, before):
    r = (cur + last + before) // 3
    return r

def randomDateValueJson(maxValue, minYear, maxYear, size) :
    sig = [random.randint(0, maxValue) for i in range(size)]
    sigm = [sig[i] if i <= 1 else moy(sig[i], sig[i-1], sig[i-2]) for i in range(size)]
    dates = [datetime.date(random.randint(minYear, maxYear),
                    random.randint(1,12),
                    random.randint(1,25)) for i in range(size)]
    dates.sort()
    json = "[";
    # Ajoute a json une ligne de type : `["date":2018-11-04,"value":39],`
    for i in range(size):
        json += "{\"date\": \"" + str(dates[i]) + "\""
        json += ",\"value\":" + str(sigm[i]) + "}"
        if (i < size - 1) :
            json += ","
        json += "\n"
    return json + "]"

print(randomDateValueJson(60,2015,2018,100))
userByTime = "userByTime = " + randomDateValueJson(60,2015,2018,100) + ";"
