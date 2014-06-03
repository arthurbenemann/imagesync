import time
import bisect


def geoReference(images, locations, offset):
    geoReference = []
    for image in images:
        loc = searchLocation(locations, image[1] + offset)
        if (loc is not None):
            loc.insert(0, image[0])
            geoReference.append(loc)
    
    return geoReference

def calcOffset(images, locations):
    firstLocation = locations[0][0]
    firstImage = images[0][1]
    lastLocation = locations[len(locations) - 1][0]
    lastImage = images[len(images) - 1][1]
    minOffset = float(firstLocation) - float(firstImage)
    maxOffset = float(lastLocation) - float(lastImage)
    #print ('\n### OFFSET')
    #print ('first LOG - ' + time.ctime(firstLocation) + '\tIMAGE - ' + time.ctime(firstImage))
    return (minOffset, maxOffset)

def searchLocation(locations, x):
    index = bisect.bisect_left(column(locations, 0), x)
    if index == 0:
        return None 
    if index == len(locations):
        return None
    return list(locations[index][1:])


def column(matrix, i):
    return [row[i] for row in matrix]   