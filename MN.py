import socket
import json

def main(isSend,id,port,pair,message):

    f = open('config.json',)
    data = json.load(f)
    ip = data['Nodes'][0]['ip']
    f.close()
    bufferSize = 1024

    if(isSend == '1'):

        bytesToSend = str.encode(message)
        serverAddressPort = (ip, port)
        UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPSocket.sendto(bytesToSend, serverAddressPort)
        msgFromPair = UDPSocket.recvfrom(bufferSize)
        trimmed = ":{}".format(msgFromPair[0])
        trimmed = trimmed[2:]
        msg = "--MN--:Message arrived from " + pair + ": " + trimmed
        print(msg)
        print("----------------------------------------------------")


    else:
        UDPSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        UDPSocket.bind((ip, port))
        bytesAddressPair = UDPSocket.recvfrom(bufferSize)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]
        trimmed = ":{}".format(message)
        trimmed = trimmed[2:]
        clientMsg = "--MN--:Message arrived from " + pair + " node :" + trimmed
        clientIP = "--MN--:Pair IP Address:{}".format(address)
        print(clientMsg)
        print(clientIP)
        ackMessage = "acknowledge packet from MN Node"
        bytesToSend = str.encode(ackMessage)
        UDPSocket.sendto(bytesToSend, address)
