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

La programación orientada a objetos es una forma de programar que trata de encontrar una solución a estos problemas.
Introduce nuevos conceptos, que superan y amplían conceptos antiguos ya conocidos. Entre ellos destacan los siguientes:


**Clase:**  Definiciones de las propiedades y comportamiento de un tipo de objeto concreto. La instanciación es la 
lectura de estas definiciones y la creación de un objeto a partir de ellas.


**Herencia:** Es la facilidad mediante la cual la clase D hereda en ella cada uno de los atributos y operaciones de C,
como si esos atributos y operaciones hubiesen sido definidos por la misma D. Por lo tanto, puede usar los mismos métodos
y variables publicas declaradas en C. Los componentes registrados como "privados" (private) también se heredan, pero
como no pertenecen a la clase, se mantienen escondidos al programador y sólo pueden ser accedidos a través de otros
métodos públicos. Esto es así para mantener hegemónico el ideal de OOP.

**Objeto:** Entidad provista de un conjunto de propiedades o atributos (datos) y de comportamiento o funcionalidad
(métodos) los mismos que consecuentemente reaccionan a eventos. Se corresponde con los objetos reales del mundo que nos
rodea, o a objetos internos del sistema (del programa). Es una instancia a una clase.

**Método:** Algoritmo asociado a un objeto (o a una clase de objetos), cuya ejecución se desencadena tras la recepción
de un "mensaje". Desde el punto de vista del comportamiento, es lo que el objeto puede hacer. Un método puede producir
un cambio en las propiedades del objeto, o la generación de un "evento" con un nuevo mensaje para otro objeto del 
sistema.

**Evento:** Es un suceso en el sistema (tal como una interacción del usuario con la máquina, o un mensaje enviado
por un objeto). El sistema maneja el evento enviando el mensaje adecuado al objeto pertinente. También se puede
definir como evento, a la reacción que puede desencadenar un objeto, es decir la acción que genera.

**Mensaje:** Una comunicación dirigida a un objeto, que le ordena que ejecute uno de sus métodos con
ciertos parámetros asociados al evento que lo generó.

**Propiedad o atributo:** Contenedor de un tipo de datos asociados a un objeto (o a una clase de objetos), que hace los datos visibles desde fuera del objeto y esto se define como sus características predeterminadas, y cuyo valor puede ser alterado por la ejecución de algún método.

**Estado interno:** Es una variable que se declara privada, que puede ser únicamente accedida y alterada por un método del objeto, y que se utiliza para indicar distintas situaciones posibles para el objeto (o clase de objetos). No es visible al programador que maneja una instancia de la clase.

**Componentes de un objeto:** Atributos, identidad, relaciones y métodos.

**Identificación de un objeto:** Un objeto se representa por medio de una tabla o entidad que esté compuesta por sus atributos y funciones correspondientes.

En comparación con un lenguaje imperativo, una "variable", no es más que un contenedor interno del atributo del objeto
o de un estado interno, así como la "función" es un procedimiento interno del método del objeto.

#### Uso practico

Para recordar la programación orientada a objetos inicialmente vamos a crear una clase en Python y usar algunos de los
métodos especiales que nos brinda el lenguaje para manipular nuestros objetos.

- Vamos a main.py y creemos la siguiente clase:

```python
# Note que la primera letra de la clase definida tiene una letra mayuscula, esta convención para digitar el código se
# denomina CamelCase
class MyClass:
    def __init__(self):
        # Es importante no combinar inglés y español DENTRO del código, está regla no aplica para mensajes
        # ¿Qué debería hacer?
        print("Inicialzando - mensaje al usuario")
    def __del__(self):
        # pass es un indicador que permite a la función no realizar nada.
        pass
    def __str__(self):
        pass
    def __eq__(self, other):
        pass
    def __lt__(self, other):
        pass
    def __gt__(self, other):
        pass
    def __add__(self, a):
        pass

# Es importante dar nombres descriptivos a nuestras variables, el código en algún momento puede ser usuado por otros,
# incluso puede ser que nosotros mismo lo necesitemos en futuro y es importante poder entenderlo de nuevo.
instanceOfMyClass = MyClass()
```

- Vamos a la consola y ejecutamos la siguiente linea. En este caso python al crearse una instancia de la clase MyClass
llama al constructor el cual se identifica con la palabra clave init dentro de la clase.

```bash
    python main.py
```

NOTA: Si desea proponga una solución al problema planteado en MyClass, ¿Qué hacer cuando tengo mensajes en uno o más 
idiomas?, ¿Cómo evitar que el código se mezcle con mensajes indeseados?

- Ahora módifique la función **del**, escriba un mensaje cualquiera y ejecute de nuevo el script. En este caso, podríamos
suponer que la función del, se ejecuta una vez el código termine, pero no es así, la función del solo se ejecuta
cuando Python (su interprete) determina que el objeto no va a ser usado más, este proceso es automatico y en general
no depende de desarrollador.

- Agregue despues de la creación de la instancia la siguiente linea. En este caso la función del SI se ejecuta pues le
estamos indicando a Python explicitamente que no vamos a usar la instancia de nuevo.

```python
# del instanceOfMyClass
```

- Vamos a jugar un poco con operadores y privacidad.

Inicialmente modificamos la clase MyClass para asignar 0 a las variables __a y _a
```python
class MyClass:

    def __init__(self):
        self.__a = 10
        self._a = 5
    @property
    def a(self):
        return self.__a
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
    def __add__(self, a):
        if isinstance(a, MyClass):
            return self.__a + a.a
        else:
            return NotImplemented

instanceOfMyClass = MyClass()
instanceOfMyClassB = MyClass()

## print(instanceOfMyClass.__a)
## print(instanceOfMyClass._a)
## print(instanceOfMyClass.a)
## print(instanceOfMyClass)
## print(instanceOfMyClass + instanceOfMyClassB)

```

Ejecutemos el código anterior descomentando la primer linea, ¿Qué sucedió?¿Por qué piensa que esto ocurre?, después 
comente la primera y descomente la segunda, ¿Qué sucedio?¿En que se diferencia este caso con el anterior?, finalmente
ejecute con la penultima linea, ¿Qué hace el sistema en este caso?¿Qué valor retorno, compare con el primer caso?.

En Python la privacidad no fue definida desde su concepción, esta situación llevo al lenguaje a ciertos escenarios donde
tuvo que adaptarse mediante su evolución. Según los ejemplos anteriores podemos determinar que __ doble guión bajo
implica privacidad, implica que el campo no puede accederse desde el exterior, mientras que un solo guión bajo no
implica seguridad, sin embargo, el uso de la anotación property (@property) nos permite acceder a propiedades privadas
mediante una función intermediaria que vigila que el campo no sea sobrescrito sin permiso explicito.

Para la etapa final vamos a verificar la sobrecarga de operadores, para esto, primero analice el código de la función
add, luego quite el comentario de la última linea y verifique la suma resultante de los dos objetos sea 10, imagine las posibilidad,
al poder modificar el operador suma puede crear nuevos objetos con solo sumarlos. ¿Para que piensa que sirve el else 
usado en la función add?.

### ¿POO en redes? La comunicación más simple

"Imagine" que tiene frente a usted su computador, internamente el dispositivo cuenta con cientos de circuitos y 
funcionalidades que difícilmente podrían describirse con precisión, sin embargo, las abstracciones de que hemos ido
aprendiendo nos permiten describir solo un parte del sistema obviando los demás elementos que lo conforman. Teniendo
en cuenta lo anterior piense que elementos de red describen su equipo. Con esto en mente vamos a plantear la
comunicación más simple, dos equipos conectados mediantes un cable coaxial.

Una implementación sencilla de un host sería:

```python
class Host:

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self.__name = name
        self.ip = ip
        self.mask = mask
```

En la anterior implementación se define la ip, la mascara de red y un nombre para el equipo. Ahora definiremos una 
variable donde se registren las IP que conoce el host así:

```python
class Host:

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self.__name = name
        self.ip = ip
        self.mask = mask
        self.ip_table = [0xC0A80001, 0xC0A80002, 0xC0A80003, 0xC0A80004]
        self.ip_table.remove(ip)
```

Pregunta: ¿Cuál es el objetivo de la  ultima linea?

Nuestro DumpHost se encuentra defino... pero ¿Qué hace nuestro HOST?, actualmente nada, sin embargo es nuestra tarea
programar las dos funcionalidades más básicas de un host, enviar y recibir.

```python
class Host:

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self.__name = name
        self.ip = ip
        self.mask = mask
        self.ip_table = [0xC0A80001, 0xC0A80002, 0xC0A80003, 0xC0A80004]
        self.ip_table.remove(ip)
    
    def send(self, data):
        pass
    
    def received(self, packet):
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

    @data.setter
    def data(self, data):
        self.__data = data
```

Ahora modificamos nuestra clase Host para que pueda enviar y recibir paquetes.

```python
from dump.packet import BasePacket
from random import randint

class Host:

    def __init__(self, name, ip=0xC0A80001, mask=0xFFFFFF00):
        self.__name = name
        self.ip = ip
        self.mask = mask
        self.ip_table = [0xC0A80001, 0xC0A80002, 0xC0A80003, 0xC0A80004]
        self.ip_table.remove(ip)

    # Anotación propiedad que sirve para acceder de manera simple desde la instancia. Una vez definido el nombre
    # del equipo este no puede cambiarse.
    @property
    def name(self):
        return self.__name

    def generate_packet(self, data):
        return BasePacket(self.ip, self.ip_table[randint(0, 2)], data)

    def generate_packet_ip(self, data, ip):
        return BasePacket(self.ip, ip, data)

    def send(self, data, ip=None):
        if ip is None:
            return self.generate_packet(data)
        else:
            return self.generate_packet_ip(data, ip)

    # La función retorna el estado de la transacción, es decir si el paquete erá para el host o no.
    # También avisa si existe un error
    def received(self, packet):
        # Verificamos que la variable de entrada sea una instancia de BasePacket
        if isinstance(packet, BasePacket):
            # Verificamos que el paquete sea para nosotros
            if packet.dst == self.ip:
                print("Paquete recibido. " + str(self.ip))
                print(packet.data)
                return True
            else:
                print("Paquete rechazado. Mi ip es " + str(self.ip) + ' ,el paquete es para ' + str(packet.dst))
                return False
        else:
            print("Error el paquete está en mal estado")
            return False
```

Con nuestros objetos definidos ahora en el main.py vamos a probar nuestro sistema. Primero definimos los dos HOST de

```python
from dump.host import Host


if __name__ == "__main__":
    h1 = Host('PC Gamer', 0xC0A80001)
    h2 = Host('Laptop', 0xC0A80002)
```

Ahora vamos a crear un loop que nos permita enviar texto entre los dos host de manera recurrente, para esto creamos
los mensajes a enviar y un estado que nos permita reconocer el punto donde se encuentra el sistema.

```python
from dump.host import Host

state = 1

Messages = ['Mensaje 1!', 'Mensaje 2!', 'Mensaje 3!', 'Mensaje 4!', 'Mensaje 5!', 'Mensaje 6!', 'Mensaje 7!', 'Mensaje 8!']

if __name__ == "__main__":
    h1 = Host('PC Gamer', 0xC0A80001)
    h2 = Host('Laptop', 0xC0A80002)
```

En el loop incluiremos la función de envío y recepción para que los dos host se envien el paquete

```python
from dump.host import Host

state = 1

Messages = ['Mensaje 1!', 'Mensaje 2!', 'Mensaje 3!', 'Mensaje 4!', 'Mensaje 5!', 'Mensaje 6!', 'Mensaje 7!',
            'Mensaje 8!']


if __name__ == "__main__":
    # Corresponde a la IP 192.19.0.1 en hexadecimal
    h1 = Host('PC Gamer', 0xC0A80001)
    # Corresponde a la IP 192.19.0.2 en hexadecimal
    h2 = Host('Laptop', 0xC0A80002)
    for i in range(4):
        h1.send(Messages[state], 0xC0A80002)
        h2.received()
        state += 1


```

En la lógica anterior el paquete es enviado por un host y recibido por el otro (conexión directa), el loop se repite
durante 8 veces y se genera un paquete con IP destino aleatoria (obtenida de la tabla definida al inicio), en algunos
casos el paquete le pertenece al host y es recibido, en otros simplemente es rechazado.

Actividad opcional: Realice una implementación Plus del sistema propuesto pero ahora con procesos, para esto puede 
ayudarse de la librería https://docs.python.org/2/library/multiprocessing.html, en este sistema el objetivo es
leer los paquetes una vez sean enviados sin necesidad de hacer un loop.

Con su primer de sistema de comunicación finalizado ahora va a implementar un nuevo tipo de paquete llamado
PersonalPacket, dicho paquete heredará de BasePacket y tendrá dos variables extra **danger** y **broken**, 
el paquete al ser creado podrá verificar que la información enviada sea de tipo string, si esto no sucede pondrá la
variable broken en True. En caso de que la variable sea string verificar que no contenga las palabras 'isis', 
'terrorismo', 'bomba'. En caso de que el paquete contenga dichas palabras pondrá la variable danger en True.

### Mi amigo el swicth

Nuestra red va a crecer y necesitamos un sistema que permita redirigir los paquetes según la ip destino, para esto
crearemos la clase router. En esta clase necesitamos definir las características mínimas del dispositivo como marca,
nombre del equipo, entre otros. Una implementetación básica es:

````python
class Switch:
    table = {}

    def __init__(self, name, brand, hosts):
        self.name = name
        self.__brand = brand
        self.hosts = [self.def_host(host) for host in hosts]

    def def_host(self, host):
        self.table[host.ip] = host

    def received_packet(self, packet):
        self.table[packet.dst].received(packet)

````

En esta clase se almacenan los hosts, estos son un diccionario donde la IP está relacionada con la referencia del 
objeto que representa el host. ¿Qué otra manera se te ocurre para interconectar los host con el router SIN cambiar las
clases antiguas.

Nota: Es importante aprender a reusar código sin causar breaking changes, pues el propósito de POO es extender poco a
poco las funcionalidades de un código y no reescribirlo. Piensa bien antes de definir procesos o algoritmos en como te
afectará en el futuro las decisiones de diseño que tomes.

Ahora en el host probamos nuestro nuevo objeto

````python
from dump.host import Host
from router.Switch import Switch

state = 1

Messages = ['Mensaje 1!', 'Mensaje 2!', 'Mensaje 3!', 'Mensaje 4!', 'Mensaje 5!', 'Mensaje 6!', 'Mensaje 7!', 'Mensaje 8!']


def next_message(received, st):
    if received:
        st += 1


if __name__ == "__main__":
    h1 = Host('PC Gamer', 0xC0A80001)
    h2 = Host('Laptop', 0xC0A80002)
    h3 = Host('Laptop', 0xC0A80003)
    hosts = [h1, h2, h3]
    # Creación del objeto router
    r = Switch('My router', 'CISCO', hosts)

    # Envío del paquete
    packet = h1.send('Hola!', 0xC0A80002)
    print("Paquete enviado para " + str(packet.dst) )
    # Recepción y envío a su correspondiente destinatario
    r.received_packet(packet)

````
La respuesta del código anterior debe ser similar a:

````bash
PyDev console: starting.
Python 3.7.6 (default, Jan  8 2020, 20:23:39) [MSC v.1916 64 bit (AMD64)] on win32
runfile('main.py', wdir='Sockets')
Paquete enviado para 3232235522
Recibido en 3232235522
Datos:Hola!
````

Ahora es tu turno debes recrear el enlace pero con muchas más funcionalidades. Los requisitos funcionales son los
siguientes:

- El paquete no debe aparecer en el main.py, es decir, el host debe enviar directamente el mensaje al objeto router.
- Se debe permitir al usuario ingresar el host origen y el host destino, también el contenido del mensaje. OJO: Solo
se debe poder enviar texto.
- Todos los paquetes dirigidos para el host 3 deben ser descartados por el router. Esta funcionalidad debe implementarse
en una clase que herede del Switch propuesto en esta guía.


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






