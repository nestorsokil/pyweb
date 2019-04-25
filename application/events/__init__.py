from thrift.transport import TSocket
from thrift.protocol import TCompactProtocol
from accumulo import AccumuloProxy
from accumulo.ttypes import TTransport

# just for testing purposes
if __name__ == '__main__':
    transport_socket = TSocket.TSocket('localhost', 42424)
    connection = TTransport.TFramedTransport(transport_socket)
    protocol = TCompactProtocol.TCompactProtocol(connection)
    accumulo_client = AccumuloProxy.Client(protocol)

    connection.open()

    print('Connected!')
