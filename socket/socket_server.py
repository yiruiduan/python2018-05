#Author:yiruidaun
import socket
socket_server=socket.socket()
socket_server.bind(("localhost",9998))
socket_server.listen()
conn,addr=socket_server.accept()
while True:
    data=conn.recv(1024).decode("utf-8")
    print(data)
    conn.send(data.upper().encode("utf-8"))
socket_server.close()