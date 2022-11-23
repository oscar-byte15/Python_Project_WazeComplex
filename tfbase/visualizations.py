from shortestPath import *

def latlongGraph(dictionary):
    n = len(dictionary) + 10
    latlongs = [()] * n
    
    for key, value in dictionary.items():
        latlongs[dictionary[key][2]] = dictionary[key][0] * -1, dictionary[key][1] * -1

    return latlongs

def getGraph(graph):
    n = len(graph) + 10
    G = [[(510, 0)]] * n

    for key, value in graph.items():
        G[key] = value
    return G

# loc, G
coordinates = latlongGraph(latlong)
graph = getGraph(mapW)