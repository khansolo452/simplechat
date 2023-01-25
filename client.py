import socket

server = socket.socket()
host = socket.gethostname()
port = 65432
print('127.0.0.1',port)
server.connect((host,port))

print (server.recv(1024))
server.close()
