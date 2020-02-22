from dump.packet import BasePacket


class Switch:
    """
        Clase usada para describir un Switch

        ...

        Attributes
        ----------
        name : str
            Nombre que para reconocer el Switch
        brand : str
            Marca a la cual pertenece el Switch
        hosts : list
            Lista de hosts conectados al Switch

        Methods
        -------
        def_host(host: Host)
            Asigna una posición de la tabla de enrutamiento del Switch al host - IP
        received_packet(packet: Packet)
            Envía el paquete al host
        """
    table = {}

    def __init__(self, name, brand, hosts):
        self.name = name
        self.__brand = brand
        self.hosts = [self.def_host(host) for host in hosts]

    def def_host(self, host):
        """ Asigna una posición de la tabla de enrutamiento del Switch al host - IP

        Parameters
        ----------
        host : Host
            Indica el host que se desea agregar a la tabla de enrutamiento.

        Raises
        ------
        NotImplementedError
            Si el paquete enviado no es del tipo BasePacket, el sistema retorna error

        """
        self.table[host.ip] = host

    def received_packet(self, packet):
        """ Envía el paquete al host

        Parameters
        ----------
        packet : BasePacket
            Paquete que contiene la información

        Raises
        ------
        NotImplementedError
            Si el paquete enviado no es del tipo BasePacket, el sistema retorna error

        """
        if isinstance(packet, BasePacket):
            raise NotImplementedError("Error en el paquete")
        self.table[packet.dst].received(packet)

