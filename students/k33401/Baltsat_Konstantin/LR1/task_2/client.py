import socket

sock = socket.socket()
sock.connect(('localhost', 9092))

data = input("Введите значение одного из катетов: ").replace(" ", "")
data += " " + input("Введите значение второго катета, если оно известно, иначе - введите 0: ").replace(" ", "")
data += " " + input("Введите значение гипотенузы, если оно известно, иначе - введите 0: ").replace(" ", "")
sock.send(data.encode())


result = sock.recv(1024)
print(result.decode("utf-8"))

sock.close()