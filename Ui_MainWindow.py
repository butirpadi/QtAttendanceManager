# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QGroupBox, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(538, 504)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabMachine = QWidget()
        self.tabMachine.setObjectName(u"tabMachine")
        self.verticalLayout_3 = QVBoxLayout(self.tabMachine)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.machineTable = QTableWidget(self.tabMachine)
        if (self.machineTable.columnCount() < 4):
            self.machineTable.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.machineTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.machineTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.machineTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.machineTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.machineTable.setObjectName(u"machineTable")
        self.machineTable.setSelectionMode(QAbstractItemView.SingleSelection)
        self.machineTable.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.verticalLayout_3.addWidget(self.machineTable)

        self.frame_5 = QFrame(self.tabMachine)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.gbMachineSetting = QGroupBox(self.frame_5)
        self.gbMachineSetting.setObjectName(u"gbMachineSetting")
        self.gbMachineSetting.setEnabled(False)
        self.gridLayout_2 = QGridLayout(self.gbMachineSetting)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tbMachineName = QLineEdit(self.gbMachineSetting)
        self.tbMachineName.setObjectName(u"tbMachineName")
        self.tbMachineName.setEnabled(False)

        self.gridLayout_2.addWidget(self.tbMachineName, 0, 2, 1, 2)

        self.tbMachinePort = QLineEdit(self.gbMachineSetting)
        self.tbMachinePort.setObjectName(u"tbMachinePort")

        self.gridLayout_2.addWidget(self.tbMachinePort, 2, 2, 1, 1)

        self.tbMachineId = QLineEdit(self.gbMachineSetting)
        self.tbMachineId.setObjectName(u"tbMachineId")

        self.gridLayout_2.addWidget(self.tbMachineId, 2, 3, 1, 1)

        self.label_6 = QLabel(self.gbMachineSetting)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.label_5 = QLabel(self.gbMachineSetting)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.frame_6 = QFrame(self.gbMachineSetting)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.NoFrame)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 4, 0, 4)

        self.gridLayout_2.addWidget(self.frame_6, 3, 2, 1, 1)

        self.label_7 = QLabel(self.gbMachineSetting)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.tbMachineAddress = QLineEdit(self.gbMachineSetting)
        self.tbMachineAddress.setObjectName(u"tbMachineAddress")

        self.gridLayout_2.addWidget(self.tbMachineAddress, 1, 2, 1, 2)

        self.frame_7 = QFrame(self.gbMachineSetting)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(4, 4, 4, 4)
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_4)

        self.btnMachineSave = QPushButton(self.frame_7)
        self.btnMachineSave.setObjectName(u"btnMachineSave")
        self.btnMachineSave.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.btnMachineSave)

        self.btnMachineCancel = QPushButton(self.frame_7)
        self.btnMachineCancel.setObjectName(u"btnMachineCancel")
        self.btnMachineCancel.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_6.addWidget(self.btnMachineCancel)


        self.gridLayout_2.addWidget(self.frame_7, 3, 3, 1, 1)


        self.horizontalLayout_4.addWidget(self.gbMachineSetting)


        self.verticalLayout_3.addWidget(self.frame_5)

        self.frame_4 = QFrame(self.tabMachine)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnTestMachine = QPushButton(self.frame_4)
        self.btnTestMachine.setObjectName(u"btnTestMachine")
        self.btnTestMachine.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnTestMachine)

        self.btnSync = QPushButton(self.frame_4)
        self.btnSync.setObjectName(u"btnSync")
        self.btnSync.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnSync)

        self.btnNew = QPushButton(self.frame_4)
        self.btnNew.setObjectName(u"btnNew")
        self.btnNew.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnNew)

        self.btnEdit = QPushButton(self.frame_4)
        self.btnEdit.setObjectName(u"btnEdit")
        self.btnEdit.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnEdit)

        self.btnDelete = QPushButton(self.frame_4)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnDelete)


        self.verticalLayout_3.addWidget(self.frame_4)

        self.tabWidget.addTab(self.tabMachine, "")
        self.tabSetting = QWidget()
        self.tabSetting.setObjectName(u"tabSetting")
        self.verticalLayout_2 = QVBoxLayout(self.tabSetting)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.tabSetting)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, 5, 5, 5)
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.tbDatabase = QLineEdit(self.frame)
        self.tbDatabase.setObjectName(u"tbDatabase")

        self.gridLayout.addWidget(self.tbDatabase, 1, 2, 1, 1)

        self.tbPassword = QLineEdit(self.frame)
        self.tbPassword.setObjectName(u"tbPassword")

        self.gridLayout.addWidget(self.tbPassword, 3, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.tbUsername = QLineEdit(self.frame)
        self.tbUsername.setObjectName(u"tbUsername")

        self.gridLayout.addWidget(self.tbUsername, 2, 2, 1, 1)

        self.tbServer = QLineEdit(self.frame)
        self.tbServer.setObjectName(u"tbServer")

        self.gridLayout.addWidget(self.tbServer, 0, 2, 1, 1)

        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.tabSetting)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 40))
        self.frame_2.setFrameShape(QFrame.NoFrame)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.btnTest = QPushButton(self.frame_2)
        self.btnTest.setObjectName(u"btnTest")
        self.btnTest.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btnTest)

        self.btnSave = QPushButton(self.frame_2)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setMinimumSize(QSize(0, 30))

        self.horizontalLayout.addWidget(self.btnSave)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.tabWidget.addTab(self.tabSetting, "")

        self.verticalLayout.addWidget(self.tabWidget)

        self.frame_3 = QFrame(self.centralwidget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.btnClose = QPushButton(self.frame_3)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_2.addWidget(self.btnClose)


        self.verticalLayout.addWidget(self.frame_3)

        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.tabWidget, self.btnSync)
        QWidget.setTabOrder(self.btnSync, self.btnNew)
        QWidget.setTabOrder(self.btnNew, self.btnEdit)
        QWidget.setTabOrder(self.btnEdit, self.btnDelete)
        QWidget.setTabOrder(self.btnDelete, self.btnClose)
        QWidget.setTabOrder(self.btnClose, self.tbServer)
        QWidget.setTabOrder(self.tbServer, self.tbDatabase)
        QWidget.setTabOrder(self.tbDatabase, self.tbUsername)
        QWidget.setTabOrder(self.tbUsername, self.tbPassword)
        QWidget.setTabOrder(self.tbPassword, self.btnTest)
        QWidget.setTabOrder(self.btnTest, self.btnSave)

        self.retranslateUi(MainWindow)
        self.btnClose.clicked.connect(MainWindow.closeWindow)
        self.btnSave.clicked.connect(MainWindow.updateSetting)
        self.btnTest.clicked.connect(MainWindow.testConnection)
        self.machineTable.itemSelectionChanged.connect(MainWindow.machineSelected)
        self.btnEdit.clicked.connect(MainWindow.editMachine)
        self.btnNew.clicked.connect(MainWindow.newMachine)
        self.btnDelete.clicked.connect(MainWindow.deleteMachine)
        self.btnSync.clicked.connect(MainWindow.syncAttendance)
        self.btnMachineSave.clicked.connect(MainWindow.saveMachine)
        self.btnMachineCancel.clicked.connect(MainWindow.cancelMachine)
        self.btnTestMachine.clicked.connect(MainWindow.testMachineConnection)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Odoo Attendance Manager", None))
        ___qtablewidgetitem = self.machineTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.machineTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem2 = self.machineTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem3 = self.machineTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"id", None));
        self.gbMachineSetting.setTitle(QCoreApplication.translate("MainWindow", u"Machine Setting", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Port", None))
        self.btnMachineSave.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.btnMachineCancel.setText(QCoreApplication.translate("MainWindow", u"CANCEL", None))
        self.btnTestMachine.setText(QCoreApplication.translate("MainWindow", u"TEST CONNECTION", None))
        self.btnSync.setText(QCoreApplication.translate("MainWindow", u"SYNC", None))
        self.btnNew.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.btnEdit.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.btnDelete.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMachine), QCoreApplication.translate("MainWindow", u"Machine", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Server Address", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Database", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.btnTest.setText(QCoreApplication.translate("MainWindow", u"TEST", None))
        self.btnSave.setText(QCoreApplication.translate("MainWindow", u"SAVE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabSetting), QCoreApplication.translate("MainWindow", u"Setting", None))
        self.btnClose.setText(QCoreApplication.translate("MainWindow", u"CLOSE", None))
    # retranslateUi

