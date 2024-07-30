from utils2 import convert_coordinates

def parser(dataGps):
    converted=dataGps.split(',')


    return {
        'id': converted[1],
        'time':converted[3],
        'coordenates':convert_coordinates(converted[5:9]), #coordenates=['1832.6701', 'N', '06955.2991', 'W']
        'date':converted[11]
    }


# dataGps='*HQ,4720051249,V1,173344,V,1828.6319,N,06957.4483,W,000.00,000,300724,FFFFFBFF,370,02,0,0,6#'

# converted=parser(dataGps)

# print(f"id: {converted['id']} \n")
# print(f"coordenates: {converted['coordenates']} \n")
# print(f"date: {converted['date']} \n")
# print(f"time: {converted['time']} \n\n")
