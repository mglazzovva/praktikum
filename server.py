import subprocess
import os
import socket


HOST = (socket.gethostname(), 9090)


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(HOST)
s.listen()

print('i am listening')

while True:
    conn, addr = s.accept()
    print('connected -', addr)
    res = b'Hello'
    conn.send(res)
    conn.close()
    