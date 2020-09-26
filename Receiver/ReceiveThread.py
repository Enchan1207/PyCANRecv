#
#  CAN受信部
#
from CANClient import Client, Listener
import threading, queue

class ReceiveThread(threading.Thread):

    def __init__(self, recvQueue, channel = None):
        super(ReceiveThread, self).__init__()

        self.client = Client(channel or 'vcan1', 500000, callback=self.onReceive)
        self.recvQueue = recvQueue

    def run(self):
        pass

    def onReceive(self, msg):
        self.recvQueue.put(msg)
