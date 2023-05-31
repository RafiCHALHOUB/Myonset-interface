from PyQt5.QtWidgets import QApplication
from Model import The_Model


class TheController:
    def __init__(self):
        from TriggersWindow import Ui_TriggersWindow
        from view import EMGWindow  # import EMGWindow here to avoid circular import
        self.model = The_Model()
        self.view = EMGWindow(self)

        self.view.show()

    def open_file(self, filename):
        # Ask for file name
        if filename:
            print("File exists")
            # Load file into the model 
            return str(self.model.open_file(filename))
        else:
            print("Please select an existing file")

    def get_channel_indices(self, selected_channels):
        self.model.get_channel_indices(selected_channels)

    def get_channel_names(self):
        return self.model.get_channel_names()

    def extract_events(self):
        self.model.extract_events()

    def get_events_ids(self):
        return self.model.get_events_ids()

    def apply_low_pass_filter(self, selected_channels_lp, high_cutoff):
        self.model.apply_low_pass_filter(selected_channels_lp, high_cutoff)

    def apply_high_pass_filter(self, selected_channels_hp, low_cutoff):
        self.model.apply_high_pass_filter(selected_channels_hp, low_cutoff)

    def visualize(self):
        self.model.plot_raw()

    def apply_bipolar_reference(self, anode1, cathode1, channel1, anode2, cathode2, channel2):
        self.model.apply_bipolar_reference(anode1, cathode1, channel1, anode2, cathode2, channel2)

    def segment(self, code_t0, tmin, tmax):
        self.model.segment(code_t0, tmin, tmax)

    def detect_force(self, selected_channels, onset, offset, peak):
        self.model.detect_force(selected_channels, onset, offset, peak)

    def detect_emg(self, selected_channels, onset, offset):
        self.model.detectemg(selected_channels, onset, offset)

    def viz(self, code_t0, tmin, tmax, onset, offset):
        self.model.viz(code_t0, tmin, tmax, onset, offset)

    def save(self, file_path):
        self.model.save(file_path)


if __name__ == "__main__":
    app = QApplication([])
    controller = TheController()
    app.exec_()
