import socket
import threading
import os


HEADER = 64
port = 6969
FORMAT = "utf-8"
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip, port)
DISCONNECT_MSG= "@disc"
EXIT_MSG = "@killServer 1902-783298-238947"
global thread1
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def client_handle(conn, addr):
    print(f"[CONNECTION] {addr} connected.")
    connected  = True
    conn.send(f"You have connected to server {ADDR} as {addr}. Server Restart Message = {EXIT_MSG}".encode(FORMAT))
    while connected:
        msg_len = conn.recv(HEADER).decode("utf-8")
        if msg_len:
            msg_len = int(msg_len)
            msg = conn.recv(msg_len).decode("utf-8")
            if msg == DISCONNECT_MSG:
                connected = False
                print(f"[CONNECTION] {addr} disconnected.")
                conn.send("Disconnect recieved".encode("utf-8"))
            if msg == EXIT_MSG:
                conn.send(EXIT_MSG.encode(FORMAT))
                conn.close()
                os.abort()
            else:
                message_array = msg.split()
                if len(message_array) > 0:
                         if message_array[0] == "echo":
                            conn.send(f"Echo: {' '.join(message_array[1::])}\n".encode(FORMAT))
                print(f"[{addr} MSG] {msg}")
                conn.send("Message recieved".encode("utf-8"))

    conn.close()

def start():
    server.listen()
    print(f"[LISTEN] Beginning Listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        thread1 = threading.Thread(target=client_handle, args=(conn, addr))
        thread1.start()
        print(f"[CONNECTION] Active Connections ={(threading.activeCount() - 1)}")

print(f"[SERVER] Starting Server...")
start()