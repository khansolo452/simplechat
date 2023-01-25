import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 65432
server.bind(('127.0.0.1',port))

print(' before listen')

server.listen(5)
print(host,port)
c, addr = server.accept()
while True:
    print('first line while')
    
    print('Got connection from', addr)
    c.send('Thank you connecting')
    c.close()
