import json
import visualizations 
import shortestPath

def graph():
    Loc = visualizations.coordinates
    G = visualizations.graph

    response = {"loc": Loc, "g": G}

    return json.dumps(response)

def paths():
    
    caminos = shortestPath.paths

    if len(caminos) == 3:
        bestPath = caminos[0]
        p2 = caminos[1]
        p3 = caminos[2]
    elif len(caminos) == 2:
        bestPath = caminos[0]
        p2 = caminos[1]
        p3 = []
    elif len(caminos) == 1:
        bestPath = caminos[0]
        p2 = []
        p3 = []
    else:
        bestPath = []
        p2 = []
        p3 = []

    bestpath = bestPath
    path1 = p2
    path2 = p3

    response = {"bestpath": bestpath, "path1": path1, "path2": path2}

    return json.dumps(response)