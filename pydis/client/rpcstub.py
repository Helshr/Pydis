import json


class RPCStub(object):
    def __getattr__(self, item):
        def _(*args, **kwargs):
            d = {'method_name': item, 'method_args': args, 'method_kwargs': kwargs}
            self.send(json.dumps(d).encode('utf-8'))

        setattr(self, item, _)
        return _
