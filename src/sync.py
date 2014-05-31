import os.path

from imageParser import findImages
from logParser import parseLog
from georeference import calcOffset, geoReference


def sync(logPath, offset):
    log = open(logPath, 'r')
    path = os.path.dirname(log.name)
    
    images = findImages(path)
    locations = parseLog(log)
                
    if offset is None:
        calcOffset(images, locations)
        return    
    
    georef = geoReference(images, locations, offset)
    
    output = open(path+'/georeference.txt','w')
    output.write('Name Lng Lat Alt Yaw Pitch Roll\n') 
    for ref in georef:
        output.write(str(ref).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', '\t')+'\n')
            
    
    print('Sync: ' + log.name)
    print('Finished: %d locations, %d images, %d matches (using offset of %1.1f)' % (len(locations), len(images),len(georef),offset))