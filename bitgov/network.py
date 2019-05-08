from socket import AF_INET, SOCK_STREAM
from bitgov.nodes import get_nodes
from bitgov.protocol import server_config, client_broadcast
# from bitgov.protocol.utilities import find_available_port

IPv4 = AF_INET
TCP = SOCK_STREAM

def connect():
    host = "0.0.0.0"
    port = 4242
    print("\n\033[1;37mAttempting to connect with the BitGov network.\033[0;0m 📡\n")
    server = server_config(IPv4, TCP, host, port)
    get_nodes(server, port)

def broadcast(data=None, host="0.0.0.0"):
    port = 4242
    client_broadcast(IPv4, TCP, host, port, data)
