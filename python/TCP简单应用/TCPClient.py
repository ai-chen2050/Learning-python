from socket import *
import os
serverName='192.168.0.107'
serverPort=12000
clientSocket=socket(AF_INET,SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
sentence=input('input lowercase sentence:')
clientSocket.send(sentence.encode("utf-8"))
modifiedSentence=clientSocket.recv(1024)
print('From Server:',modifiedSentence.decode("ASCII"))
a=input()
os.system("pause")
clientSocket.close()
