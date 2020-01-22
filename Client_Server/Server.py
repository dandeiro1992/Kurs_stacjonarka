import sys
from time import sleep
import hashlib
from PodSixNet.Channel import Channel
from PodSixNet.Server import Server


class ClientChannel(Channel):

    def Network(self, data):
        print("damian", data)

    def Network_myaction(self, data):
        # print("myaction:", data)
        if data["myaction"] == "damian":
            print("gnojdas")
        else:
            print("cos innego")
        print(data['myaction'])

    def Network_hash(self, data):
        m = hashlib.sha256()
        print(data["value"])
        m.update(data["value"].encode("utf-8"))
        print(m.hexdigest())


class MyServer(Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print('new connection:', channel)

    def Launch(self):
        while True:
            self.Pump()
            sleep(0.0001)


print("Server rozpoczyna prace\n")
# get command line argument of server, port
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        s = MyServer(localaddr=(host, int(port)))
        s.Launch()
