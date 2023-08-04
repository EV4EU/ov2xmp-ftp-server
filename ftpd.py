import json
from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

FTP_ROOT = '/files'


if __name__ == '__main__':

    f = open('config.json')
    config = json.load(f)

    user = config['username']
    password = config['password']
    
    authorizer = DummyAuthorizer()
    authorizer.add_user(user, password, FTP_ROOT, perm="elradfmw")

    handler = FTPHandler
    handler.authorizer = authorizer
    handler.permit_foreign_addresses = True
    
    passive_ports = [49152, 49155]
    assert len(passive_ports) == 2
    handler.passive_ports = range(passive_ports[0], passive_ports[1])

    server = FTPServer(('0.0.0.0', 21), handler)
    server.serve_forever()
