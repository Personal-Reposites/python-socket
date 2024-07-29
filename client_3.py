import socket

ip="54.87.142.68"

mysocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect((socket.gethostname(), 8081))

mysocket.send(bytes("hola mi querido servidor", "utf-8"))


#Getting Datos
full_msg=''

while True:
	msg=mysocket.recv(8)

	if len(msg) <=0:
		break
	full_msg += msg.decode("utf-8")
#Fin Getting Datos

print(full_msg)