import socket
import threading

HEADER = 64
FORMAT = 'utf-8'
PORT = 5050
SERVER = "192.168.154.1"
DISCONNECT_MESSAGE = "!DISCONNECT"
#SERVER = socket.gethostbyname(socket.gethostname()) another option to do it automaticaly
# ASK GOOGLE FOR PUBLIC IP TO CONNECT FROM DIFFERENT COMPUTERS
#print(SERVER)
ADDR = (SERVER, PORT)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MESSAGE:
                connected = False
            
            print(f"[{addr}] {msg}")
            conn.send("Message Received!". encode(FORMAT))

    conn.close()


def start():
    server.listen()
    print(f"[LISTENNING] Server is listening on {SERVER}")
    listening = True 
    while listening:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")



print("[STARTING] server is starting...")
start()