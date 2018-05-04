#Author:yiruidaun
import socket,sys,os,time

s = socket.socket()
s.connect(("localhost", 9998))

try:
    while True:

        msg=input("please input your massage:")
        msg=msg.strip()
        if len(msg)==0:
            continue
        s.send(msg.encode("utf-8"))
        if msg is "q":break
        data=s.recv(102400).decode("utf-8")
        if data=="q":
            break
        for line in data.split("\n"):
            print(line)
    s.close()
except ConnectionRefusedError:
    print("连接已经断开!!!")
