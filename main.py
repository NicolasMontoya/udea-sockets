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
