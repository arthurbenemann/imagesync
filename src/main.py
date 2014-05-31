import sys
import sync
 
# get argument list using sys module
arg = sys.argv

logPath = arg[1]

if len(arg) == 1:
    print('specify a log file')   
if len(arg) == 2:
    sync.sync(logPath,None)
else:
    sync.sync(logPath, float(arg[2]))
