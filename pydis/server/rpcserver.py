from pydis.server import tcpserver
from pydis.server import jsondecode
from pydis.server import rpcstub


class RPCServer(tcpserver.Server, jsondecode.JSONRPC, rpcstub.RPCStub):
    def __init__(self):
        super(RPCServer, self).__init__()

    def loop(self):
        self.bind_listen(6789)
        while True:
            self.accept_receive_close()

    def on_msg(self, data):
        self.from_data(data)
        self.call_method()
