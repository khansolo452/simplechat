import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 65432
server.bind((host,port))

print(' before listen')

server.listen(5)
print(host,port)

while True:
    c, addr = server.accept()
    print('first line while')
    
    print('Got connection from', addr)
    c.send(b'Thank you for connecting')
    c.close()
