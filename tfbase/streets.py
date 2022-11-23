import csv

def addKey_Values(dictionary, key, value):
    dictionary[key] = value

def printDictionary(dictionary):
    for k, v in dictionary.items():
        print(f"{k}: {v}")

def cargarDatos(dictionary):
    with open("..\datos\Calles de San Martín de Porres.csv") as file: 
        reader = csv.reader(file)
        
        for id, row in enumerate(reader):
            addKey_Values(dictionary, row[0].lower(), id)

def createStreetsDictionary():   
    streets = {}
    cargarDatos(streets)
    return streets

streetsDictionary = createStreetsDictionary()