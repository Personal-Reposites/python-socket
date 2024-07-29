import socket

mysocket =socket.socket(socket.AF_INET, socket.SOCK_STREAM)

mysocket.connect((socket.gethostname(), 8081))

mysocket.send(bytes("hola mi querido servidor", "utf-8"))

msg=mysocket.recv(1024)

print(msg.decode("utf-8"))