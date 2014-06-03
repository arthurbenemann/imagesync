import PhotoScan
import os

def getProjectPath():
    path, name = os.path.split(PhotoScan.app.document.path)  # @UnusedVariable
    return path

def getLogPath():
    return getProjectPath() +'/logs/log.log'

def getImagesPath():
    return getProjectPath() +'/images/'

def applyGeoreference(path):
    CoordinateSystem = PhotoScan.CoordinateSystem()
    CoordinateSystem.init('EPSG::4326')
    PhotoScan.app.document.activeChunk.ground_control.projection = CoordinateSystem
    PhotoScan.app.document.activeChunk.ground_control.crs = CoordinateSystem
    PhotoScan.app.document.activeChunk.ground_control.apply()
    PhotoScan.app.document.activeChunk.ground_control.load(path+ '/georeference.txt', 'csv')
    PhotoScan.app.document.activeChunk.ground_control.apply()


def getTotalError():
    exportedLocations = getProjectPath()+'exportedLocations.csv'
    PhotoScan.app.document.activeChunk.ground_control.save(exportedLocations,'csv')
    for line in open(exportedLocations, 'r'):
        if '# Total error' in line: 
            return float(line.split('\t')[7])
        