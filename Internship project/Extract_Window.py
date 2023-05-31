# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Extract_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Extract_events_Window(QtWidgets.QWidget, object):
    def __init__(self, controller):
        from view import EMGWindow
        super(Ui_Extract_events_Window, self).__init__()
        self.controller = controller
        self.extractui = Ui_Extract_events_Window
        self.extractui.setObjectName(self, "Extract_events_Window")
        self.extractui.resize(self, 681, 146)
        self.extractui.setCursor(self, QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        self.extractui.setStyleSheet(self, "background-color: rgb(222, 221, 218);")
        self.view = EMGWindow(self)
        self.setupexUi(self)

    def setupexUi(self, Extract_events_Window):
        self.centralwidget = QtWidgets.QWidget(Extract_events_Window)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(360, 70, 171, 25))
        self.pushButton.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("")
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 70, 171, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 0, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        # Extract_events_Window.setCentralWidget(self.centralwidget)

        self.retranslateUi(Extract_events_Window)
        QtCore.QMetaObject.connectSlotsByName(Extract_events_Window)

    def retranslateUi(self, Extract_events_Window):
        _translate = QtCore.QCoreApplication.translate
        Extract_events_Window.setWindowTitle(_translate("Extract_events_Window", "Extract events"))
        self.pushButton.setText(_translate("Extract_events_Window", "Cancel"))
        self.pushButton.clicked.connect(self.close_window)
        self.pushButton_3.setText(_translate("Extract_events_Window", "Extract events"))
        self.pushButton_3.clicked.connect(self.extract_events)
        self.pushButton_3.clicked.connect(self.close_window)

        self.label.setText(_translate("Extract_events_Window", "  Would you like to extract events ?"))

    def extract_events(self):
        self.controller.extract_events()

    def close_window(self):
        self.extractui.close(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Extract_events_Window = QtWidgets.QWidget()
    ui = Ui_Extract_events_Window(self)
    ui.setupexUi(Extract_events_Window)
    Extract_events_Window.show()
    sys.exit(app.exec_())
