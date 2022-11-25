import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9093))

data = sock.recv(1024)
print(data.decode("utf-8"))

sock.close()
