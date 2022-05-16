import socket
import threading

HOST = "localhost"
PORT = 5545
MSGEXIT = "!leave"
FORMAT = "utf-8"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))

clients = []


def recieve(conn, addr):
    run = True
    while run:
        msg = (conn.recv(1024)).decode(FORMAT)
        if MSGEXIT in msg:
            print("[SERVER]: Bye, addr: {addr}, conn: {conn}")
            run = False
            conn.send("!exit")
        print(msg)

        for client in clients:
            if client != conn and msg != MSGEXIT:
                client.send(msg.encode(FORMAT))

    conn.close()
    clients.remove(conn)
    

def main():
    s.listen()
    print('[SERVER]: server is ready!!!')

    while True:
        conn, addr = s.accept()
        clients.append(conn)
        t = threading.Thread(target=recieve, args=(conn, addr))
        t.start()
        


main()
