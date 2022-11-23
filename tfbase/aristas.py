from randomValues import *
from datetime import datetime
from math import radians, cos, sin, asin, sqrt

def askTime():
    time = int(input("Digite la hora en formato de 24hrs: "));
    if time not in range(0, 24):
        time = askTime() 
    return time

def getlongitude(n1, n2):
    lon1,lat1=n1
    lon2,lat2=n2
    if lon1 == lat2 and lon2 == lat1:
      longitude = 0
    else:
      lon1 = radians(lon1)
      lon2 = radians(lon2)
      lat1 = radians(lat1)
      lat2 = radians(lat2)
      dlon = lon2 - lon1
      dlat = lat2 - lat1
      a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
      c = 2 * asin(sqrt(a)) 
      r = 6371
      longitude = c * r
    
    return longitude

def point_percent(time):
    percent = 0
    # de 0am - 4am
    if time in range(0, 5):
        percent = 0.1
    
    # de 5am - 8am
    if time in range(5, 9):
        percent = 0.9

    # de 9am - 16pm
    if time in range(9, 18):
        percent = 0.5

    # de 18pm - 20pm
    if time in range(18, 21):
        percent = 1.3

    # de 21pm - 23pm
    if time in range(21, 23):
        percent = 0.3

    return percent

def getFactor(time, val): 
    time_points = [0, 1, 1, 1, 2, 3, 15, 19, 17, 14, 13, 10, 10, 11, 12, 13, 14, 16, 17, 20, 19, 15, 4, 2]

    percent = point_percent(time)
    factor = int((val * percent) + time_points[time])

    if factor > 50:
        factor = 50

    return factor

def calculateWeight(n1, n2, time, val):
    
    longitude = getlongitude(n1, n2) * 100
    factor = getFactor(time, val)
    
    weight = longitude * factor

    if longitude > 0:
        weight = round(factor + longitude, 2)
    
    if (weight > 100):
        return 99
    else:
        return int(weight)

def updateGraph():
    time = askTime()

    # map con pesos
    mapW = {}
    for key in map2:
        if key in latlong:
            k = getInterId(key)
            mapW[k] = []
        else:
            continue
        for arista in map2[key]:
            edge = (arista[0], arista[1])
            if edge in latlong:
                weight = calculateWeight(getOnlyLatLong(key), getOnlyLatLong(edge), time, arista[2])
                # [intersección, peso]
                if weight == 0: continue
                mapW[k].append((getInterId(edge), weight))
        mapW[k]
    return mapW

def getMaxKey(G):
    return max(G, key = G.get)

mapW = updateGraph()