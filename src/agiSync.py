import PhotoScan
import sync
import os
import sys
import agisoftUtil
 
def askUserForLogFile():
    return PhotoScan.app.getOpenFileName('ArduPilot Flight log (.log)')
def askUserForOffset(offset = 0):
    return PhotoScan.app.getFloat('Offset value in seconds',offset)

def estimateOffset():
    logPath = agisoftUtil.getLogPath()
    imagesPath = agisoftUtil.getImagesPath()
    minOff,maxOff = sync.sync(logPath,imagesPath,None)
    print('\nMin: '+ str(minOff)+'\tMax: '+str(maxOff))
    
    
    minOff = PhotoScan.app.getFloat('Min. offset (s):',minOff)
    maxOff = PhotoScan.app.getFloat('Max. offset (s):',maxOff)
        
    interval = maxOff - minOff
    step = interval/PhotoScan.app.getInt('Get number of steps for the offset search (%2.0fs interval)'%(int(interval)),50)
    
    # Run iteration
    offset = minOff
    while offset<maxOff:
        sync.sync(logPath, imagesPath,offset)    
        agisoftUtil.applyGeoreference(imagesPath)    
        error = agisoftUtil.getTotalError()
        print('offset:{:8.1f}s \terror: {:8.2f}m'.format(offset,error)+' - '+'|'*int(error/2))
        PhotoScan.app.update()
        offset = offset +step;
    
    
def syncImages():
    logPath = agisoftUtil.getLogPath()
    imagesPath = agisoftUtil.getImagesPath()
    sync.sync(logPath, imagesPath,askUserForOffset())    
    agisoftUtil.applyGeoreference(imagesPath)

# get argument list using sys module
PhotoScan.app.addMenuItem('EstimateOffset',estimateOffset, shortcut = 'e')
PhotoScan.app.addMenuItem('SyncImages',syncImages, shortcut = 's')


