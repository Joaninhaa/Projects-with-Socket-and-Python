import socket
import threading

HOST = "localhost"
PORT = 5545
MSGEXIT = "leave"
FORMAT = "utf-8"

c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
c.connect((HOST, PORT))

name = input("Username: ")
name = "[" + name + "]: "


def send(run):
    while True:
        try:
            msg = str(input("-> "))
            msg = name + msg
            data = msg.encode(FORMAT)
            c.send(data)
            if MSGEXIT in msg:
                run = False
                c.close()
                break
        except:
            break
    

def recieve(run):
    while True:
        try:
            msg = (c.recv(1024)).decode(FORMAT)
            if msg == "!exit":
                break
            print(msg)
        except:
            break
    run = False


def main():
    run = True
    ta = threading.Thread(target=send, args=(run,))
    t = threading.Thread(target=recieve, args=(run,))
    ta.start()
    t.start()
            


main()
