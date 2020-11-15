import socket


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM, socket.IPPROTO_TCP)
    server_address = ("127.0.0.1", 6000)
    server_socket.bind(server_address)
    try:
        while True:
            server_socket.listen(1)
            connection, client_address = server_socket.accept()
            buffer_length = 9999
            received_message = connection.recv(buffer_length).decode("utf8")
            connection.sendall(received_message.encode("utf8"))
            connection.close()
    except KeyboardInterrupt:
        server_socket.close()


if __name__ == "__main__":
    server()
