import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', 9091))
sock.listen(10)
conn, addr = sock.accept()

print('connected to:', addr)

while True:
    data = conn.recv(1024)
    print(data)

