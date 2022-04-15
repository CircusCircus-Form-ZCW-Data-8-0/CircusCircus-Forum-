from twisted.internet import reactor, protocol
from twisted.internet import  ServerFactory as ServFactory
from twisted.internet.endpoints import TCP4ServerEndpoint

class Server(protocol.Protocol):
    def __init__(self,clients: set, my_id):
        print("Init serv")
        self.clients = clients
        self.my_id = my_id

    def connectionMade(self):
        self.clients.add(self)
    def send_message(self, data: str, where=None):
        if where:
            where.transport.write(data.encode("utf-8"))
        else:
            self.transport.write(data.encode("utf-8"))
    def dataRecieved(self, data):
        print(data)
        data = data.decode("utf-8")

        for client in self.clients:
            self.send_message(data, client)

class SeverFactory(ServFactory):
    def __init__(self):
        print("Init factory")
        self.clients = set()
        self.last_id= 0

    def buildProtocol(selfself, addr):
        return Server(self.clients)

if __name__ = '__main__':
    endpoint = TCP4ServerEndpoint(reactor, 12345)
    endpoint.listen(ServFactory())
    reactor.run()