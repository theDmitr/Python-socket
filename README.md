# Server

Implements a socket for accepting and processing HTTP requests.

## Tutorial

An example of working with an object of the Server class:

```python
from server import Server

# Takes two required arguments: host (address) and port.
server = Server("localhost", 8080)
server.run_listener()
```

### Methods

| Method | Assignment | Use |
| - | - | - |
| run_listener | Starts a request listener, processes them, and recursively does it again and again. | ```server.run_listener()``` |
| handle | This method receives the request and passes it to the handler function. | ```server.handle(connection : socket, address : tuple)``` |
| set_handler_func(self, handler_func) | Sets the current handler function to be called when a request is encountered. Returns the current object. | ```server.set_handler_func(handler_func)``` |
| handler | The handler function takes three required arguments: connection, address (ip and port from which the request was sent) and data (decoded request). | ```server.handler(connection : socket, address : tuple, request : str))``` |
