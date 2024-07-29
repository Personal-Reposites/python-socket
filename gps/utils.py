dataGPS= '1828.7736,N,06957.3862,W'

def convert_coordinates(dataGps):
    latLng=dataGps.split(',0')
    #print(latLng)

    return {
        'latitude': f"{latLng[0]}",
        'longitude': f"{latLng[1]}"
    }

converted=convert_coordinates(dataGPS)

print(converted['latitude'])
print(converted['longitude']) 
