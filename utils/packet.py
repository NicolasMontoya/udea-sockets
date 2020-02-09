class Packet:
    CONST_DATA = 'INFO'

    def __init__(self, type_packet, data):
        self.__type = type_packet
        self.__data = data
        self.response = None

    @property
    def type(self):
        return self.__type

    @property
    def data(self):
        return self.__data

    def __call__(self):
        return pickle.dumps(self)