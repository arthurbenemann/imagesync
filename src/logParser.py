import gpstime

def parseLog(log):
    locations = []
    while True:
        gpsLine = log.readline()
        if not gpsLine: break
        if 'FMT' in gpsLine: continue
        if 'PARM' in gpsLine: continue 
        if 'MSG' in gpsLine: continue
        
        if 'GPS' in gpsLine:
            while True:
                attLine = log.readline()
                if not attLine: break
                
                if 'ATT' in attLine:
                    locations.append(parseLogLines(gpsLine, attLine))
                    break;
    return locations

def parseLogLines(gpsLine, attLine):
    # Parse GPS message
    gps = gpsLine.split(',')
    SOW = int(gps[2]) / 1000.0
    gpsWeek = int(gps[3])
    Lat = float(gps[6])
    Lng = float(gps[7])
    # RelAlt = float(gps[8])
    Alt = float(gps[9])
        
    # Parse ATT message
    att = attLine.split(',')
    Roll = float(att[2])
    Pitch = float(att[3])
    Yaw = float(att[4])
    
    # Convert GPS time to UTC
    year, month, day, hh, mm, ss = gpstime.UTCFromGps(gpsWeek, SOW)
    time = gpstime.mkUTC(year, month, day, hh, mm, ss)  
    #return time, Lng, Lat, Alt, Yaw, Pitch, Roll 
    return time, Lng, Lat, Alt
