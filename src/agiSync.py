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
    
    offset = minOff
    step = PhotoScan.app.getFloat('Offset serach step size (s)',1)
    while offset<maxOff:
        sync.sync(logPath, imagesPath,offset)    
        agisoftUtil.applyGeoreference(imagesPath)    
        print('offset:{:8.1f} \terror: {:8.2f}'.format(offset,agisoftUtil.getTotalError()))
        offset = offset +step;
    
    
def syncImages():
    logPath = agisoftUtil.getLogPath()
    imagesPath = agisoftUtil.getImagesPath()
    sync.sync(logPath, imagesPath,askUserForOffset())    
    agisoftUtil.applyGeoreference(imagesPath)

# get argument list using sys module
PhotoScan.app.addMenuItem('EstimateOffset',estimateOffset, shortcut = 'e')
PhotoScan.app.addMenuItem('SyncImages',syncImages, shortcut = 's')
PhotoScan.app.addMenuItem('GetError',agisoftUtil.getTotalError, shortcut = 'r')


