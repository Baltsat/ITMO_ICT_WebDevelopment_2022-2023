import threading
import socket
import time


def get_message():
    while True:
        try:
            data = sock.recv(1024).decode('utf-8')
            print(data)
        except socket.error:
            time.sleep(0.5)
            continue


def write_message():
    while True:
        message = input('[' + name + '] ')
        sock.sendto(('[' + name + '] ' + message).encode('utf-8'), server)
        if message == 'EXIT':
            sock.close()
            break
            
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(('localhost', 9094))

name = input('Введи свой ник: ')
print(f'Привет, {name}! Теперь можешь писать сообщения. \nЕсли захочешь выйти из чата напиши EXIT\n')

server = '', 9094
sock.sendto((name).encode('utf-8'), server)

thread_send = threading.Thread(target=write_message, args=())
thread_get = threading.Thread(target=get_message, args=())

thread_send.start()
thread_get.start()
