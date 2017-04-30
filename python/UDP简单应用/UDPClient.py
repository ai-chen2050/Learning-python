from socket import *
import os
serverName="192.168.0.107"
serverPort=12000
clientSocket=socket(AF_INET,SOCK_DGRAM)
message=input('Input lowercase sentence: ')
clientSocket.sendto(message,(serverName,serverPort))
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
print(modifiedMessage)
print (serverAddress)
input("UDPClient.py")
a=input()
os.system("pause")
clientSocket.close()
