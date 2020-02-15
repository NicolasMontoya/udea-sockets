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
