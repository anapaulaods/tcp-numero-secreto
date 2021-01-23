import socket
host = 'localhost'    
port = 2509
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp.connect((host, port))

print('Tente acertar o Número Secreto de 1 a 100! Você terá 5 tentativas.\n Boa Sorte!\n')
tentativas = 5
while tentativas > 0:
    tentativas = tentativas - 1
    numero = int(input('Numero: '))  
    tcp.send(str(numero).encode('utf-8'))
    
    msg = tcp.recv(1024)
    print(repr(msg))

    if (msg == b"Parabens, voce acertou!"):
        tentativas = -1
        tcp.close()

if (tentativas == 0):
    numerosecreto = tcp.recv(1024)
    print('\nVocê não tem mais tentativas sobrando, que pena! O Numero Secreto era:', numerosecreto)
    tcp.close()