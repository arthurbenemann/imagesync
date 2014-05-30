import os.path

def findImages(path):
    imagesList = []
    for fileInPath in os.listdir(path):
        if "JPG" in fileInPath:
            imagesList.append([fileInPath, os.path.getmtime(path + '/' + fileInPath)])
        
    imagesList.sort()
    return imagesList 
        
