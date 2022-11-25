import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9091))
sock.send(b'Hello, server. \n\tIt is me, Constantine Baltsat.\n')

data = sock.recv(1024).decode('utf-8')
print(data)

sock.close()