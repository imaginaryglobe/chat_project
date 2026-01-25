import socket
import threading

        
def new_client_connection(conn, add):
    while True:
        buf = conn.recv(64)
        if not buf:
            break;
        buf = buf.decode()
        if buf == "exit":
            break
        else:
            messages.append(buf)
            print(add, "says:", buf)

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('localhost', 8089))
serversocket.listen(2) 

messages = []

while True:
    connection, address = serversocket.accept()
    thread = threading.Thread(target=new_client_connection, args=(connection, address))
    thread.start()
