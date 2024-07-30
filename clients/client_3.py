import socket

ip="10.0.0.28"
port=8080

mysocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect((ip, port))
#sms='hola mi querido servidor'
sms='*HQ,4720051299,V1,173344,V,1828.6319,N,06957.4483,W,000.00,000,300724,FFFFFBFF,370,02,0,0,6#'

mysocket.send(bytes(sms, "utf-8"))


#Getting Datos
full_msg=''

while True:
	msg=mysocket.recv(8)

	if len(msg) <=0:
		break
	full_msg += msg.decode("utf-8")
#Fin Getting Datos

print(full_msg)