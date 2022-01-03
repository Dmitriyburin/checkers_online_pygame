import socket


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = '5.23.55.52'
        self.port = 6668
        self.addr = (self.server, self.port)
    #     self.first_connect = self.connect()
    #
    # def first_connect(self):
    #     return self.p

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def send(self, data):
        try:
            self.client.send(data.encode())
            return self.client.recv(2048).decode()
        except socket.error as e:
            print(e)

    def close(self):
        self.client.close()
