from aristas import *
import heapq as hq
import math

def getMin(a):
    min = a[0][1]
    index = 0
    for i, c in enumerate(a):
        if c[1] < min:
            min = c[1]
            index = i
    return a.pop(index)

def definePath(d, path):
    g = []
    g.append(d)

    while path[d] != -1:
        destination = path[d]
        g.insert(0, destination)
        d = destination
    return g

# uses dijkstra
def findShortestPath(graph, s, ignore):
    n = len(graph)
    path = [-1] * n
    visited = [False] * n
    visited[ignore] = True
    
    cost = [math.inf] * n
    cost[s] = 0

    priorityq = [(s, 0)]

    while priorityq:
        # vértice, peso
        u, g = getMin(priorityq)
        if not visited[u]:
            visited[u] = True
        for v, w in graph[u]:
            if not visited[v]:
                weight = g + w
                if weight < cost[v]:
                    cost[v] = weight
                    path[v] = u
                    priorityq.append((v, weight))
    return path, cost

def getDirections(s, d, graph):
    neighbours = graph[s]
    paths = []
    costs = []

    for n in neighbours:
        path, cost = findShortestPath(mapW, n[0], s)
        path = definePath(d, path)
        path.insert(0, s)
        paths.append(path)
        costs.append(cost[d])
    return paths, costs

def getBestPaths(paths, costs):
    bestCosts = [(i, x) for i, x in enumerate(costs)]
    bestCosts.sort(key=lambda x:x[1])
    
    n = len(bestCosts)
    if n > 3:
        bestCosts = [bestCosts[i] for i in range(3)]
    else:
        bestCosts = [bestCosts[i] for i in range(n)]

    bestPaths = [paths[c[0]] for c in bestCosts]
    
    return bestPaths

# si el costo es inf, significa que no existe un camino
def aPathExists(paths, costs):
    for i, cost in enumerate(costs):
        if cost == float('Inf'):
            paths[i] = []

def deleteInvalidPaths(paths, costs):
    for i, p in enumerate(paths):
        if p == []:
            paths.pop(i)
            costs.pop(i)

# desde donde quiero empezar a buscar
source = 15
# a donde quiero llegar
destination = 30
paths, costs = getDirections(source, destination, mapW)

# elimina caminos inválidos (no existentes)
aPathExists(paths, costs)
deleteInvalidPaths(paths, costs)

# retorna los mejores caminos
paths = getBestPaths(paths, costs)
costs.sort()