
class BasePacket:
    def __init__(self, src, dst, data):
        self.__dst = dst
        self.__src = src
        self.__data = data

    @property
    def data(self):
        return self.__data

    @property
    def src(self):
        return self.__src

    @property
    def dst(self):
        return self.__dst

    @data.setter
    def data(self, data):
        self.__data = data
