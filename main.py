# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from typing import final
from PySide6 import QtWidgets
import PySide6
from PySide6 import QtCore
from PySide6.QtGui import QShowEvent

from PySide6.QtWidgets import QApplication,  QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QFile
from OdooConnection import OdooConnection
from Ui_MainWindow import Ui_MainWindow
import sqlite3
from pprint import pprint
import requests


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        # self.load_ui()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # open setting
        # -----------------------------------------------
        conn = sqlite3.connect("my.sqlite")
        cur = conn.cursor()

        # create table setting
        cur.execute("CREATE TABLE IF NOT EXISTS[setting] ([id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,[server_url] VARCHAR(1024) NULL,[database] VARCHAR(100) NULL,[username] VARCHAR(100) NULL,[password] VARCHAR(100) NULL)")
        # crewate table machine
        cur.execute("CREATE TABLE IF NOT EXISTS[zkmachine] ([id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,[name] VARCHAR(100) NULL,[address] VARCHAR(500) NULL,[port] VARCHAR(100) NULL,[machine_id] VARCHAR(100) NULL)")

        # open setting to form
        cur.execute("select id,server_url,database,username,password from setting")
        rows = cur.fetchall()
        cur.close()

        if rows:
            dbsetting = rows[0]
            self.ui.tbServer.setText(str(dbsetting[1]))
            self.ui.tbDatabase.setText(str(dbsetting[2]))
            self.ui.tbUsername.setText(str(dbsetting[3]))
            self.ui.tbPassword.setText(str(dbsetting[4]))
        
        # open machine data
        cur = conn.cursor()
        cur.execute("SELECT id,name,address,port,machine_id from zkmachine")
        machineRows = cur.fetchall()
        print('Get Data Machine')
        print('------------------------------')
        # pprint(machineRows)
        cur.close()
        
        if machineRows:
            rowidx = 0            
            self.ui.machineTable.setRowCount(len(machineRows))
            
            for machine in machineRows:
                self.ui.machineTable.setItem(rowidx,0,QtWidgets.QTableWidgetItem(str(machine[1])))
                self.ui.machineTable.setItem(rowidx,1,QtWidgets.QTableWidgetItem(str(machine[2])))
                self.ui.machineTable.setItem(rowidx,2,QtWidgets.QTableWidgetItem(str(machine[3])))
                
                rowidx+=1

        conn.close()
        # ---------------------------------------------

    def clearInputan(self):
        self.ui.tbMachineAddress.setText("")
        self.ui.tbMachineName.setText("")
        self.ui.tbMachinePort.setText("")

    def newMachine(self):
        # clear inputan
        self.clearInputan()
        
        # disable table widget
        self.ui.machineTable.setEnabled(False)
        
        # set enable inputan
        self.ui.gbMachineSetting.setEnabled(True)
        self.ui.tbMachineName.setFocus()
        
    def editMachine(self):
        print('edit Machine')
        
    def deleteMachine(self):
        print('delete Machine')
        
    def syncAttendance(self):
        print('synch Machine')

    def machineSelected(self):
        print('Selected Items : ')
        self.ui.tbMachineName.setText(self.ui.machineTable.selectedItems()[0].text())
        self.ui.tbMachineAddress.setText(self.ui.machineTable.selectedItems()[1].text())
        self.ui.tbMachinePort.setText(self.ui.machineTable.selectedItems()[2].text())
    
    def testConnection(self):
        try:
            odooCon = OdooConnection(self.ui.tbUsername.text(),self.ui.tbPassword.text(),self.ui.tbDatabase.text(),self.ui.tbServer.text())
            session_id = odooCon.getSessionId()
            if session_id:
                QMessageBox.warning(self, "Connection Successful", "Connection successful. \n Your session id : " + session_id, QMessageBox.Ok)    
        except Exception as e:
            QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)
        
        # try:
        #     odoo_url = str(self.ui.tbServer.text()) + "/web/session/authenticate"
        #     headers = {
        #         "Content-type": "application/json",
        #         "Accept": "application/json"
        #         }      
        #     data = {
        #         "jsonrpc": "2.0",
        #         "method": "call",
        #         "id": 1,
        #         "params": {
        #             "login": self.ui.tbUsername.text(),
        #             "password": self.ui.tbPassword.text(),
        #             "db": self.ui.tbDatabase.text(),
        #             "context": {}
        #         }
        #     }
        #     pprint(data)
        #     req = requests.post(url=odoo_url, json=data, headers=headers)

        #     print('First Result : ')
        #     print('---------------------------------------')
        #     pprint(req.headers)
        #     print(req.text)
        #     print('Status Code : ' + str(req.status_code))

        #     res_json = req.json()
            
        #     if "error" in res_json:
        #         QMessageBox.warning(self,"Error Connection","Connection Error, please check your credentials.",QMessageBox.Ok)
        #         return
            
        #     if req.status_code == 200:
        #         QMessageBox.information(self, "Connection", "------------ Connection Success ------------", QMessageBox.Ok)

        # except Exception as e:
        #     QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)

    def closeWindow(self):
        if QMessageBox.warning(self, "Close", "Are you sure?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.close()

    def updateSetting(self):
        try:
            conn = sqlite3.connect("my.sqlite")
            cur = conn.cursor()
            # open setting to form
            query = """update setting set server_url= ?, database= ?,username= ?,password= ?"""
            cur.execute(query, (self.ui.tbServer.text(), self.ui.tbDatabase.text(), self.ui.tbUsername.text(), self.ui.tbPassword.text()))
            conn.commit()

            cur.close()
            conn.close()
        except Exception as e:
            print(e)
        finally:
            print("Update setting successful.....")


if __name__ == "__main__":
    # app = QApplication([])
    app = QApplication(sys.argv)
    widget = Main()

    # center screen
    center = QApplication.primaryScreen().geometry().center()
    widget.show()
    widget.move(center - widget.frameGeometry().center())

    sys.exit(app.exec())
