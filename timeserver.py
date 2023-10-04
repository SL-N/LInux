import socket
from datetime import datetime

sock = socket.socket()
sock.bind(('', 1303))
sock.listen(2)

while True:
    conn, addr = sock.accept()
    now = datetime.now()
    data = now.strftime("%d.%m.%Y, %H:%M")
    conn.send(data.encode(encoding = 'UTF-8'))

        
