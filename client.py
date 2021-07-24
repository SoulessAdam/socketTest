import socket

HEADER = 64
port = 6969
FORMAT = "utf-8"
DISCONNECT_MSG= "@disc"
server_ip = "192.168.0.117"
EXIT_MSG = "@killServer 1902-783298-238947"
ADDR = (server_ip, port)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send_msg(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length = padMessage(send_length)
    client.send(send_length)
    client.send(message)
    print(client.recv(2048).decode(FORMAT))
    
def padMessage(msg):
    msg += b' '*(HEADER-len(msg))
    return msg

print(f"Connected to server {ADDR}.")
print(client.recv(2048).decode(FORMAT))
while True:
    print(client.recv(2048).decode(FORMAT))
    message = input("Input Message To Send: ")
    send_msg(message)
    if message == DISCONNECT_MSG:
        break