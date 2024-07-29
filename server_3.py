import socket

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
        print(f"connection from {address} has been established")
        # print('Connected by', address)

        clientsocket.send(bytes("welcome to the server 2", "utf-8"))

        try:
            msg=clientsocket.recv(1024)

            if msg :
                print(msg.decode("utf-8"))


            clientsocket.close()

        except Exception as e:
            print(e)
            clientsocket.close()     

except Exception as e:
    print(e)
    print("\n\n\t\t\t\t\t\t\t\t\t\t\t *-* CONNECTION CLOSED *-* ")
