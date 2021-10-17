from socket import *

IP = '127.0.0.1'
PORT = 5555

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind((IP, PORT))
tcpSerSock.listen(10)
tcpCliSock, addr = tcpSerSock.accept()
data = tcpCliSock.recv(2048)
#print(data)
target = socket(AF_INET,SOCK_STREAM)
target.connect(('93.184.216.34', 80))
target.sendall(data)

data_r = target.recv(2048)
#print(data_r)
tcpCliSock.sendall(data_r)

target.close()
tcpCliSock.close()
tcpSerSock.close()