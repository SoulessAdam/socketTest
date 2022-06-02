import socket
from Crypto.Cipher import AES

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
key = b'ThisIsAKeyTest--'
enc = AES.new(key, AES.MODE_CBC)

def connectSocket():
    IP = input("Input IP: ")
    Port = int(input("Input Port: "))
    ADDR = (IP, Port)
    sock.connect(ADDR)


def MessageLoop():
    while 1:
        send(EncryptMessage(padBytes(input(("[>>>] Message to Send: ")).encode("utf-8"))))


def padBytes(bytes):
    print(bytes)
    bytesToAdd = 16 - len(bytes)
    if bytesToAdd < 0:
        raise BytesWarning("YO FUCKIN MESSAGE TOO BIG")
    for i in range(0, bytesToAdd):
        bytes += b'0'
    print(bytes.__len__())
    return bytes


def EncryptMessage(MessageBytes):
    return enc.encrypt(MessageBytes)


def send(bytes):
    sock.send(bytes)


def main():
    connectSocket()
    MessageLoop()

main()
