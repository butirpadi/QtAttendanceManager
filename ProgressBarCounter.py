import time
from PySide6 import QtCore


class ProgressBarCounter(QtCore.QThread):

    any_signal = QtCore.Signal(int)

    def __init__(self, parent=None, index=0, progressBar=None):
        super(ProgressBarCounter, self).__init__(parent)
        self.index = index
        self.is_running = True
        self.progressBar = progressBar

    def run(self):
        print('Starting thread...', self.index)
        cnt=0
        max = self.progressBar.maximum()
        for i in range(max):
            if cnt < max:
                cnt += 1
                time.sleep(0.01)
                self.any_signal.emit(cnt) 

    def stop(self):
        self.is_running = False
        print('Stopping thread...', self.index)
        self.terminate()
