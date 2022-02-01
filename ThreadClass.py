import time
from PySide6 import QtCore


class ThreadClass(QtCore.QThread):

    any_signal = QtCore.Signal()

    def __init__(self, parent=None, index=0):
        super(ThreadClass, self).__init__(parent)
        self.index = index
        self.is_running = True

    def run(self):
        print('Starting thread...', self.index)
        # if self.index == 999:
        #     cnt=0
        #     # while (True):
        #     #     cnt+=1
        #     #     if cnt==99:
        #     #         cnt=0
        #     #         time.sleep(0.01)
                
        #     #     self.any_signal.emit(cnt)
        # else:
        self.any_signal.emit()

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()
