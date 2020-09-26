#
# CANクライアント
#
from CANClient.Listener import Listener
import can

try:
    import RPi.GPIO as GPIO
except ImportError:
    pass

class Client():
    def __init__(self, ch, baudRate, intPin = 25, filter = None, callback = None):
        # GPIO初期設定
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(intPin, GPIO.IN)

        # CANインタフェース初期化
        self.CANBus = can.interface.Bus(channel = ch, bustype = 'socketcan_native', bitrate = baudRate, canfilters = filter)

        # リスナ設定
        self.listener = Listener(callback=callback)
        can.Notifier(self.CANBus, [self.listener, ])

    # データを送りつける
    def sendFrame(self, id, data = [0x00, ]):
        message = can.Message(data = data, arbitration_id = id, )

        self.CANBus.send(message)
