import socket

HOST = (socket.gethostname(), 9090)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(HOST)
print('Connected to', HOST)

msg = client.recv(1024)
print(msg.decode('UTF-8'))