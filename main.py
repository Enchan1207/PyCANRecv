#
# CAN受信スレッド
#
from Receiver import Receiver
import threading, queue

def main():
    recvQueue = queue.Queue()
    rct = Receiver(queue = recvQueue)
    rct.setDaemon(True)
    rct.start()

    print("Start...")

    endReq = False
    try:
        while not endReq:
            item = recvQueue.get(timeout = 10)
            if item is None:
                endReq = True
                continue

            print(item)
            
    except KeyboardInterrupt:
        print("Interrupt")

if __name__ == "__main__":
    main()
