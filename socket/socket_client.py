#Author:yiruidaun
import socket,os
enter=""

while enter!="quit":
    enter=input("请输入您要说的话：")
    client = socket.socket()
    client.connect(("localhost", 5555))
    client.send(enter.encode("utf-8"))
    client.close()
