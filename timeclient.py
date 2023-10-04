import socket

sock = socket.socket()
sock.connect(('localhost', 1303))

data = sock.recv(1024)
print(data.decode())
sock.close()

