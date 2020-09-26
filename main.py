#
# CAN受信スレッド example
#
from Receiver import ReceiveThread
import threading, queue

def main():
    recvQueue = queue.Queue()
    rct = ReceiveThread(recvQueue = recvQueue, channel = 'vcan1')
    rct.setDaemon(True)
    rct.start()
    print("Receive-thread Start...")

    # 適度にdeQueueしてメッセージをダンプ
    endReq = False
    try:
        while not endReq:
            try:
                item = recvQueue.get(timeout = 10)
                print("ID: {0} Data: {1}".format(item.arbitration_id, item.data))
            except queue.Empty:
                print("--- CAN Receive Timeout! ---")
                endReq = True
                continue
            
    except KeyboardInterrupt:
        print("Interrupt")

if __name__ == "__main__":
    main()
