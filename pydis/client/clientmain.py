from pydis.client import rpcclient

while True:
    raw = input("Please enter your command: ")
    commands = raw.split(' ')
    command, key, value = commands
    print("command: {} \n {}: {}".format(command, key, value))
# c = rpcclient.RPCClient()
# c.connect('127.0.0.1', 6789)
# c.SET("test", 123)