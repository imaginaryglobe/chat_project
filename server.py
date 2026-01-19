import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(2) 

while True:
    connection, address = serversocket.accept()
    buf = connection.recv(64)
    buf = buf.decode()
    if len(buf) > 0:
        print(buf)
        break
