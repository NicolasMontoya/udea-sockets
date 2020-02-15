class Router:
    table = {}

    def __init__(self, name, brand, hosts):
        self.name = name
        self.__brand = brand
        self.hosts = [self.def_host(host) for host in hosts]

    def def_host(self, host):
        self.table[host.ip] = host

    def received_packet(self, packet):
        self.table[packet.dst].received(packet)

