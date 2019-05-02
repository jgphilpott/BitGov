import socket
import threading

def server_config(HOST, PORT, IPv, PROTOCOL, BUFF):

    print("\033[0;33mConfiguring the server.. \033[0;0m", end="")
    try:

        with socket.socket(IPv, PROTOCOL) as sock:

            sock.bind((HOST, PORT))
            sock.listen()
            print("\033[1;32mSuccess!\033[0;0m")

            while True:

                connection, address = sock.accept()
                connection.setblocking(False)

                with connection:

                    print("Connected with:", address)
                    request = b""

                    while True:
                        try:
                            fragment = connection.recv(BUFF)
                        except:
                            break
                        request += fragment

                    print("Received:", request)
                    connection.sendall(request)

    except:
        print("\033[0;31mError!\033[0;0m ⛔")
        return None
