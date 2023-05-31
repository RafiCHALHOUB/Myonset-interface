# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BipolarWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtCore import QObject


class Ui_BipolarWindow(QtWidgets.QWidget, object):
    def __init__(self, parent=None):
        super(Ui_BipolarWindow, self).__init__(parent=parent)
        # Set the tool button style for the BipolarWindow
        self.ui = Ui_BipolarWindow
        self.ui.setObjectName(self, "BipolarWindow")
        self.ui.resize(self, 660, 355)
        self.ui.setContextMenuPolicy(self, QtCore.Qt.DefaultContextMenu)
        self.ui.setLayoutDirection(self, QtCore.Qt.LayoutDirection.LeftToRight)
        # self.ui.setToolButtonStyle(self,QtCore.Qt.ToolButtonStyle)
        # self.ui.setDocumentMode(False)
        # self.ui.setTabShape(self,QtWidgets.QTabWidget.Rounded)
        # self.ui.setUnifiedTitleAndToolBarOnMac(False)
        self.setupUi(self)

    def setupUi(self, BipolarWindow):
        self.centralwidget = QtWidgets.QWidget(BipolarWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAcceptDrops(False)
        self.label.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label.setScaledContents(False)
        self.label.setIndent(-3)
        self.label.setObjectName("label")
        self.columnView_6 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_6.setGeometry(QtCore.QRect(20, 70, 81, 111))
        self.columnView_6.setProperty("showDropIndicator", False)
        self.columnView_6.setDragEnabled(True)
        self.columnView_6.setObjectName("columnView_6")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 100, 141, 51))
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
        self.columnView_8 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_8.setGeometry(QtCore.QRect(20, 190, 81, 111))
        self.columnView_8.setProperty("showDropIndicator", False)
        self.columnView_8.setDragEnabled(True)
        self.columnView_8.setObjectName("columnView_8")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(150, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAcceptDrops(False)
        self.label_2.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_2.setLineWidth(3)
        self.label_2.setScaledContents(False)
        self.label_2.setIndent(-3)
        self.label_2.setObjectName("label_2")
        self.columnView_7 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_7.setGeometry(QtCore.QRect(170, 70, 81, 111))
        self.columnView_7.setProperty("showDropIndicator", False)
        self.columnView_7.setDragEnabled(True)
        self.columnView_7.setObjectName("columnView_7")
        self.columnView_9 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_9.setGeometry(QtCore.QRect(170, 190, 81, 111))
        self.columnView_9.setProperty("showDropIndicator", False)
        self.columnView_9.setDragEnabled(True)
        self.columnView_9.setObjectName("columnView_9")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(310, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setAcceptDrops(False)
        self.label_4.setLayoutDirection(QtCore.Qt.LayoutDirection.LeftToRight)
        self.label_4.setStyleSheet("")
        self.label_4.setFrameShape(QtWidgets.QFrame.Panel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setLineWidth(3)
        self.label_4.setScaledContents(False)
        self.label_4.setIndent(-3)
        self.label_4.setObjectName("label_4")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(330, 210, 141, 51))
        self.textEdit_2.setObjectName("textEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 270, 89, 25))
        self.pushButton.setObjectName("pushButton")
        # BipolarWindow.setCentralWidget(self.centralwidget)
        # self.menubar = QtWidgets.QMenuBar(BipolarWindow)
        # self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        # self.menubar.setObjectName("menubar")
        # BipolarWindow.setMenuBar(self.menubar)
        # self.statusbar = QtWidgets.QStatusBar(BipolarWindow)
        # self.statusbar.setObjectName("statusbar")
        # BipolarWindow.setStatusBar(self.statusbar)

        self.retranslateUi(BipolarWindow)
        QtCore.QMetaObject.connectSlotsByName(BipolarWindow)

    def retranslateUi(self, BipolarWindow):
        _translate = QtCore.QCoreApplication.translate
        BipolarWindow.setWindowTitle(_translate("BipolarWindow", "Bipolar Reference"))
        self.label.setText(_translate("BipolarWindow", "Anode"))
        self.label_2.setText(_translate("BipolarWindow", "Cathode"))
        self.label_4.setText(_translate("BipolarWindow", "New Channel"))
        self.pushButton.setText(_translate("BipolarWindow", "Execute"))

    # self.comboBox_2.addItems(channels)
    # self.comboBox_3.addItems(channels)
    # self.comboBox_4.addItems(channels)

    # Set channel names in the drop-down menus

    # self.ui.set_dropdown_values("channels")

    # self.controller.get_channel_names('channels')
    # print(channels)
    # self.ui.set_dropdown_values(self)
    # self.ui.set_dropdown_values('channels')
    # print("Channels in EMGWindow:", channels)
    # self.ui.set_dropdown_values(channels)
    # Pass channel names to second window

    #  self.ui.set_dropdown_values(channel_names)
    #   channels = self.controllechr.get_channel_names()
    #  print("Channels in EMGWindow:", channels)
    # self.ui.set_dropdown_values(channels)

    # print(type(channels))
    def get_channel_names(self):
        # Get channel names from model
        channels = self.controller.get_channel_names()
        # Clear all dropdown menus
        self.ui = Ui_BipolarWindow(channels)

        self.ui.comboBox.clear()
        if channels:
            for channel in channels:
                self.ui.comboBox.addItem(channel)

        else:
            print("list is empty")
        self.ui.show()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BipolarWindow = QtWidgets.QMainWindow()
    ui = Ui_BipolarWindow()
    ui.setupUi(BipolarWindow)
    BipolarWindow.show()
    sys.exit(app.exec_())
