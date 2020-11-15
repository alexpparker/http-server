import socket
import sys


def client(message: str):
    addr_info = socket.getaddrinfo("127.0.0.1", 6000)
    stream_info = [socket_tup for socket_tup in addr_info if socket_tup[1] == socket.SOCK_STREAM][0]
    client_socket = socket.socket(*stream_info[:3])
    client_socket.connect(stream_info[-1])
    client_socket.sendall(message.encode("utf8"))
    buffer_length = 9999
    print(client_socket.recv(buffer_length).decode("utf8"))
    client_socket.close()


if __name__ == "__main__":
    client(sys.argv[1])
