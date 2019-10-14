import socket


class Client(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self, host, port):
        self.sock.connect((host, port))

    def send(self, data):
        self.sock.send(data)


if __name__ == "__main__":
    c = Client()
    c.connect('127.0.0.1', 6789)
    c.send("shit".encode("utf-8"))