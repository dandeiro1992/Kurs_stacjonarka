import sys
from _thread import start_new_thread
from time import sleep

from PodSixNet.Connection import ConnectionListener
from PodSixNet.Connection import connection


class MyNetworkListener(ConnectionListener):

    def __init__(self, host, port):
        self.Connect((host, port))
        t = start_new_thread(self.InputLoop, ())

    def Network(self, data):
        print('network data:', data)

    def Network_connected(self, data):
        print("connected to the server")

    def Network_error(self, data):
        print("error:", data['error'][1])

    def Network_disconnected(self, data):
        print("disconnected from the server")

    def Network_myaction(data):
        print("myaction:", data)

    def Network_hash(data):
        print("action")
    def Loop(self):
        connection.Pump()
        self.Pump()

    def InputLoop(self):
        # horrid threaded input loop
        # continually reads from stdin and sends whatever is typed to the server
        while 1:
            hash = input()
            print("hash:",hash)
            if hash == "hash":
                connection.Send({"action": "hash", "value": sys.stdin.readline().rstrip("\n")})
            else:
                connection.Send({"action": "myaction", "myaction": sys.stdin.readline().rstrip("\n")})


print("Rozpoczynam poloiczenie \n")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage:", sys.argv[0], "host:port")
        print("e.g.", sys.argv[0], "localhost:31425")
    else:
        host, port = sys.argv[1].split(":")
        c = MyNetworkListener(host, int(port))
        while 1:
            c.Loop()
            sleep(0.001)
