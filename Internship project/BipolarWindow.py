from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_BipolarWindow(QtWidgets.QWidget, object):
    def __init__(self, controller, channels):
        from view import EMGWindow
        super(Ui_BipolarWindow, self).__init__()
        # Set the tool button style for the BipolarWindow
        self.controller = controller
        self.channels = channels
        self.ui = Ui_BipolarWindow
        self.view = EMGWindow
        self.ui.setObjectName(self, "BipolarWindow")
        self.ui.resize(self, 660, 355)
        self.ui.setContextMenuPolicy(self, QtCore.Qt.DefaultContextMenu)
        self.ui.setLayoutDirection(self, QtCore.Qt.LayoutDirection.LeftToRight)
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
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(330, 100, 141, 51))
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setObjectName("textEdit")
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
        self.pushButton.setGeometry(QtCore.QRect(518, 254, 121, 41))
        self.pushButton.clicked.connect(self.apply_bipolar_reference)
        self.pushButton.clicked.connect(self.close_window)

        self.pushButton.setObjectName("pushButton")
        # self.pushButton.clicked.connect(self.apply_bipolar_reference())
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(20, 100, 81, 22))
        self.comboBox.addItems(self.channels)
        self.comboBox.setObjectName("comboBox")

        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(170, 100, 81, 22))
        self.comboBox_2.addItems(self.channels)
        self.comboBox_2.setObjectName("comboBox_2")

        self.comboBox_3 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 210, 81, 22))
        self.comboBox_3.addItems(self.channels)
        self.comboBox_3.setObjectName("comboBox_3")

        self.comboBox_4 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_4.setGeometry(QtCore.QRect(170, 210, 81, 22))
        self.comboBox_4.addItems(self.channels)

        self.comboBox_4.setObjectName("comboBox_4")

        self.retranslateUi(BipolarWindow)
        QtCore.QMetaObject.connectSlotsByName(BipolarWindow)
        BipolarWindow.setTabOrder(self.comboBox, self.comboBox_2)
        BipolarWindow.setTabOrder(self.comboBox_2, self.comboBox_3)
        BipolarWindow.setTabOrder(self.comboBox_3, self.comboBox_4)
        BipolarWindow.setTabOrder(self.comboBox_4, self.textEdit)
        BipolarWindow.setTabOrder(self.textEdit, self.textEdit_2)
        BipolarWindow.setTabOrder(self.textEdit_2, self.pushButton)

    def retranslateUi(self, BipolarWindow):
        _translate = QtCore.QCoreApplication.translate
        BipolarWindow.setWindowTitle(_translate("BipolarWindow", "Bipolar Reference"))
        self.label.setText(_translate("BipolarWindow", "Anode:"))
        self.label_2.setText(_translate("BipolarWindow", "Cathode:"))
        self.label_4.setText(_translate("BipolarWindow", "New Channel"))
        self.pushButton.setText(_translate("BipolarWindow", "Execute"))

    def apply_bipolar_reference(self):
        anode1 = self.comboBox.currentText()
        cathode1 = self.comboBox_2.currentText()
        anode2 = self.comboBox_3.currentText()
        cathode2 = self.comboBox_4.currentText()
        channel1 = self.textEdit.toPlainText()
        channel2 = self.textEdit_2.toPlainText()
        self.controller.apply_bipolar_reference(anode1, cathode1, channel1, anode2, cathode2, channel2)

    def close_window(self):
        self.ui.close(self)


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    BipolarWindow = QtWidgets.QMainWindow()
    ui = Ui_BipolarWindow(None)
    ui.setupUi(BipolarWindow)
    BipolarWindow.show()
    sys.exit(app.exec_())
