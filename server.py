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
            request = connection.recv(1024).decode("utf-8")
            response = self.handler_func(address, request)
            connection.sendall(response.encode())
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
    def handler(address : tuple, data : str):
        """ The handler function takes two required arguments: address (ip and port from which the request was sent) and data (decoded request).
            The handler function returns the response as a bytecode. """
        return "<p>Test</p>"   # or b"..."
