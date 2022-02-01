# This Python file uses the following encoding: utf-8
import os
import threading
import sys
import PySide6
import json
import sqlite3
import requests
import time
from pathlib import Path
# from typing import final
from PySide6 import QtWidgets
from PySide6 import QtCore, QtSql
from PySide6.QtGui import QShowEvent, QStandardItemModel
from PySide6.QtWidgets import QApplication, QHeaderView,  QMainWindow, QMessageBox, QTableWidgetItem
from PySide6.QtCore import QCoreApplication, QFile, QSize
from OdooConnection import OdooConnection
from ThreadClass import ThreadClass
from Ui_MainWindow import Ui_MainWindow
from pprint import pprint
from zk import ZK, const
from myzk import MyZK


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        # self.load_ui()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.database_name = "my.sqlite"
        self.ui.tbMachineName.setEnabled(True)

        self.thread = {}

        # hide table column
        self.ui.machineTable.setColumnHidden(3, True)
        self.ui.tbMachineId.hide()
        # self.ui.machineTable.hide()
        self.ui.btnTestSync.hide()
        # self.ui.btnTestSync.setEnabled(True)

        # open setting
        # -----------------------------------------------
        conn = sqlite3.connect(self.database_name)
        cur = conn.cursor()

        # create table setting
        cur.execute(
            "CREATE TABLE IF NOT EXISTS[setting] ([id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,[server_url] VARCHAR(1024) NULL,[database] VARCHAR(100) NULL,[username] VARCHAR(100) NULL,[password] VARCHAR(100) NULL)")
        # crewate table machine
        cur.execute(
            "CREATE TABLE IF NOT EXISTS[zkmachine] ([id] INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,[name] VARCHAR(100) NULL,[address] VARCHAR(500) NULL,[port] VARCHAR(100) NULL,[machine_id] VARCHAR(100) NULL)")

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
        else:
            # create init setting
            cur = conn.cursor()
            query = "insert into setting (server_url,database,username,password) values (?,?,?,?)"
            cur.execute(query, ("", "", "", ""))
            conn.commit()
            cur.close()

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

        # QTableView
        # set machine table header label
        # model = QStandardItemModel()
        # model.setHorizontalHeaderLabels(['Name','Address','Port','ID'])
        # self.ui.tableView.setModel(model)
        self.loadTableView()
        
        self.ui.tableView.clicked.connect(self._tableViewClicked)
        # self.ui.tableView.selectionModel().Current.connect(self._tableViewClicked)
        
        self.ui.machineTable.hide()
    
    def loadTableView(self):
        # query table view
        self.sqlModel = QtSql.QSqlQueryModel()
        mydb = QtSql.QSqlDatabase("QSQLITE")
        mydb.setDatabaseName("my.sqlite")
        mydb.open()
        query = QtSql.QSqlQuery(mydb)
        query.exec("select name as NAME, address as ADDRESS ,port as PORT, id, null as ''   from zkmachine")
        self.sqlModel.setQuery(query)
        self.ui.tableView.setModel(self.sqlModel)    
        # hide column id  
        # self.ui.tableView.setColumnHidden(3,True)
        self.ui.tableView.hideColumn(3)
        # stretch column
        self.ui.tableView.resizeColumnToContents(0)
        self.ui.tableView.resizeColumnToContents(1)
        self.ui.tableView.resizeColumnToContents(2)
        # self.ui.tableView.horizontalHeader().
        # self.ui.tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
    
    def _tableViewClicked(self):
        selectedIndex = self.ui.tableView.selectionModel().currentIndex()
        selectedData = self.ui.tableView.model()
        # pprint(selectedData.index(selectedIndex.row(),0).data(0))
        # pprint(selectedData.index(selectedIndex.row(),1).data(0))
        # pprint(selectedData.index(selectedIndex.row(),2).data(0))
        # pprint(selectedData.index(selectedIndex.row(),3).data(0))
        # pprint(selectedData.index(selectedIndex.row(),4).data(0))
        # print('----------------------------')
        
        self.ui.tbMachineName.setText(selectedData.index(selectedIndex.row(),0).data(0))
        self.ui.tbMachineAddress.setText(selectedData.index(selectedIndex.row(),1).data(0))
        self.ui.tbMachinePort.setText(selectedData.index(selectedIndex.row(),2).data(0))
        self.machine_id = int(selectedData.index(selectedIndex.row(),3).data(0))
        self.ui.tbMachineId.setText(str(self.machine_id))        

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
        

    def _testMachineConnection(self):
        if self.isTableSelected():
            print('Machine test connection ......')

            # ip_addr = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 1).text()
            # port = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 2).text()
            
            selectedIndex = self.ui.tableView.selectionModel().currentIndex()
            selectedData = self.ui.tableView.model()
            
            
            ip_addr = selectedData.index(selectedIndex.row(),1).data(0)
            port = selectedData.index(selectedIndex.row(),2).data(0)

            zk = MyZK(ip_addr, port=int(port), timeout=10)

            try:
                print('Machine connecting.....')
                conn = zk.connect()
                conn.disable_device()
                users = conn.get_users()
                QMessageBox.information(self, "Connection Successful", "Connection successfull. \nMachine contains " + str(len(users)) + " users")
                conn.enable_device()
                conn.disconnect()
            except Exception as e:
                QMessageBox.warning(self, "Machine Connection Error", str(e))
        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

        self.setFormMode('normal')
        self.thread[0].stop()

    def testMachineConnection(self):
        self.setFormMode('sync')
        self.thread[0] = ThreadClass(None, 1)
        self.thread[0].start()
        self.thread[0].any_signal.connect(self._testMachineConnection)

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

        self.toggleMainButton(not val)

    def toggleMainButton(self, val):
        self.ui.btnSync.setEnabled(val)
        self.ui.btnNew.setEnabled(val)
        self.ui.btnEdit.setEnabled(val)
        self.ui.btnDelete.setEnabled(val)
        self.ui.btnTestMachine.setEnabled(val)
        self.ui.btnClose.setEnabled(val)

    def isTableSelected(self):
        if self.ui.machineTable.isHidden() :
            return (len(self.ui.tableView.selectedIndexes()) > 0)
        else:
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
                
                if self.ui.machineTable.isHidden() :
                    machine_id = self.machine_id
                else:                    
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
                self.loadTableView()
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
        self.loadTableView()

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
        self.loadTableView()
        
        # reload table view
        self.loadTableView()

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
        # ip_addr = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 1).text()
        # port = self.ui.machineTable.item(self.ui.machineTable.currentRow(), 2).text()
        
        ip_addr = self.ui.tbMachineAddress.text()
        port = self.ui.tbMachinePort.text()

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
            
            print('get attendance in json')
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

    def setFormMode(self, mode='normal'):
        self.formMode = mode

        if self.formMode == 'normal':
            self.ui.centralwidget.setEnabled(True)
            self.ui.machineTable.setEnabled(True)
            self.ui.gbMachineSetting.setEnabled(False)
        elif self.formMode == 'sync':
            self.ui.centralwidget.setEnabled(False)

    def testAttendance(self):
        print('=======================================')
        print('       TEST GET ATTENDANCE')
        print('=======================================')
        atts = self.getAttendances()
        pprint(atts)
    
    def syncRawAttendance(self):
        self.setFormMode('sync')
        self.thread[1] = ThreadClass(None, 1)
        self.thread[1].any_signal.connect(self._syncRawAttendance)
        self.thread[1].start()
        
    def _syncRawAttendance(self):
        if self.isTableSelected():
            print('Sync Raw Data .....')
            is_success = False
            try:
                print('Create connection ...')
                odooCon = OdooConnection(self.ui.tbUsername.text(), self.ui.tbPassword.text(), self.ui.tbDatabase.text(), self.ui.tbServer.text())
                session_id = odooCon.getSessionId()
                print('Session id : ' + session_id)
                if session_id:
                    atts = {}
                    print('Get Data Attendance')
                    atts = self.getAttendances()
                    print('Jumlah data attendance : ' + str(len(atts)))
                    # pprint(atts)                   

                    print('Posting Attendance to Server')
                    postjson = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "attendance": json.dumps(atts, default=str)
                        },
                        "id": None
                    }

                    # print('-----------------------------')
                    # pprint(postjson)

                    headers = {
                        'content-type': "application/json",
                        'Cookie': "session_id="+session_id+";"
                    }

                    print('Posting raw data to server ......')
                    res = requests.post(self.ui.tbServer.text() + '/sync/raw/attendance', headers=headers, json=postjson)
                    print('Send data successfull......')

                    is_success = True

                    return res

            except Exception as e:
                QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)
            finally:
                self.setFormMode('normal')
                if is_success:
                    QMessageBox.information(self, "Synchronizing Attendance", "Synchonizing successfull, check attendance data on your server.")

        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

        self.setFormMode('normal')
        self.thread[1].stop()

    def testSyncAttendance(self):
        self._syncAttendance(True)

    def syncAttendance(self):
        self.setFormMode('sync')
        self.thread[2] = ThreadClass(None, 1)
        self.thread[2].any_signal.connect(self._syncAttendance)
        self.thread[2].start()
        # self._syncAttendance(False)
        # self.setFormMode('normal')
    
    def _syncAttendance(self):
        if self.isTableSelected():
            print('Sync Machine .....')
            is_success = False
            try:
                print('Create connection ...')
                odooCon = OdooConnection(self.ui.tbUsername.text(), self.ui.tbPassword.text(), self.ui.tbDatabase.text(), self.ui.tbServer.text())
                session_id = odooCon.getSessionId()
                print('Session id : ' + session_id)
                if session_id:
                    atts = {}
                    print('Get Data Attendance')
                    atts = self.getAttendances()
                    print('Attendance Data : ' + str(len(atts)))
                    # pprint(atts)
                    

                    print('Prepare send attendance data to Server ...')
                    postjson = {
                        "jsonrpc": "2.0",
                        "method": "call",
                        "params": {
                            "attendance": json.dumps(atts, default=str)
                        },
                        "id": None
                    }

                    # print('-----------------------------')
                    # pprint(postjson)

                    headers = {
                        'content-type': "application/json",
                        'Cookie': "session_id="+session_id+";"
                    }

                    # print('Posting json data to server ......')
                    # postjson = {
                    #     "jsonrpc": "2.0",
                    #     "method": "call",
                    #     "params": {
                    #         "attendance": []
                    #     },
                    #     "id": None
                    # }
                    # pprint(postjson)
                    # print('Jumlah attendance : ' + str(len(atts)))

                    # if israw:
                    #     res = requests.post(self.ui.tbServer.text() + '/sync/raw/attendance', headers=headers, json=postjson)
                    # else:
                    print('Send data to server ....')
                    res = requests.post(self.ui.tbServer.text() + '/sync/attendance', headers=headers, json=postjson)
                    print('Send data succesfull....')

                    is_success = True

                    return res

            except Exception as e:
                QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)
            finally:
                self.setFormMode('normal')
                if is_success:
                    QMessageBox.information(self, "Synchronizing Attendance", "Synchonizing successfull, check attendance data on your server.")

        else:
            QMessageBox.warning(self, "Warning", "Select machine first.", QMessageBox.Ok)

        self.setFormMode('normal')
        self.thread[2].stop()

    def machineSelected(self):
        print('Selected Items : ')
        self.ui.tbMachineName.setText(self.ui.machineTable.selectedItems()[0].text())
        self.ui.tbMachineAddress.setText(self.ui.machineTable.selectedItems()[1].text())
        self.ui.tbMachinePort.setText(self.ui.machineTable.selectedItems()[2].text())
        machine_id = int(self.ui.machineTable.item(self.ui.machineTable.currentRow(), 3).text())
        self.ui.tbMachineId.setText(str(machine_id))

    def testConnection(self):

        # check input connection
        if self.ui.tbServer.text().strip() != "" and self.ui.tbUsername.text().strip() != "" and self.ui.tbPassword.text().strip() and self.ui.tbDatabase.text().strip():
            try:
                odooCon = OdooConnection(self.ui.tbUsername.text(), self.ui.tbPassword.text(), self.ui.tbDatabase.text(), self.ui.tbServer.text())
                session_id = odooCon.getSessionId()
                if session_id:
                    QMessageBox.warning(self, "Connection Successful", "Connection successful. \n Your session id : " + session_id, QMessageBox.Ok)
            except Exception as e:
                QMessageBox.warning(self, "Connection failed", str(e), QMessageBox.Ok)
        else:
            QMessageBox.warning(self, "Connection Test", "Fill all input.", QMessageBox.Ok)

    def closeWindow(self):
        if QMessageBox.warning(self, "Close", "Are you sure?", QMessageBox.Yes | QMessageBox.No) == QMessageBox.Yes:
            self.close()

    def updateSetting(self):
        try:
            conn = sqlite3.connect(self.database_name)
            cur = conn.cursor()
            # open setting to form
            query = "update setting set server_url= ?, database= ?,username= ?,password= ?"
            cur.execute(query, (self.ui.tbServer.text(), self.ui.tbDatabase.text(), self.ui.tbUsername.text(), self.ui.tbPassword.text()))
            conn.commit()
            print('Updating setting ....')
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
    # widget.move(center - widget.frameGeometry().center())
    widgetPos = widget.frameGeometry()
    # widget.move(center)
    widget.move(center.x() - (widgetPos.width()/2), center.y() - (widgetPos.height()/2))

    sys.exit(app.exec())
