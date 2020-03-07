## Practica de Sockets con POO

La programación en red surge como respuesta
a la necesidad de intercambiar información
entre aplicaciones que se ejecutan en
estaciones que se encuentran conectadas a
través de una red de comunicación. Sin
embargo, para que dos aplicaciones puedan
comunicarse entre sí es necesario que un
programa pueda localizar al otro y que, además, ambos programas sean capaces de
intercambiar información. Es entonces en este contexto donde los desarrolladores
propusieron el concepto de socket. 

### Socket
Los sockets son la forma más popular de implementar IPC (Inter Process
Communications), para las comunicaciones interplataforma. Un socket corresponde
a una abstracción utilizada en la programación en red para identificar un extremo de
la conexión/comunicación a establecer. Incluso, un socket también permite
implementar la comunicación entre dos aplicaciones que residen o en el mismo
dispositivo. Sin embargo, existen otros mecanismos IPC para comunicar procesos en
la misma estación. 

### Introducción a POO

POO es un paradigma de programación que usa objetos y sus interacciones, para diseñar aplicaciones y
programas informáticos. Está basado en varias técnicas, incluyendo herencia, abstracción, polimorfismo y
encapsulamiento. Su uso se popularizó a principios de la década de los años 1990. En la actualidad, existe variedad
de lenguajes de programación que soportan la orientación a objetos.

#### Cómo se piensa en objetos

Pensar en términos de objetos es muy parecido a cómo lo haríamos en la vida real. Por ejemplo vamos a pensar en un coche
para tratar de modelizarlo en un esquema de POO. Diríamos que el coche es el elemento principal que tiene una serie de
características, como podrían ser el color, el modelo o la marca. Además tiene una serie de funcionalidades asociadas,
como pueden ser ponerse en marcha, parar o aparcar.

Pues en un esquema POO "el coche" sería lo que se conoce como "Clase". Sus características, como el color o el modelo,
serían propiedades y las funcionalidades asociadas, como ponerse en marcha o parar, serían métodos.


#### Conceptos fundamentales

El paradigma de programación POO busca modelar objetos relevantes a un problema mediante la descripción de sus atributos y 
métodos. 

Nota: Para la primer sección usaremos la consola de Python, o en su defecto puede usar el archivo main.py para ir
explorando el comportamiento de Python.


**Clase:**  Es una definición abstracta de un concepto. En programación permite definir las propiedades y 
el comportamiento de un tipo de objeto concreto. 

```bash
PyDev console: starting.
Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] on win32
# Note que la primera letra de la clase definida tiene una letra mayuscula, esta convención para digitar el código se
# denomina CamelCase
class Nodo:
...     name = 'Nombre nodo'
...     def send(self):
...         print('Enviado ' + 'nombre')
...     def recv(self):
...         print('Recibido')
... 
```

**Objeto:** Se define como la instancia de una clase. Se encuentra provista de un conjunto de propiedades o atributos
 propios (datos) y de comportamiento o funcionalidad (métodos). Estos se crean a partir de la definición de una clase 
 y permite generar elementos con valores reales.


```bash
    # Despues de definir la clase Nodo en la consola vamos a crear un objeto de la clase Nodo y usaremos su función
    # send
    miNodo = Nodo()
    miNodo.send()
    Enviado nombre
```

NOTA: Si desea explore las funciones de Python getattr y setattr, las dos funciones nos permiten trabajar con
atributos de un objeto en Python.

```bash
    # Ejemplo de uso de las funciones getattr y setattrjhf,
    >> setattr(l, 'nuevo',True)

   >> getattr(l, 'nuevo')
    True

    >> l.nuevo
    True
```

Python es un lenguaje muy flexible que permite manipular atributos en cualquier parte del código. Podemos incluso agregar
y eliminar atributos desde fuera de la clase. Asi:


```bash
    # Ejemplo de uso de las funciones getattr y setattrjhf,
    >> miNodo.type = 'x'
    >> del miNodo.type
```

### Metodos especiales

Las clases en Python tiene unos metodos especiales que permiten modificar el comportamiento de los objetos o incluso,
redefinir comportamientos genericos del lenguaje. Algunos de estos metodos especiales son:

**__init\__:** Método que se llama al crear una instancia de un objeto,  cumple con el rol de inicializador y se difiere
del constructor porque se ejecuta despues de que el objeto ya a sido construido.

````python

class Node:
     """Basic Node"""
    def __init__(self, name = 'Por Defecto', address = 0x0771):
        self.name = name
        self.address = address
        self.type = 'PC'
        print('El objeto fue creado')
    def send(self):
        """Función para enviar datos"""
        print('sending')
    def recv(self):
        """Función para recibir datos"""
        print('Receiving')
    
````

**__str\__:** Metodo que se ejecuta una vez se llame el objeto como string, es decir, cuando se solicita una impresión
del objeto, este retorna el valor que se encuentre en la función __str\__

````python

class Node:
     """Basic Node"""
    def __init__(self, name = 'Por Defecto', address = 0x0771):
        self.name = name
        self.address = address
        self.type = 'PC'
        print('El objeto fue creado')
    def send(self):
        """Función para enviar datos"""
        print('sending')
    def recv(self):
        """Función para recibir datos"""
        print('Receiving')
    def __str__(self) -> str:
        """
        Este metodo retorna las propiedades del objeto en un cadena de texto
    
        Returns
        -------
        str
            Valor final del objeto
        
        Examples
        --------
        Despues de crear una instancia del objeto usamos el siguiente comando
    
        >> miNodo = Node('Mi nodo', 0x0102)
        >> print(miNodo)
    
        """
        # Ejemplo de documentación
        return self.type + ' -> ' + ' Nombre: ' + self.name + ' Dirección: ' + self.address 

    
````

En el ejemplo de uso de la función str podemos identificar los comentarios con docstring en formato Numpy. Mediante
dicha documentación es posible dar claridad sobre avances de proyecto o simplemente clarificar el uso de un código
determinado.

**__del\__:** Metodo que se ejecuta una vez se destruye el objeto, este metodo es muy similar al destructor de C.
Se usa para ejecutar una acción particular cuando una instancia de un objeto deja de existir. Generalmente el metodo
del para destruir instancias no se utiliza y se le permite al interprete gestionar los recursos de los objetos a 
discreción

````python

class Node:
     """Basic Node"""
    def __init__(self, name = 'Por Defecto', address = 0x0771):
        self.name = name
        self.address = address
        self.type = 'PC'
        print('El objeto fue creado')
    def send(self):
        """Función para enviar datos"""
        print('sending')
    def recv(self):
        """Función para recibir datos"""
        print('Receiving')
    def __del__(self):
        """ Función que se ejecuta en la destrucción de un objeto 
        
        Examples:
        --------
        Una vez creado un objeto, al destruirlo se llama esta función
    
        >> miNodo = Node('Nombre', 0x1373)
        >> del miNodo
        """
        print('Hasta luego, Me destruyo')

    
````

**__add\__:** Metodo que permite gestionar el operador suma para un objeto de la clase

````python

class Node:
     """Basic Node"""
    def __init__(self, name = 'Por Defecto', address = 0x0771):
        self.name = name
        self.address = address
        self.type = 'PC'
        print('El objeto fue creado')
    def send(self):
        """Función para enviar datos"""
        print('sending')
    def recv(self):
        """Función para recibir datos"""
        print('Receiving')
    def __add__(self, other) -> Node:
        """ Función que se ejecuta ante la suma
        
        Examples:
        --------
        Esta función se ejecuta cuando se suman dos Nodos
    
        >> a = Node('nombre 1', 0x01)
        El objeto fue creado
        >> b = Node('nombre 2', 0x01)
        El objeto fue creado
        >> c = a + b
        El objeto fue creado
        >> c.name
        'nombre 2 ADD nombre 1'

        """
        if isinstance(other, Node):
            return Node(other.name + ' ADD ' + self.name, 0x0)
        else
            return NotImplemented
    
````

**__gt\__ , __eq\__ y __lt\__:** Metodos de comparación de objetos, permiten comparar cuando un
objeto es mayor, menor o igual que otro, son de especial utilidad cuando necesitamos definir
jerarquia entre diferentes objetos de la misma clase.

````python

class Node:
     """Basic Node"""
    def __init__(self, name = 'Por Defecto', address = 0x0771):
        self.name = name
        self.address = address
        self.type = 'PC'
        print('El objeto fue creado')
    def send(self):
        """Función para enviar datos"""
        print('sending')
    def recv(self):
        """Función para recibir datos"""
        print('Receiving')
    def __gt__(self, other) -> bool:
        if self.address > other.address:
            return True
        else :
            return False
    def __lt__(self, other) -> bool:
        if self.address < other.address:
            return True
        else :
            return False
    def __eq__(self, other) -> bool:
        if self.address == other.address:
            return True
        else :
            return False
    
````

````python

>> a = Node('Nodo 1', 10)
El objeto fue creado
>> b = Node('Nodo 2', 8)
El objeto fue creado
>> c = a + b
El objeto fue creado
>> d = Node('Nodo 3', 23)
El objeto fue creado
>> e = Node('Nodo 4', 23)
El objeto fue creado
>> d == e
True
>> d != e
False
>> d > e
False
>> d > a
True
>> a > d
False


````

En el anterior código podemos identificar un ejemplo donde mediante la dirección de la clase Node, podemos comparar
cada uno de los objetos y determinar cuales son mayores, cuales son menores y su igualdad.

 ### Vamos a jugar un poco con operadores y privacidad.

Vamos a crear una clase llamada Link que permita comunicar Nodos. Para esto ¿Qué necesitamos? ... El link debe tener
dos accesos multidireccionales, un nombre, una marca y unas caracteristicas.

```python
class Link:

    def __init__(self, name, brand):
        self.name = name
        self.brand = brand
    def __del__(self):
        pass
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass
```

Ahora ¿qué pasa? si yo ejecuto las siguientes lineas:

```bash
>> lin = Link('Mi link', 'CISCO')
>> lin.name = 'Nuevo nombre'
>> lin.brand = 'ASUS'

```

¿Debería poder modificar la marca de mi enlace?, ¿Debería poder modificar el nombre del enlace?
Como muchos otro objetos, el nombre es una atributo que debería ser publico puesto que
puede darsele un uso distinto y cambiar de nombre a discreción de usuario, el nombre es una atributo de identificación
para el usuario y no cumple una función única, mientras que la marca si es un atributo privado que no debería poder
modificarse, pues define que empresa construyo dicho objeto.

```python
class Link:

    def __init__(self, name, brand):
        self.name = name
        self._brand = brand
    def __del__(self):
        pass
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass

>> lin = Link('name', 'CISCO')
>> lin._brand = 'Nuevo'
>> print(lin._brand)
```

Ejecutemos el código anterior, ¿Qué sucedió?¿Existe alguna advertencia por parte del interprete de Python?.
¿Que considera que significa el guión bajo en Python?.


```python
class Link:

    def __init__(self, name, brand):
        self.name = name
        self.__brand = brand
    def __del__(self):
        pass
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass

>> lin = Link('name', 'CISCO')
>> print(lin.__brand)
>> lin.__brand = 'Nuevo'
>> print(lin.__brand)

```

Ejecutemos el código anterior, ¿Qué sucedió? ¿Qué diferencia existe con el caso anterior?.
¿Que considera que significa el doble guión bajo en Python?, ¿El valor de la variable __brand realmente cambio?.

```python
class Link:

    def __init__(self, name, brand):
        self.name = name
        self.__brand = brand
    @property
    def brand(self):
        return self.__brand
    def __del__(self):
        pass
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass

>> lin = Link('name', 'CISCO')
>> print(lin.__brand)
>> lin.__brand = 'Nuevo'
>> print(lin.__brand)
>> print(lin.brand)

```

¿Cómo es esto posible?, ¿Qué son las variables con doble guión bajo?

En Python la privacidad no fue definida desde su concepción, esta situación llevo al lenguaje a ciertos escenarios donde
tuvo que adaptarse mediante su evolución. Según los ejemplos anteriores podemos determinar que __ doble guión bajo
implica privacidad, implica que el campo no puede accederse desde el exterior, mientras que un solo guión bajo no
implica seguridad, pero si es una adventencia al usuario que no debería tocar dicho atributo directamente. Otro dato 
útil es el uso de la anotación property (@property) para acceder a propiedades privadas mediante una función
 intermediaria que vigila que el campo no sea sobrescrito sin permiso explicito.


### ¿POO en redes? La comunicación más simple

"Imagine" que tiene frente a usted su computador, internamente el dispositivo cuenta con cientos de circuitos y 
funcionalidades que difícilmente podrían describirse con precisión, sin embargo, las abstracciones de que hemos ido
aprendiendo nos permiten describir solo un parte del sistema obviando los demás elementos que lo conforman. Teniendo
en cuenta lo anterior piense que elementos de red describen su equipo. Con esto en mente vamos a plantear la
comunicación más simple, dos equipos conectados mediantes un cable coaxial.

Una implementación sencilla de un Nodo sería:

```python
class Nodo:

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self.__name = name
        self.ip = ip
        self.mask = mask
```

En la anterior implementación se define la ip, la mascara de red y un nombre para el equipo. Ahora definiremos una 
variable donde se registren las IP que conoce el host así:

```python
class Node:

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self._name = name
        self.ip = ip

```

Nuestro DumpHost se encuentra defino... pero ¿Qué hace nuestro HOST?, actualmente nada, sin embargo es nuestra tarea
programar las dos funcionalidades más básicas de un host, enviar y recibir.

```python
class Node:

    def __init__(self, name, ip=0xC0A80001):
        self.__name = name
        self.ip = ip
    
    def send(self):
        pass
    
    def received(self):
        pass
```

¿Qué debería enviar nuestro host?, exacto, paquetes, para crear los paquetes definiremos una clase bastante simple
llamada Packet, dicha clase tendrá una IP destino, una IP origen y datos. Recuerde usar lo aprendido en la introducción
a POO.

```python
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

```

El paquete debe tener sus atributos privados pues una vez estructurado no debería poder modificarse sus atributos 
claves.

Con la clase Link de los ejemplos pasados construiremos un elemento que permita transmite dichos paquetes, a su vez 
modificaremos la clase Node.

```python

class Node:

    def __init__(self, name, ip=0xC0A80001):
        self.port = None
        self.link = None
        self.__name = name
        self.ip = ip

    # Anotación propiedad que sirve para acceder de manera simple desde la instancia. Una vez definido el nombre
    # del equipo este no puede cambiarse.
    @property
    def name(self):
        return self.__name

    def is_connected(self):
        return self.link is not None

    def connect(self, port, link):
        self.link = link
        self.port = port

    def disconnect(self, port):
        self.link = None
        self.port = None

class Link:
    def __init__(self, name, brand):
        self.name = name
        self.__brand = brand
        self.nodeOne = None
        self.nodeTwo = None
    @property
    def brand(self):
        return self.__brand

    def connect(self, nodeOne: Node, nodeTwo: Node) -> bool:
        self.nodeOne = nodeOne
        self.nodeTwo = nodeTwo
        nodeOne.connect(1,self)
        nodeTwo.connect(2,self)


>> a = Node('Nodo 1', 1)
>> b = Node('Nodo 2', 2)
>> a.is_connected()
False
>> b.is_connected()
False
>> lin = Link('Cable', 'ASUS')
>> lin.connect(a, b)
>> a.is_connected()
True
>> b.is_connected()
True

```

Ahora tenemos un puente entre Nodos, finalmente tenemos que permitir enviar paquetes entre dispositivos conectados. 
Para esto creamos una función llamada transmit en la clase Link que permita pasar la información de un nodo a otro y un
buffer en cada Nodo que reciba los paquetes

```python
from dump.packet import BasePacket


class Node:

    def __init__(self, name, ip=0xC0A80001):
        self.port = None
        self.link = None
        self.__name = name
        self.buffer = []
        self.ip = ip

    # Anotación propiedad que sirve para acceder de manera simple desde la instancia. Una vez definido el nombre
    # del equipo este no puede cambiarse.
    @property
    def name(self):
        return self.__name

    def is_connected(self):
        return self.link is not None

    def connect(self, port, link):
        self.link = link
        self.port = port

    def disconnect(self, port):
        self.link = None
        self.port = None

    def generate_packet(self, data, ip):
        return BasePacket(self.ip, ip, data)

    def send(self, data, ip):
        self.link.transmit(self.generate_packet(data, ip))

    # La función retorna el estado de la transacción, es decir si el paquete erá para el host o no.
    # También avisa si existe un error
    def received(self):
        if self.buffer:
            return self.buffer.pop()
        else:
            print('No hay datos')


class Link:
    def __init__(self, name, brand):
        self.name = name
        self.__brand = brand
        self.connected_devices = {}
    @property
    def brand(self):
        return self.__brand

    def connect(self, node_one: Node, node_two: Node) -> bool:
        self.connected_devices[node_one.ip] = node_one
        self.connected_devices[node_two.ip] = node_two
        node_one.connect(1,self)
        node_two.connect(2,self)
    
    def transmit(self, packet: BasePacket):
        self.connected_devices[packet.dst].buffer.append(packet)


```

Con nuestros objetos definidos ahora vamos a probar nuestro sistema. Primero definimos los dos HOST de

```python

>> a = Node('Nodo 1', 1)
>> b = Node('Nodo 2', 2)
>> lin = Link('Cable', 'UdeA')
>> lin.connect(a,b)
>> a.is_connected()
True
>> b.is_connected()
True
>> a.send('Mensaje', 2)
>> packet = b.received()
>> packet.data
'Mensaje'
>> packet.dst
2
>> packet.src
1


```

Actividad

1. Cree un nuevo Objeto SuperLink que herede sus caracteristicas de Lin y permita definir parametros como el tiempo
retardo con el cual llegan los paquetes, la velocidad del medio, entre otros que usted considere importante.

2. Modifique los Nodos para que su IP cumpla con las caracteristicas propias. Si la IP es incorrecta no permita conectar
al Link.

3. Si el host destino no está en la misma red descarte el paquete desde el host y debe aparecer un mensaje Host fuera
de red.


4 .Implementar un nuevo tipo de paquete llamado PersonalPacket, dicho paquete heredará de BasePacket y
 tendrá dos variables extra **danger** y **broken**,  el paquete al ser creado podrá verificar que la información 
 enviada sea de tipo string, si esto no sucede pondrá lavariable broken en True. En caso de que la variable sea string 
 verificar que no contenga las palabras 'isis', 'terrorismo', 'bomba'. En caso de que el paquete contenga dichas
  palabras pondrá la variable danger en True.


### Server y client en Python

El primer cliente a desarrollar en Python será un cliente web. Es decir, un cliente
que permita conectarse a un servidor web. Para recordar el modelo de operación
petición/respuesta asociado al servicio HTTP. Dado que ya realizó la guía anterior implemente un objeto cliente básico
que permita seleccionar la página a la cualquier hacer la petición y cuando tiempo de delay tenga la petición, también
adjunte una funcionalidad que permita guardar los mensajes obtenidos durante las peticiones y una última funcionalidad
para mostrar dichos mensajes.

```python
class MyClient:

    def __init__(self, ip, secure=False):
        #Implemente aquí su código (Configure el socket)
        self.ip = ip
        self.secure = secure
    def send_request(self):
        ## Guarde su la respuesta y realice la petición
        pass
    def print_requests(self):
        ## Imprima las respuestas optenidas
        pass
```

Ahora con la información básica vista en la guía anterior vamos a crear una clase llamada ServerDump,
dicha clase debe contener los elementos básicos que permiten la comunicación mediante sockets.

````python
from socket import AF_INET, SOCK_STREAM, socket


class ServerDump:

    request_queue_size = 5

    def __init__(self, server_address=("localhost", 4444), address_family=AF_INET, socket_type=SOCK_STREAM,
                 bind_and_activate=True):
        pass

````

Con la información de entrada de nuestra clase servidor inicializamos el socket.

````python
from socket import AF_INET, SOCK_STREAM, socket


class ServerDump:

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
````

Usamos las funciones de la clase socket para declarar algunos métodos propios de la funcionalidad de los socket como
bind, listen y close

````python
from socket import AF_INET, SOCK_STREAM, socket


class ServerDump:

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
````

Finalmente definimos la función connection_on donde se busca mantener un ciclo infinito para que socket pueda comunicarse
con sus clientes

````python
from socket import AF_INET, SOCK_STREAM, socket


class ServerDump:

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
````

Es de resaltar del código anterior que la función handle se encarga de gestionar la respuesta del servidor por lo tanto,
es lógica del usuario que desea que responda nuestro servidor.

El siguiente código es un ejemplo de uso donde el servidor se encarga de retornar el mismo texto enviado por el cliente
pero en mayusculas:

SERVIDOR
````python
from dump.sockets_dump import ServerDump


def handle(data: bytearray, conn):
    conn.sendall(data.upper())

s = ServerDump()
s.connection_on(handle)

````

CLIENTE
````python
from socket import *

if __name__ == "__main__":
    c = socket(AF_INET, SOCK_STREAM)
    c.connect(("localhost", 4444))
    while True:
        request = input("Request>	")
        c.sendall(request.encode())
        data = c.recv(1024)
        print(data)
        if request == "QUIT":
            break
    c.close()
````

Para la siguiente actividad proponga un cliente mediante POO e implemente la lógica necesaria para que el servidor
reciba un texto, cambie las vocales por números aleatorios y retorne la respuesta al cliente.


### Server GITA

Ahora usando la clase GitaServer del modulo server ubicado en el paquete gita_socket levante un servidor con el
siguiente código:

```python
from gita_socket import server
import pickle

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

class MyTCPHandler(server.BaseRequestHandler):

    def handle(self):
        # self.request is the TCP socket connected to the client
        data = self.request.recv(4096)
        # Este objeto contiene el paquete para gestionar la petición
        data_object = pickle.loads(data)
        print(data_object)
        

HOST, PORT = "localhost", 9999

# Cree el servidor, binding to localhost on port 9999
server = server.GitaServer((HOST, PORT), MyTCPHandler)

# Activate the server; this will keep running until you
# interrupt the program with Ctrl-C
server.serve_forever()

```

Lea el código de GitaServer, analice las funciones implementadas y su funcionamiento. Finalmente, en el método
handle de la clase MyTCPHandler defina la función de recepción de la petición y según la información interna que
contiene el paquete retorne:

Si el paquete es de tipo 1 -> En el campo response se debe devolver la hora actual del pais (En el campo data debe
indicar la abreviatura del país a buscar)

Si el paquete es de tipo 2 -> En el campo response se debe devolver con la suma indicada en el campo data

Nota: Si desea puede intentar crear un servicio de mensajería mediante polling, es decir, cuando un cliente envie un
mensaje el servidor lo debe guardar y esperar a que el cliente destino pregunte por sus mensajes. Intente usar una mini
base de datos tipo JSON.






