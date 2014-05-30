import os.path

from imageParser import findImages
from logParser import parseLog
from georeference import calcOffset, geoReference


def main():
    log = open('/home/arthur/bigMap/images/102___05/data.log', 'r')
    path = os.path.dirname(log.name)
    print('\n### SYNC ' + log.name)
    
    images = findImages(path)
    locations = parseLog(log)
                
    offset = calcOffset(images, locations)    
    #offset = 0.0
    georef = geoReference(images, locations, offset)
    
    for ref in georef:
        print(ref)
            
    print('\nFinished: %d locations, %d images, %d matches' % (len(locations), len(images),len(georef))) 
    
if __name__ == "__main__":
    main()          
