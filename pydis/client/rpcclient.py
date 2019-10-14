from pydis.client import rpcstub, client


class RPCClient(client.Client, rpcstub.RPCStub):
    pass