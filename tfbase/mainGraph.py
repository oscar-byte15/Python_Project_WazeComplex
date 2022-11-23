from streetsIntersections import *

def createKeys(graph):
    intersectionsIDs = {}

    for i in range(len(graph)):
        for street in graph[i]:
            # si las keys aún no han sido creadas, las agrega al diccionario
            if (i, street) not in intersectionsIDs and street != -1:
                intersectionsIDs[(i, street)] = []
    return intersectionsIDs

def addIntersections(graph, i, j):  
    street = graph[i][j]

    if street != -1:
        # agrego la intersección már próxima hacia la izquierda
        if j > 0 and graph[i][j - 1] != -1:
            tup = (i, graph[i][j - 1])
            map[(i, street)].append(tup)

        # agrego la intersección már próxima hacia la derecha
        if j < len(graph[i]) - 1 and graph[i][j + 1] != -1:
            tup = (i, graph[i][j + 1])
            map[(i, street)].append(tup)

def addIntersectionsReversed(graph, i, j):  
    street = graph[i][j]

    # ahora voy al reverso de la lista
    if i != -1 and street != -1:
        if (street < len(graph)) and (i in graph[street]):
            tup = (street, i)
            map[(i, street)].append(tup)
            
            k = graph[street].index(i) # k = 2

            if k > 0 and graph[street][k - 1] != -1:
                tup = (street, graph[street][k - 1])
                map[(i, street)].append(tup)
        
            if k < len(graph[street]) - 1 and graph[street][k + 1] != -1:
                tup = (street, graph[street][k + 1])
                map[(i, street)].append(tup)

def joinIntersections(graph):
    n = len(graph)
    for i in range(n):        
        for j in range(len(graph[i])):
            addIntersections(graph, i, j)
            addIntersectionsReversed(graph, i, j)

def totalNodes(graph):
    total = 0 
    for key, value in graph.items():
        total += len(value)
    return total

# grafo principal
map = createKeys(intersectionsAdList)
joinIntersections(intersectionsAdList)