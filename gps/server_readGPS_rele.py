import socket
from parse import parser
import pickle

# Configuración del servidor
HOST = socket.gethostname()   # Cambiar por la dirección IP del servidor si es necesario
PORT = 8080        # Puerto en el que escuchará el servidor

# Crear un socket TCP/IP
server_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
print('Socket created')

server_socket.bind((HOST, PORT))
print('Socket bind complete')

server_socket.listen(10)
print('Socket now listening')
try:
    while True:
        clientsocket, address = server_socket.accept()
        print("***************** Bloque  *************************")
        print(f"connection from {address} has been established")
        # print('Connected by', address)

        clientsocket.send(bytes("OK", "utf-8"))

        try:
            msg=clientsocket.recv(1024)
            
            print(f"{msg} \n")

            try:
                print(f"{pickle.loads(msg)} \n")
            except Exception as et:
                print(f"Error pikcle: {et} \n")

                try:
                    print(msg.hex())
                except Exception as eh:
                    print(f"Error hex: {eh} \n")


            if msg :


                f = open("parsed", "a+")
                

                try:
                    if msg.decode("utf-8").split(',')[0] =='*HQ':
                        converted=parser(msg.decode("utf-8"))
                        
                        f.write("{ \n")
                        f.write(f"id: {converted['id']} \n")
                        f.write(f"coordenates: {converted['coordenates']} \n")
                        f.write(f"date: {converted['date']} \n")
                        f.write(f"time: {converted['time']} \n")
                        f.write("} \n")

                        print("saved")
                        f.close()

                    print(msg.decode("utf-8"))
                    clientsocket.close()

                except Exception as e:
                    print(e)
                    f.close()
                    clientsocket.close()

            print("------------------- FIN Bloque ------------------\n")
            clientsocket.close()

        except Exception as e:
            print(e)
            clientsocket.close()     

except Exception as e:
    print(e)
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t *-* CONNECTION CLOSED *-* ")
