import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientsocket.connect(('localhost', 8089))
while True:
    msg = input("send a message to the server, or type 'close server' to shut it down.")
    text = msg.encode()
    clientsocket.send(text)
    if msg == "close server":
        break