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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTabWidget,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(453, 351)
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
        self.tableView = QTableView(self.tabMachine)
        self.tableView.setObjectName(u"tableView")

        self.verticalLayout_3.addWidget(self.tableView)

        self.frame_4 = QFrame(self.tabMachine)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.NoFrame)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnClose_5 = QPushButton(self.frame_4)
        self.btnClose_5.setObjectName(u"btnClose_5")
        self.btnClose_5.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnClose_5)

        self.btnClose_2 = QPushButton(self.frame_4)
        self.btnClose_2.setObjectName(u"btnClose_2")
        self.btnClose_2.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnClose_2)

        self.btnClose_3 = QPushButton(self.frame_4)
        self.btnClose_3.setObjectName(u"btnClose_3")
        self.btnClose_3.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnClose_3)

        self.btnClose_4 = QPushButton(self.frame_4)
        self.btnClose_4.setObjectName(u"btnClose_4")
        self.btnClose_4.setMinimumSize(QSize(0, 30))

        self.horizontalLayout_3.addWidget(self.btnClose_4)


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

        self.lineEdit_4 = QLineEdit(self.frame)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 1, 2, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 3, 2, 1, 1)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 2, 2, 1, 1)

        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

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

        self.retranslateUi(MainWindow)
        self.btnClose.clicked.connect(MainWindow.closeWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Odoo Attendance Manager", None))
        self.btnClose_5.setText(QCoreApplication.translate("MainWindow", u"SYNC", None))
        self.btnClose_2.setText(QCoreApplication.translate("MainWindow", u"NEW", None))
        self.btnClose_3.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        self.btnClose_4.setText(QCoreApplication.translate("MainWindow", u"DELETE", None))
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

