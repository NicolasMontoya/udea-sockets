import pickle
import socket
from utils.packet import Packet


class GitaClient:

    cache = []

    def __init__(self, host="localhost", port=9999, socket_type=1, auto_connection=True):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__host = host
        self.__port = port
        self.socket_type = socket_type
        if auto_connection:
            self.socket.connect((self.__host, self.__port))

    def open_connection(self):
        self.socket.connect((self.__host, self.__port))

    def send(self, packet):
        data = pickle.dumps(packet)
        self.socket.send(data)

    def send_and_wait(self, packet):
        self.send(packet)
        res = self.socket.recv(1024)
        return res

    def close_connection(self):
        self.socket.close()
