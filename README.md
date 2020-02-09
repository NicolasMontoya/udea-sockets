## Practica de Sockets con POO

... teoria  sobre POO y sockets

###Introducción a POO

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
        pass
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
add, luego descomente la última linea y verifique la suma resultante de los dos objetos sea 10, imagine las posibilidad,
al poder modificar el operador suma puede crear nuevos objetos con solo sumarlos. ¿Para que piensa que sirve el else 
usado en la función add?.

### Cliente Socket

El primer cliente a desarrollar en Python será un cliente web. Es decir, un cliente
que permita conectarse a un servidor web. Para recordar el modelo de operación
petición/respuesta asociado al servicio HTTP. Dado que ya realizó la gúia anterior implemente un objeto cliente básico
que permita seleccionar la página a la cual quier hacer la petición y cuando tiempo de delay tenga la petición, también
adjunte una funcionalidad que permita guardar los mensajes obtenidos durante las peticiones y una última funcionalidad
para mostrar dichos mensajes.

```python
class MyClient:

    def __init__(self, ip, secure=False):
        #Implemente aquí su código (Configure el socket)
        pass
    def sendRequest(self):
        ## Guarde su la respuesta y realice la petición
    def printRequests(self):
        ## Imprima las respuestas optenidas
        pass
```

Ahora usando la clase GitaServer del modulo server ubicado en el paquete gita_socket levante un servidor:

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






