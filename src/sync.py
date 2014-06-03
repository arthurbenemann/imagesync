import os.path
import georeference 
import imageParser 
import logParser 


def sync(logPath,imagesPath, offset):
    log = open(logPath, 'r')
        
    images = imageParser.findImages(imagesPath)
    locations = logParser.parseLog(log)
                
    if offset is None:
        return georeference.calcOffset(images, locations)   
    
    georef = georeference.geoReference(images, locations, offset)
    
    output = open(imagesPath+'/georeference.txt','w')
    output.write('Name Lng Lat Alt Yaw Pitch Roll\n') 
    for ref in georef:
        output.write(str(ref).replace('[', '').replace(']', '').replace(',', '').replace("'", '').replace(' ', '\t')+'\n')
            
    output.flush()
    #print('Sync: ' + log.name)
    #print('Finished: %d locations, %d images, %d matches (using offset of %1.1f)' % (len(locations), len(images),len(georef),offset))