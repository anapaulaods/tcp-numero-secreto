import socket
from random import *
random = randint(1,100)

host = 'localhost'
port = 2509

tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.bind((host, port))
tcp.listen(1)

connect, addr = tcp.accept()
print('Bem vindo Cliente: ', addr)
tentativas = 5
while tentativas > 0:
    print(random)
    numero = int(connect.recv(1024))
    tentativas = tentativas - 1
    if numero > random:
        connect.send(b'Numero secreto e menor!')
    if numero < random:
        connect.send(b'Numero secreto e maior!')
    if numero == random:
        connect.send(b'Parabens, voce acertou!')
        tentativas = -1
    if not numero:
        break

connect.send(str(random).encode('utf-8'))     
connect.close()