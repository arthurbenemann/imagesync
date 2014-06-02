#@PydevCodeAnalysisIgnore
import PhotoScan
import sync
import os
import sys
 
def askUserForLogFile():
    return PhotoScan.app.getOpenFileName('ArduPilot Flight log (.log)')
def askUserForOffset():
    return PhotoScan.app.getFloat('Offset value in seconds',0)

def estimateOffset():
    logPath = askUserForLogFile()
    offsetMessage = sync.sync(logPath,None)
    PhotoScan.app.messageBox(offsetMessage)

def syncImages():
    logPath = askUserForLogFile()
    path, name = os.path.split(logPath)
    sync.sync(logPath,askUserForOffset())    

    CoordinateSystem = PhotoScan.CoordinateSystem()
    CoordinateSystem.init('EPSG::4326')
    PhotoScan.app.document.activeChunk.ground_control.projection = CoordinateSystem
    PhotoScan.app.document.activeChunk.ground_control.crs = CoordinateSystem
    PhotoScan.app.document.activeChunk.ground_control.apply()
    PhotoScan.app.document.activeChunk.ground_control.load(path + '/georeference.txt','csv')
    PhotoScan.app.document.activeChunk.ground_control.apply()

# get argument list using sys module
PhotoScan.app.addMenuItem('EstimateOffset',estimateOffset, shortcut = 'e')
PhotoScan.app.addMenuItem('SyncImages',syncImages, shortcut = 's')

