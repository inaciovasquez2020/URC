import socket, threading, json

PEERS = set()
PORT = 8338

def send(sock, msg):
    sock.sendall((json.dumps(msg)+"\n").encode())

def handle_peer(conn, addr, on_msg):
    buf = b""
    while True:
        data = conn.recv(4096)
        if not data: break
        buf += data
        while b"\n" in buf:
            line, buf = buf.split(b"\n",1)
            on_msg(json.loads(line))
    conn.close()

def serve(on_msg):
    s = socket.socket()
    s.bind(("", PORT))
    s.listen()
    while True:
        c,a = s.accept()
        threading.Thread(target=handle_peer,args=(c,a,on_msg),daemon=True).start()

def connect(host, on_msg):
    s = socket.socket()
    s.connect((host, PORT))
    threading.Thread(target=handle_peer,args=(s,(host,PORT),on_msg),daemon=True).start()
    return s
