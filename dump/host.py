from dump.messages import Messages
from dump.packet import BasePacket
from random import randint


class Host:

    ethernet = []

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self.__name = name
        self.ip = ip
        self.mask = mask
        self.ip_table = [0xC0A80001, 0xC0A80002, 0xC0A80003, 0xC0A80004]
        self.ip_table.remove(ip)

    @property
    def name(self):
        return self.__name

    def generate_packet(self, data):
        return BasePacket(self.ip, self.ip_table[randint(0, 2)], data)

    def generate_packet_ip(self, data, ip):
        return BasePacket(self.ip, ip, data)

    def send(self, data, ip=None):
        if ip is None:
            self.ethernet.append(self.generate_packet(data))
        else:
            self.ethernet.append(self.generate_packet_ip(data, ip))

    def received(self):
        packet = self.ethernet.pop()
        if isinstance(packet, BasePacket):
            if packet.dst == self.ip:
                print(Messages.RECEIVED_PACKET + str(self.ip))
                print("Datos:" + packet.data)
                return True
            else:
                print("Paquete rechazado. Mi ip es " + str(self.ip) + ' ,el paquete es para ' + str(packet.dst))
                return False
        else:
            print(Messages.ERROR_PACKET)
            return False
