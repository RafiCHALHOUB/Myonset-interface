from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QAction, QLineEdit, QWidget
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
from BipolarWindow import Ui_BipolarWindow
from FilterWindow import Ui_FilterWindow
from Extract_Window import Ui_Extract_events_Window
from SegmentationWindow import Ui_SegmentationWindow
from Emg_detection_window import Ui_Emg_detection_window
from forecedetectionwindow import Ui_force_detection_window
from VizWindow import Ui_VizWindow


class EMGWindow(QMainWindow):
    def __init__(self, controller):
        super(EMGWindow, self).__init__()
        self.controller = controller
        self.setWindowTitle("Traitement de signaux EMG")
        self.setGeometry(100, 100, 1000, 600)
        self.widgets(self)

    def openforcewindow(self):
        # self.window = QtWidgets.QMainWindow()
        channels = self.controller.get_channel_names()
        self.forceui = Ui_force_detection_window(self.controller, channels)
        self.forceui.setupforceUi(self.forceui)
        if channels:
            self.forceui.listWidget.addItems(channels)
        self.forceui.show()

    def openemgwindow(self):
        # self.window = QtWidgets.QMainWindow()
        channels = self.controller.get_channel_names()
        self.emgui = Ui_Emg_detection_window(self.controller, channels)
        self.emgui.setupemgUi(self.emgui)
        if channels:
            self.emgui.listWidget.addItems(channels)
        self.emgui.show()

    def opensegmentationwindow(self):
        self.window = QtWidgets.QMainWindow()
        events_ids = self.controller.get_events_ids()
        self.segui = Ui_SegmentationWindow(self.controller, events_ids)
        if len(events_ids):
            unique_event_ids = sorted(set(events_ids))
            unique_event_ids = list(unique_event_ids)
            self.segui.listWidget.clear()  # clear the listWidget
            for event_id in unique_event_ids:
                self.segui.listWidget.addItem(str(event_id))
        self.segui.show()

    def openemgvizwindow(self):
        self.window = QtWidgets.QMainWindow()
        events_ids = self.controller.get_events_ids()
        self.vizui = Ui_VizWindow(self.controller, events_ids)
        if len(events_ids):
            unique_event_ids = sorted(set(events_ids))
            unique_event_ids = list(unique_event_ids)

            self.vizui.listWidget.clear()  # clear the listWidget
            for event_id in unique_event_ids:
                self.vizui.listWidget.addItem(str(event_id))
                self.vizui.comboBox.addItem(str(event_id))
                self.vizui.comboBox_2.addItem(str(event_id))

        self.vizui.show()

    def openforcevizwindow(self):
        self.forceui.vizui.show()

    def openfilterwindow(self):
        self.window = QtWidgets.QMainWindow()

        channels = self.controller.get_channel_names()
        self.filterui = Ui_FilterWindow(self.controller, channels)
        if channels:
            self.filterui.listWidget.addItems(channels)
            self.filterui.listWidget_2.addItems(channels)
        self.filterui.show()

    def openbipWindow(self):
        self.window = QtWidgets.QMainWindow()
        # Get channel names from model
        channels = self.controller.get_channel_names()
        # Clear all dropdown menus
        self.ui = Ui_BipolarWindow(self.controller, channels)
        # self.controller.apply_bipolar_reference(bipolar)
        # self.ui.pushButton.clicked.connect()
        self.ui.comboBox.clear()
        if channels:
            for channel in channels:
                self.ui.comboBox.addItems(channels)
                self.ui.comboBox_2.addItems(channels)
                self.ui.comboBox_3.addItems(channels)
                self.ui.comboBox_4.addItems(channels)
        else:
            print("list is empty")

        self.ui.setupUi(self.ui)
        self.ui.show()

    def widgets(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(929, 766)
        MainWindow.setAutoFillBackground(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 0, 401, 151))
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo_bleu_myonset.svg"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, 640, 251, 81))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(100, 680, 151, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(20, 370, 311, 281))
        self.widget.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.widget.setObjectName("widget")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(105, 10, 121, 31))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_3.setTextFormat(QtCore.Qt.AutoText)
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.widget_4 = QtWidgets.QWidget(self.centralwidget)
        self.widget_4.setGeometry(QtCore.QRect(50, 220, 251, 101))
        self.widget_4.setMouseTracking(False)
        self.widget_4.setAutoFillBackground(False)
        self.widget_4.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(50, 60, 151, 31))
        self.label_4.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.label_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")

        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 60, 161, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 150, 161, 41))
        self.pushButton_6.setObjectName("pushButton_6")
        self.widget_3 = QtWidgets.QWidget(self.centralwidget)
        self.widget_3.setGeometry(QtCore.QRect(50, 200, 251, 80))
        self.widget_3.setMouseTracking(False)
        self.widget_3.setAutoFillBackground(False)
        self.widget_3.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.widget_3.setObjectName("widget_3")
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setGeometry(QtCore.QRect(80, 30, 101, 31))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget_3)
        self.label_5.setGeometry(QtCore.QRect(60, 0, 171, 17))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 929, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.widget_5 = QtWidgets.QWidget(self.centralwidget)
        self.widget_5.setGeometry(QtCore.QRect(590, 200, 191, 221))
        self.widget_5.setMouseTracking(False)
        self.widget_5.setAutoFillBackground(False)
        self.widget_5.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.widget_5.setObjectName("widget_5")
        self.label_7 = QtWidgets.QLabel(self.widget_5)
        self.label_7.setGeometry(QtCore.QRect(20, 20, 151, 17))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget_5)
        self.label_8.setGeometry(QtCore.QRect(20, 120, 161, 17))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_3.setGeometry(QtCore.QRect(40, 50, 111, 51))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_5)
        self.pushButton_7.setGeometry(QtCore.QRect(40, 150, 111, 51))
        self.pushButton_7.setObjectName("pushButton_7")
        self.widget_8 = QtWidgets.QWidget(self.centralwidget)
        self.widget_8.setGeometry(QtCore.QRect(590, 510, 191, 111))
        self.widget_8.setMouseTracking(False)
        self.widget_8.setAutoFillBackground(False)
        self.widget_8.setStyleSheet("background-color: rgb(222, 221, 218);")
        self.widget_8.setObjectName("widget_8")
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_8.setGeometry(QtCore.QRect(40, 30, 111, 51))
        self.pushButton_8.setObjectName("pushButton_8")
        self.label_6 = QtWidgets.QLabel(self.widget_8)
        self.label_6.setGeometry(QtCore.QRect(55, 0, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Yrsa")
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Myonset App"))
        self.pushButton_2.setText(_translate("MainWindow", "Visualize"))
        self.pushButton_2.clicked.connect(self.visualize)
        self.label_3.setText(_translate("MainWindow", "Pre-Process Data"))
        self.label_5.setText(_translate("MainWindow", "Start by loading the file "))
        self.label_6.setText(_translate("MainWindow", "Open Viz app "))
        self.label_7.setText(_translate("MainWindow", "Segment based on events"))
        self.label_8.setText(_translate("MainWindow", "Run automatic detection"))
        self.pushButton_4.setText(_translate("MainWindow", " Bipolar reference "))
        # self.pushButton_4.clicked.connect(self.get_channel_names)
        self.pushButton_4.clicked.connect(lambda: self.openbipWindow())
        self.pushButton_6.setText(_translate("MainWindow", "Filter EMG"))
        self.pushButton_6.clicked.connect(lambda: self.openfilterwindow())
        self.pushButton.setText(_translate("MainWindow", "Load data"))
        self.pushButton.clicked.connect(self.open_file_dialog)
        self.pushButton_3.setText(_translate("MainWindow", "Segmentation"))
        self.pushButton_3.clicked.connect(self.opensegmentationwindow)
        self.pushButton_7.setText(_translate("MainWindow", "Get onsets"))
        self.pushButton_7.clicked.connect(self.openemgwindow)
        self.pushButton_7.clicked.connect(self.openforcewindow)
        self.pushButton_8.setText(_translate("MainWindow", "Viz"))
        self.pushButton_8.clicked.connect(self.openemgvizwindow)
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave.triggered.connect(self.save)
        self.addAction(self.actionSave)

    def save(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "CSV Files (*.csv)", options=options)
        if file_path:
            self.controller.save(file_path)

    def apply_bipolar_reference(self):

        self.controller.apply_bipolar_reference()

    def extract_events(self):
        # Add your code here to extract events
        self.controller.extract_events()

    def visualize(self):
        self.controller.visualize()

    def open_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filename, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                                  "All Files (*);;Python Files (*.py)", options=options)
        if filename:
            self.controller.open_file(filename)
            self.label_4.setText("The file is loaded !")
            self.extractui = Ui_Extract_events_Window(self)
            # self.extractui.setupexUi(self)
            self.extractui.show()
        # self.trigui = Ui_TriggersWindow(self)
        # self.trigui.setuptrigUi(self)
        # self.trigui.show()

        if __name__ == "__main__":
            app = QApplication([])
            window = EMGWindow(None)
            window.show()
            app = QtWidgets.QApplication(sys.argv)
            MainWindow = QtWidgets.QMainWindow()
            ui = EMGWindow()
            ui.setupUi(MainWindow)
            MainWindow.show()
            sys.exit(app.exec_())
