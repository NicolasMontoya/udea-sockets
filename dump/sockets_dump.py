from socket import AF_INET, SOCK_STREAM, socket


class ServerDump:
    """
    Clase usada para implementar un servidor simple mediante sockets - Python 3

    ...

    Attributes
    ----------
    server_address : tuple
        Tupla con los datos escenciales de configuración (HOST, PORT)
    address_family : int
        Familia de direcciones usada
    socket_type : int
        Tipo de socket usado
    socket: socket
        Socket usado para comunicación

    Methods
    -------
    server_bind()
        Permite configurar al servidor
    server_activate()
        Permite al servidor escuchar peticiones
    server_close()
        Cierra la comunicación del socket
    connection_on(handle)
        Comienza la comunicación y deja listo el sistema para enlazarse con el cliente
    """
    request_queue_size = 5

    def __init__(self, server_address=("localhost", 4444), address_family=AF_INET, socket_type=SOCK_STREAM,
                 bind_and_activate=True):
        # Inicializando servidor
        print("Inicializando servidor")
        self.server_address = server_address
        self.address_family = address_family
        self.socket_type = socket_type
        # Creación de socket
        print("Creación de socket")
        self.socket = socket(self.address_family, self.socket_type)
        if bind_and_activate:
            try:
                print("El socket comienza a escuchar")
                self.server_bind()
                self.server_activate()
            except Exception as e:
                self.server_close()
                raise

    def server_bind(self):
        self.socket.bind(self.server_address)
        self.server_address = self.socket.getsockname()

    # El socket comienza a escuchar
    def server_activate(self):
        self.socket.listen(self.request_queue_size)

    def server_close(self):
        self.socket.close()

    # Esperando el cliente y ejecución función de control
    def connection_on(self, handle):
        print("Esperando cliente")
        conn, add = self.socket.accept()
        while True:
            data = conn.recv(1024)
            print('Recibido {!r}'.format(data))
            if data.decode() == 'QUIT':
                break
            elif data:
                print('Procesando los datos...')
                handle(data, conn)
        self.server_close()


def handle(data: bytearray, conn):
    conn.sendall(data.upper())


s = ServerDump()
s.connection_on(handle)
