import socket
import threading


HEADER = 64
port = 6969
server_ip = socket.gethostbyname(socket.gethostname())
ADDR = (server_ip, port)
DISCONNECT_MSG= "@disc"
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def client_handle(conn, addr):
    print(f"[CONNECTION] {addr} connected.")
    connected  = True
    while connected:
        msg_len = int(conn.recv(HEADER).decode("utf-8"))
        msg = conn.recv(msg_len).decode("utf-8")
        if msg == DISCONNECT_MSG: connected = False
        print(f"[{ADDR} MSG] {msg}")

    conn.close()

def start():
    server.listen()
    print(f"[LISTEN] Beginning Listening on {ADDR}")
    while True:
        conn, addr = server.accept()
        threading.Thread(target=client_handle, args=(conn, addr)).start()
        print(f"[CONNECTION] {threading.activeCount() -1}")

print(f"[SERVER] Starting Server...")
start()