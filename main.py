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
from zk import ZK, const
from myzk import MyZK
import json


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        # self.load_ui()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database_name = "my.sqlite"
        self.ui.tbMachineName.setEnabled(True)

        # hide table column
        self.ui.machineTable.setColumnHidden(3, True)
        self.ui.tbMachineId.hide()

        # open setting
        # -----------------------------------------------
        conn = sqlite3.connect(self.database_name)
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
        # cur = conn.cursor()
        # cur.execute("SELECT id,name,address,port,machine_id from zkmachine")
        # machineRows = cur.fetchall()
        # print('Get Data Machine')
        # print('------------------------------')
        # # pprint(machineRows)
        # cur.close()

        # if machineRows:
        #     rowidx = 0
        #     self.ui.machineTable.setRowCount(len(machineRows))

        #     for machine in machineRows:
        #         self.ui.machineTable.setItem(rowidx,0,QtWidgets.QTableWidgetItem(str(machine[1])))
        #         self.ui.machineTable.setItem(rowidx,1,QtWidgets.QTableWidgetItem(str(machine[2])))
        #         self.ui.machineTable.setItem(rowidx,2,QtWidgets.QTableWidgetItem(str(machine[3])))

        #         rowidx+=1

        self.loadDataToTable(conn)

        conn.close()
        # ---------------------------------------------

        # initialize variable
        # form mode
        # normal, edit, new
        self.formMode = 'normal'

    def loadDataToTable(self, conn):
        # open machine data
        cur = conn.cursor()
        cur.execute("SELECT id,name,address,port,machine_id from zkmachine")
        machineRows = cur.fetchall()
        print('Get Data Machine')
        print('------------------------------')
        # pprint(machineRows)
        cur.close()

        self.ui.machineTable.clear()

        if machineRows:
            rowidx = 0
            self.ui.machineTable.setRowCount(len(machineRows))

            for machine in machineRows:
                self.ui.machineTable.setItem(rowidx, 0, QtWidgets.QTableWidgetItem(str(machine[1])))
                self.ui.machineTable.setItem(rowidx, 1, QtWidgets.QTableWidgetItem(str(machine[2])))
                self.ui.machineTable.setItem(rowidx, 2, QtWidgets.QTableWidgetItem(str(machine[3])))
                self.ui.machineTable.setItem(rowidx, 3, QtWidgets.QTableWidgetItem(str(machine[0])))

                rowidx += 1

    def testMachineConnection(self):
        if self.isTableSelected():
            print('Machine test connection ......')

            ip_addr = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 1).text()
            port = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 2).text()

            zk = MyZK(ip_addr, port=int(port))

            try:
                print('Machine connecting.....')
                conn = zk.connect()
                conn.disable_device()
                users = conn.get_users()
                QMessageBox.information(self, "Connection Successful", "Machine contains " + str(len(users)) + " users")
                conn.enable_device()
                conn.disconnect()
            except Exception as e:
                QMessageBox.warning(self, "Machine Connection Error", str(e))
        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

    def clearInputan(self):
        self.ui.tbMachineAddress.setText("")
        self.ui.tbMachineName.setText("")
        self.ui.tbMachinePort.setText("")

    def newMachine(self):
        self.formMode = 'new'

        # clear inputan
        self.clearInputan()

        # set enable inputan
        self.toggleMachineInput(True)
        self.ui.tbMachineName.setFocus()

    def toggleMachineInput(self, val):
        print('toggle machine')
        self.ui.gbMachineSetting.setEnabled(val)
        self.ui.machineTable.setEnabled(not val)

        self.ui.btnSync.setEnabled(not val)
        self.ui.btnNew.setEnabled(not val)
        self.ui.btnEdit.setEnabled(not val)
        self.ui.btnDelete.setEnabled(not val)

    def isTableSelected(self):
        return (len(self.ui.machineTable.selectedItems()) > 0)

    def editMachine(self):
        if self.isTableSelected():
            # if len(self.ui.machineTable.selectedItems()) > 0:
            self.toggleMachineInput(True)

            self.formMode = 'edit'
        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

    def deleteMachine(self):
        if self.isTableSelected():
            if QMessageBox.question(self, "Delete Machine", "Are you sure ?", QMessageBox.Yes, QMessageBox.No) == QMessageBox.Yes:
                print('Delete machine')
                machine_id = int(self.ui.machineTable.item(self.ui.machineTable.currentRow(), 3).text())

                # delete machine
                conn = sqlite3.connect(self.database_name)
                cur = conn.cursor()

                cur.execute("delete from zkmachine where id = " + str(machine_id))

                rows = cur.fetchall()
                cur.close()
                conn.commit()
                self.loadDataToTable(conn)
                conn.close()

                # de select machineTable
                self.ui.machineTable.selectRow(-1)
        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

    def insertMachine(self):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()

        query = "INSERT INTO zkmachine (name,address,port) values (?,?,?)"

        cur.execute(query, (self.ui.tbMachineName.text(), self.ui.tbMachineAddress.text(), self.ui.tbMachinePort.text()))
        conn.commit()

        cur.close()

        self.loadDataToTable(conn)

        conn.close()
        self.toggleMachineInput(False)

    def updateMachine(self):
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()

        query = "update zkmachine set name = ?,address = ?,port = ? where id = ?"

        cur.execute(query, (self.ui.tbMachineName.text(), self.ui.tbMachineAddress.text(), self.ui.tbMachinePort.text(), int(self.ui.tbMachineId.text())))
        conn.commit()

        cur.close()

        self.loadDataToTable(conn)

        conn.close()
        self.toggleMachineInput(False)

    def saveMachine(self):
        print('FORM MODE : ')
        print(self.formMode)

        if self.formMode == 'new':
            self.insertMachine()
        elif self.formMode == 'edit':
            self.updateMachine()

    def cancelMachine(self):
        print('Cancel Machine')
        self.toggleMachineInput(False)

        self.formMode = 'normal'

    def getAttendances(self):
        ip_addr = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 1).text()
        port = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 2).text()

        zk = MyZK(ip_addr, port=int(port))

        try:
            print('Machine connecting.....')
            conn = zk.connect()
            conn.disable_device()
            att_json = {}

            # Get attendances
            # attendances = conn.get_attendance()
            # if attendances:
            #     pprint(attendances)
            # else :
            #     print('Empty attendance')

            att_json = conn.get_attendance_json()
            # if att_json:
            #     pprint(att_json)
            # else:
            #     print('Empty Attendance')

            conn.enable_device()
            conn.disconnect()

            return att_json
        except Exception as e:
            QMessageBox.warning(self, "Machine Connection Error", str(e))

    def syncAttendance(self):
        if self.isTableSelected():
            print('Sync Machine .....')

            try:
                print('Create connection ...')
                odooCon = OdooConnection(self.ui.tbUsername.text(), self.ui.tbPassword.text(), self.ui.tbDatabase.text(), self.ui.tbServer.text())
                session_id = odooCon.getSessionId()
                print('Session id : ' + session_id)
                if session_id:
                    atts = {}
                    atts = self.getAttendances()
                    

                    postjson = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "attendance": json.dumps(atts, default=str)
                        },
                        "id": None
                    }

                    print('-----------------------------')
                    # pprint(postjson)

                    headers = {
                        'content-type': "application/json",
                        'Cookie' : "session_id="+session_id+";"
                    }

                    print('Posting json data to server ......')
                    # postjson = {
                    #     "jsonrpc": "2.0",
                    #     "method": "call",
                    #     "params": {
                    #         "attendance": []
                    #     },
                    #     "id": None
                    # }
                    # pprint(postjson)
                    print('Jumlah attendance : ' + str(len(atts)))
                    res =  requests.post(self.ui.tbServer.text() + '/sync/attendance', headers=headers, json=postjson)
                    # res =  requests.post(self.ui.tbServer.text() + '/sync/raw/attendance', headers=headers, json=postjson)
                    print('post done.')
                    
                    
                    return res

            except Exception as e:
                QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)

        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

    def machineSelected(self):
        print('Selected Items : ')
        self.ui.tbMachineName.setText(self.ui.machineTable.selectedItems()[0].text())
        self.ui.tbMachineAddress.setText(self.ui.machineTable.selectedItems()[1].text())
        self.ui.tbMachinePort.setText(self.ui.machineTable.selectedItems()[2].text())
        machine_id = int(self.ui.machineTable.item(self.ui.machineTable.currentRow(), 3).text())
        self.ui.tbMachineId.setText(str(machine_id))

    def testConnection(self):
        try:
            odooCon = OdooConnection(self.ui.tbUsername.text(), self.ui.tbPassword.text(), self.ui.tbDatabase.text(), self.ui.tbServer.text())
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
            conn = sqlite3.connect(self.database_name)
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
