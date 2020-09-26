#
#  CAN受信部
#
from CANClient import Client, Listener
import threading, queue

class Receiver(threading.Thread):

    def __init__(self, client = None, queue = None):
        self.client = client or Client('vcan1', 500000, callback=self.onReceive)
        self.queue = queue.Queue()

    def run(self):
        pass

    def onReceive(self, msg):
        self.queue.put(msg)
