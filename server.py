from threading import Thread
import socket
from encrypt import *
from decrypt import *

class SendingThread(Thread):
    def __init__(self, mySocket):
        Thread.__init__(self)
        self.mySocket = mySocket

    def run(self):
        # write code to send data continuously
        while True:
            data = input()
            data=start_encrypt(data)
            self.mySocket.send(bytes(data, 'utf-8'))


class ReceivingThread(Thread):
    def __init__(self, mySocket):
        Thread.__init__(self)
        self.mySocket = mySocket

    def run(self):
        # write code to receive data continuously
        while True:
            msg = self.mySocket.recv(1024)
            msg=start_decrypt(msg)
            print(msg.decode('utf-8'))


# create a socket object
s = socket.socket(
    socket.AF_INET, # internet address family => IP v4
    socket.SOCK_STREAM # TCP
)
# bind socket with a port number
s.bind(('192.168.1.15', 2010))
# keep System_1 in listening mode
s.listen()
# accept the incoming connection request
mySocket, address = s.accept()
# create a thread to send data
sendThread = SendingThread(mySocket)
# create an another to receive data
receiveThread = ReceivingThread(mySocket)
# start both threads
sendThread.start()
receiveThread.start()