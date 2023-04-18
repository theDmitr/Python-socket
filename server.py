import socket, ssl

class Server:
    """ Implements a socket for accepting and processing HTTP requests. """
    def __init__(self, host : str, port : int) -> None:
        """ Takes two required arguments: host (address) and port. """
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((host, port))
        self.sock.listen(1)
        self.handler_func = Server.handler

    def run_listener(self) -> None:
        """ Starts a request listener, processes them, and recursively does it again and again. """
        connection, address = self.sock.accept()
        self.handle(connection, address)
        self.run_listener()
    
    def handle(self, connection : socket, address : tuple) -> None:
        """ This method receives the request and passes it to the handler function. """
        print("Request received from " + str(address))
        try:
            self.handler_func(connection, address, connection.recv(4096).decode())
        except UnicodeDecodeError:
            print("[ERROR] UnicodeDecodeError")
        finally:
            connection.close()
    
    def set_handler_func(self, handler_func):
        """ Sets the current handler function to be called when a request is encountered.
            Returns the current object. """
        self.handler_func = handler_func
        return self
    
    @staticmethod
    def handler(connection : socket, address : tuple, request : str) -> None:
        response = "<p>Test</p>"
        connection.sendall(response.encode())
