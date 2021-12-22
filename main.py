# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PySide6 import QtWidgets
import PySide6
from PySide6 import QtCore
from PySide6.QtGui import QShowEvent

from PySide6.QtWidgets import QApplication, QDialog, QMainWindow, QMessageBox
from PySide6.QtCore import QFile
from PySide6.QtUiTools import QUiLoader
# from Ui_mainform import Ui_MainForm
# from Ui_settingwindow import Ui_SettingWindow
from Ui_MainWindow import Ui_MainWindow

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        # self.load_ui()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
    def closeWindow(self):
        if QMessageBox.warning(self,"Close","Are you sure?",QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.close()
    # def openSettingForm(self):
        
    #     # self.window = QtWidgets.QMainWindow()
    #     # self.ui = Ui_FormSetting()
    #     # self.ui.setupUi(self.window)
    #     # self.window.show()
    #     settingWindow = QMainWindow(parent=self)
    #     settingWindow.ui  = Ui_SettingWindow()
    #     settingWindow.ui.setupUi(settingWindow)
    #     # settingWindow.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
    #     settingWindow.showNormal()
        

    # def load_ui(self):
    #     loader = QUiLoader()
    #     path = os.fspath(Path(__file__).resolve().parent / "mainform.ui")
    #     ui_file = QFile(path)
    #     ui_file.open(QFile.ReadOnly)
    #     loader.load(ui_file, self)
    #     ui_file.close()
    


if __name__ == "__main__":
    # app = QApplication([])
    app = QApplication(sys.argv)
    widget = Main()
    
    # center screen
    center = QApplication.primaryScreen().geometry().center()    
    widget.show()
    widget.move(center - widget.frameGeometry().center())
    
    sys.exit(app.exec_())
