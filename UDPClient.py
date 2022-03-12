import socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def connectToServer():
    serverIP = input("Input server ip: ")
    port = int(input("Input server port: "))
    ADDR = (serverIP, port)
    clientSocket.connect(ADDR)


def sendMessageLoop():
    while 1:
        clientSocket.send(input(">>> Outgoing: ").encode("utf-8"))


def main():
    connectToServer()
    sendMessageLoop()

main()