#
# CAN受信リスナ
#
import can

class Listener(can.Listener):
    def __init__(self, callback = None):
        self.callback = callback

    # @override CANコールバック関数(can.Listenter)
    def on_message_received(self, msg):
        self.callback(msg)
