from utils2 import convert_coordinates

def parser(dataGps):
    converted=dataGps.split(',')


    return {
        'id': converted[1],
        'time':converted[3],
        'coordenates':convert_coordinates(converted[5:9]), #coordenates=['1832.6701', 'N', '06955.2991', 'W']
        'date':converted[11]
    }

