from pydis.datastruct.sds import SdsImp


class RPCStub(object):
    def __init__(self):
        pass

    def SET(self, key, value):
        self
        print("{}: {}".format(key, value))
