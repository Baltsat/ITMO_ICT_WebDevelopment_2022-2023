import socket
from math import sqrt

sock = socket.socket()
sock.bind(('', 9092))
sock.listen(10)
conn, addr = sock.accept()

print('Connected to', addr)

while True:
    data = conn.recv(1024).decode()
    try:
        data = data.split(" ")
        katet_1 = float(data[0])
        katet_2 = float(data[1])
        gipotenyza = float(data[2])
    except:
        conn.sendall('Неверный формат входных данных!\n'.encode())
    else:
        if katet_2 == 0:
            katet_2 = sqrt(gipotenyza**2 - katet_1**2)
            conn.sendall(f'Второй катет имеет длину: {katet_2}\n'.encode())
        elif gipotenyza == 0:
            gipotenyza = sqrt(katet_1**2 + katet_2**2)
            conn.sendall(f'Гипотенуза имеет длину: {gipotenyza}\n'.encode())
        else:
            if gipotenyza == sqrt(katet_1**2 + katet_2**2):
                conn.sendall('Это прямоугольный треугольник. Теорема Пифагора выполняется.'.encode())
            else:
                conn.sendall('Треугольник не прямоугольный. Теорема Пифагора не выполняется.'.encode())

    if not data:
        break
    conn.send(b'Bye.\n')
