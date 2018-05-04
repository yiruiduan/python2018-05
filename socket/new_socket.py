#Author:yiruidaun
import socket
socket_server=socket.socket()
socket_server.bind(("localhost",5555))
socket_server.listen()
conn,addr=socket_server.accept()
data=conn.recv(1024)
print(data)