import socket

# Configuración del servidor
HOST = socket.gethostname()   # Cambiar por la dirección IP del servidor si es necesario
PORT = 8080        # Puerto en el que escuchará el servidor

    # Crear un socket TCP/IP
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
    print('Socket created')
    server_socket.bind((HOST, PORT))
    print('Socket bind complete')
    server_socket.listen(10)
    print('Socket now listening')

    
    try:
        while True:

            conn, addr = server_socket.accept()

            with conn:

                print('Connected by', addr)
                try:
                    #data = conn.recv(1024)
                    # Convert the byte string to a hexadecimal representation
                    
                    # The byte string provided
                    # byte_string = b'xx\x11\x01\x03RP0\x96t\x86\x18 \x14\x00\x01\x00\x00\x1aN\r\n'

                    hex_representation = conn.recv(1024).hex()

                    if hex_representation.startswith('7878') :
                        # Format it to look like a typical hexadecimal dump with spaces or colons if desired
                        #formatted_hex = ' '.join(hex_representation[i:i+2] for i in range(0, len(hex_representation), 2))

                        #formatted_hexadecimal = [(hex(int(i, 16))) for i in formatted_hex.split(' ')]

                        print("\n Datos Entrantes:")
                        print(hex_representation)
                        #print(formatted_hex)
                        #print(formatted_hexadecimal)
                        print("\n ")
                       

                    else:
                        conn.close()                        

                    conn.close()

                except Exception as e:
                    print(e)
                    conn.close()
 

        server_socket.close()
    except Exception as e:
        print(e)
        print("\n\n\t\t\t\t\t\t\t\t\t\t\t *-* CONNECTION CLOSED *-* ")
