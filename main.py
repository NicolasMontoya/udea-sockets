from gita_socket.server import GitaServer, BaseRequestHandler
import pickle
from utils.packet import Packet


class MyTCPHandler(BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(4096)
        data_object = pickle.loads(data)
        if data_object.type == 1:
            data_object.response = 'co'
        else:
            data_object.response = 'None'
        # just send back the same data, but upper-cased
        self.request.sendall(pickle.dumps(data_object))


if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = GitaServer((HOST, PORT), MyTCPHandler)

    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()