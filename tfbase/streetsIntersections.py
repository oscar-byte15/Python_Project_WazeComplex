from streets import *

def printAdList(graph):
    for i, intersection in enumerate(graph):
        print(i, intersection)
    
    print(f"Cantidad de vértices = {len(graph)}")

def streetExists(streetName):
    if streetName in streetsDictionary:
        id = streetsDictionary[streetName]
    else:
        id = -1
    return id

def createAdjacencyList(adjacencyList):
    with open('..\datos\Calles de San Martín de Porres.csv') as file: 
        reader = csv.reader(file)
        for row in reader:  
            intersections = []
            for i in range(len(row)):
                if i != 0:
                    intersections.append(streetExists(row[i].lower()))
            adjacencyList.append(intersections)
    return adjacencyList

intersectionsAdList = createAdjacencyList([])