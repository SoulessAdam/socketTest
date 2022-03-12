import socket

HEADER = 1024
port = 6969
FORMAT = "utf-8"
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip, port)

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(ADDR)

def startRecv():
    print(f"[UDP CLIENT] Listening on {ADDR}")
    while True:
        bytesAddressPair = server.recvfrom(HEADER)
        message = bytesAddressPair[0]
        address = bytesAddressPair[1]

        print(f"Message From {address}: {message}")

startRecv()