import PodSixNet.Channel
import PodSixNet.Server
from time import sleep


class ClientChannel(PodSixNet.Channel.Channel):
    def Network(self, data):
        print(data)


class BoxesServer(PodSixNet.Server.Server):
    channelClass = ClientChannel

    def Connected(self, channel, addr):
        print('new connection:', channel)


print("STARTING SERVER ON LOCALHOST")
# try:
address = input("Host:Port (localhost:8000): ")
if not address:
    host, port = "localhost", 8000
else:
    host, port = address.split(":")
boxesServe = BoxesServer()
while True:
    boxesServe.Pump()
    sleep(0.01)
