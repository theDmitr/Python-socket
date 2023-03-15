# Server

Implements a socket for accepting and processing HTTP requests.

## Tutorial

An example of working with an object of the Server class:

```python
from server import Server

def handler_func(address, data):
    return b"<p>Hello, World!</p>"

# Takes two required arguments: host (address) and port.
server = Server("localhost", 80).set_handler_func(handler_func)
server.run_listener()
```

### Methods

| Method | Assignment | Use |
| - | - | - |
| run_listener | Starts a request listener, processes them, and recursively does it again and again. | server.run_listener() |
| handle | This method receives the request and passes it to the handler function. | server.handle(connection : socket, address : tuple) |
| set_handler_func(self, handler_func) | Sets the current handler function to be called when a request is encountered. Returns the current object. | server.set_handler_func(handler_func) |
| handler | The handler function takes two required arguments: address (ip and port from which the request was sent) and data (decoded request). The handler function returns the response as a bytecode. | ```server.handler(address : tuple, data : str))``` |
