from PyQt5 import QtWidgets, QtGui


class TriggerDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Set Trigger Values')

        # Create the labels and line edits for trigger values
        self.red_left_label = QtWidgets.QLabel('Red Left:')
        self.red_left_edit = QtWidgets.QLineEdit()
        self.red_right_label = QtWidgets.QLabel('Red Right:')
        self.red_right_edit = QtWidgets.QLineEdit()
        self.green_left_label = QtWidgets.QLabel('Green Left:')
        self.green_left_edit = QtWidgets.QLineEdit()
        self.green_right_label = QtWidgets.QLabel('Green Right:')
        self.green_right_edit = QtWidgets.QLineEdit()
        self.onset_label = QtWidgets.QLabel('Onset:')
        self.onset_edit = QtWidgets.QLineEdit()
        self.offset_label = QtWidgets.QLabel('Offset:')
        self.offset_edit = QtWidgets.QLineEdit()
        self.peak_label = QtWidgets.QLabel('Peak:')
        self.peak_edit = QtWidgets.QLineEdit()
        self.resp_list_label = QtWidgets.QLabel('Response Triggers:')
        self.resp_list_edit = QtWidgets.QLineEdit()

        # Create the Extract Events button
        self.extract_button = QtWidgets.QPushButton('Extract Events')
        self.extract_button.clicked.connect(self.extract_events)

        # Create the layout and add the widgets to it
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.red_left_label, 0, 0)
        layout.addWidget(self.red_left_edit, 0, 1)
        layout.addWidget(self.red_right_label, 1, 0)
        layout.addWidget(self.red_right_edit, 1, 1)
        layout.addWidget(self.green_left_label, 2, 0)
        layout.addWidget(self.green_left_edit, 2, 1)
        layout.addWidget(self.green_right_label, 3, 0)
        layout.addWidget(self.green_right_edit, 3, 1)
        layout.addWidget(self.onset_label, 4, 0)
        layout.addWidget(self.onset_edit, 4, 1)
        layout.addWidget(self.offset_label, 5, 0)
        layout.addWidget(self.offset_edit, 5, 1)
        layout.addWidget(self.peak_label, 6, 0)
        layout.addWidget(self.peak_edit, 6, 1)
        layout.addWidget(self.resp_list_label, 7, 0)
        layout.addWidget(self.resp_list_edit, 7, 1)
        layout.addWidget(self.extract_button, 8, 0, 1, 2)
        self.setLayout(layout)

        # def set_triggers(self):
        # Get the trigger values from the line edits
        # trig_id = {
        #     'red_left': int(self.red_left_edit.text()),
        #      'red_right': int(self.red_right_edit.text()),
        #     'green_left': int(self.green_left_edit.text()),
        #     'green_right': int(self.green_right_edit.text())
        # }
        emg_id = {
            'onset': int(self.onset_edit.text()),
            'offset': int(self.offset_edit.text()),
            'peak': int(self.peak_edit.text())
        }
        resp_list = [int(x) for x in self.resp_list_edit.text().split()]
        return trig_id, emg_id, resp_list
        # Return the trigger values
        self.trigger_values = (trig_id, emg_id, resp_list)
        self.accept()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    dialog = TriggerDialog()
    if dialog.exec_() == QtWidgets.QDialog.Accepted:
        print(dialog.trig_id, dialog.emg_id, dialog.resp_list)
    sys.exit(app.exec_())
