from mainGraph import *
from perlin_noise import PerlinNoise
import matplotlib.pyplot as plt
import numpy as np
import random

def formatearLatitudeorLongitude(input):
    separar = input
    separar = separar.split(".");

    union= separar[0]+"."+separar[1]+separar[2];
    variable_float = float(union)

    return variable_float

# devuelve solo la latitud y longitud, no el id
def getOnlyLatLong(key):
    return (latlong[key][0], latlong[key][1])

def getInterId(key):
    return latlong[key][2]

def createLatLongDictionary(latlong):
    with open("..\datos\Latitud y Longitud de calles.csv") as file: 
        reader = csv.reader(file)      
        # ignora el header (la 1era fila del csv)
        next(reader)
        # se le asignará un id a cada vértice
        id = 0
        for row in reader:
            # busco el id de la calle en mi diccionario de calles 
            intersection = streetExists(row[0]), streetExists(row[1])
            if intersection in map:
                latlong[intersection] = formatearLatitudeorLongitude(row[2]), formatearLatitudeorLongitude(row[3]), id
                id += 1
    return latlong
     
latlong = createLatLongDictionary({})