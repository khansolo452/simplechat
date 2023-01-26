import socket

server = socket.socket()
host = socket.gethostname()
port = 65432
print(host,port)
server.connect((host,port))

print (server.recv(1024))
server.close()
