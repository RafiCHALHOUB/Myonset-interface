# Create a list widget for channel selection
self.ch_selection = QListWidget()
self.ch_selection.addItems(self.ch_names)
self.ch_selection.setSelectionMode(QListWidget.MultiSelection)
for i in range(self.ch_selection.count()):
    item = self.ch_selection.item(i)
    item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
    item.setCheckState(QtCore.Qt.Unchecked)
self.ch_selection.itemChanged.connect(self.plot_raw)

# Create a check box for multi-channel selection
self.multich_selection = QCheckBox('Select all channels')
self.multich_selection.stateChanged.connect(self.plot_raw)

# Show the list widget and check box
self.ch_selection.show()
self.multich_selection.show()


def plot_raw(self):
    # Get the selected channel(s)
    selected_ch = []
    for i in range(self.ch_selection.count()):
        item = self.ch_selection.item(i)
        if item.checkState() == QtCore.Qt.Checked:
            selected_ch.append(item.text())

    # If the "Select all channels" checkbox is checked, plot all channels
    if self.multich_selection.isChecked():
        selected_ch = self.ch_names

    # Check if selected channels are in the list of channel names
    for ch in selected_ch:
        if ch not in self.ch_names:
            print(f"{ch} is not in list of channel names!")
            return

    # Plot the raw data for the selected channel(s)
    fig = self.raw.plot(n_channels=len(selected_ch), duration=10.0, show_scrollbars=False,
                        scalings='auto', remove_dc=True, block=True,
                        start=0, order=[self.ch_names.index(ch) for ch in selected_ch])
    fig.subplots_adjust(top=0.9, hspace=0.5)
    fig.axes[0].set_title(', '.join(selected_ch))

    # Show the plot
    mne.viz.tight_layout()
    mne.viz.show()

    # self.ui.setToolButtonStyle(self,QtCore.Qt.ToolButtonStyle)
    # self.ui.setDocumentMode(False)
    # self.ui.setTabShape(self,QtWidgets.QTabWidget.Rounded)
    # self.ui.setUnifiedTitleAndToolBarOnMac(False)

    def extract_channel_data(self):
        if hasattr(self, 'raw'):
            ch_names = self.raw.info['ch_names']
            ch_data = self.raw.get_data()
            for i in range(len(ch_names)):
                self.channel_data_dict[ch_names[i]] = ch_data[i]
        else:
            print("Error: Data file not loaded yet.")