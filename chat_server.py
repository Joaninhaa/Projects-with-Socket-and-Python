import socket
import threading

HOST = "192.168.1.110"
PORT = 5545
MSGEXIT = "!leave"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
FORMAT = "utf-8"
clients = []

def recieve(conn, addr):
    run = True
    while run:
        msg = (conn.recv(1024)).decode(FORMAT)
        if MSGEXIT in msg:
            print("[SERVER]: tão vazando!!!")
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
    print('[SERVER]: AYAYAY')
    while True:
        conn, addr = s.accept()
        clients.append(conn)
        t = threading.Thread(target=recieve, args=(conn, addr))
        t.start()
        


main()
