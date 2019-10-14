import socket


class Server(object):
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def bind_listen(self, port):
        self.sock.bind(('0.0.0.0', port))
        self.sock.listen(5)

    def accept_receive_close(self):
        (client_socket, address) = self.sock.accept()
        msg = client_socket.recv(1024)
        self.on_msg(msg)
        client_socket.close()