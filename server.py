import socket

class Server:
    """ Implements a socket for accepting and processing HTTP requests. """
    def __init__(self, host : str, port : int) -> None:
        """ Takes two required arguments: host (address) and port. """
        self.sock = socket.socket()
        self.sock.bind((host, port))
        self.sock.listen(2)
        self.handler_func = Server.handler

    def run_listener(self) -> None:
        """ Starts a request listener, processes them, and recursively does it again and again. """
        connection, address = self.sock.accept()
        self.handle(connection, address)
        self.run_listener()
    
    def handle(self, connection : socket, address : tuple) -> None:
        """ This method receives the request and passes it to the handler function. """
        print("Connection from: " + str(address))
        while True:
            data = connection.recv(1024).decode()
            if not data: break
            connection.send(self.handler_func(address, data))
        connection.close()
    
    def set_handler_func(self, handler_func):
        """ Sets the current handler function to be called when a request is encountered.
            Returns the current object. """
        self.handler_func = handler_func
        return self
    
    @staticmethod
    def handler(address : tuple, data : str) -> bytes:
        """ The handler function takes two required arguments: address (ip and port from which the request was sent) and data (decoded request).
            The handler function returns the response as a bytecode. """
        return "<p>Test</p>".encode()   # or b"..."