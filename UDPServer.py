import socket
import threading
import os


HEADER = 1024
port = 6969
FORMAT = "utf-8"
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip, port)
DISCONNECT_MSG= "@disc"
EXIT_MSG = "@killServer 1902-783298-238947"

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def startRecv():
    print(f"[UDP CLIENT] Listening on {ADDR}")
    while True:
        bytesAddressPair = server.recvfrom(HEADER)

        message = bytesAddressPair[0]

        address = bytesAddressPair[1]

        clientMsg = "Message from Client:{}".format(message)
        clientIP = "Client IP Address:{}".format(address)

        print(clientMsg)
        print(clientIP)

startRecv()