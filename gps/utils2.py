def convert_coordinates(dataGps):

    #lat
    lat_min_sec=dataGps[0].split('.')
    latGrado=lat_min_sec[0][0:2]
    latMinute=lat_min_sec[0][2:4]
    latSecond=int(lat_min_sec[1])
    latSecond= round(((latSecond/100)*60)/100, 3)
    latDirection=dataGps[1]

    #lng
    lng_min_sec=dataGps[2].split('.')
    lngGrado=lng_min_sec[0][1:3]
    lngMinute=lng_min_sec[0][3:5]
    lngSecond=int(lng_min_sec[1])
    lngSecond= round(((lngSecond/100)*60)/100, 3)
    lngDirection=dataGps[-1]

    return f"{latGrado}°{latMinute}'{latSecond}\"{latDirection},{lngGrado}°{lngMinute}'{lngSecond}\"{lngDirection}"


