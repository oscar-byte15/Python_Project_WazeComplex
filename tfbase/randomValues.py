from latLongIds import *

def getGraphSize(graph):
    return len(graph)

def perlinNoise():
    xpix = 10
    ypix = getGraphSize(map)
    noise = PerlinNoise(octaves=5, seed=1)
    pic = [[noise([i/xpix, j/ypix]) for j in range(xpix)] for i in range(ypix)]

    return np.array(np.array(pic)*100, dtype=int)

randValues = perlinNoise()

def sameNode(n1, n2):
    x1, y1 = n1
    x2, y2 = n2
    if (x1 == y2) and (y1 == x2):
        return True
    return False

def getListRandValues(n):
    r = random.randrange(0, n)
    
    while sum(randValues[r]) == 0:
        r = random.randrange(0, n)

    return list(randValues[r])

def getPositive(num):
    if num < 0:
        return num * -1
    else:
        return num

# agrega un valor random (generado con perlin noise) al diccionario de lat y longs
def addRandValue(dictionary):

    randv = getListRandValues(len(latlong))

    for key, value in map.items():
        l = []
        for u in value:
            if sameNode(key, u):
                u += (0,)      
                l.append(u)
                continue

            if len(randv) > 0:
                u += (getPositive(randv.pop()),)
            else:
                randv = getListRandValues(len(latlong))
                u += (getPositive(randv.pop()),)
            l.append(u)
        dictionary[key] = l
    return dictionary
    
map2 = addRandValue({})