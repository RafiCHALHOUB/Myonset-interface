import mne
import matplotlib.pyplot as plt
import logging
import myonset as myo
import sys
from PyQt5.QtWidgets import QFileDialog


class The_Model():
    def __init__(self):
        self.emg_data = None
        self.sfreq = None
        self.events = None
        self.times = None
        self.ch_names = None
        self.ch_selection = None
        self.multich_selection = None
        self.trig_id = {}
        self.emg_id = {}
        self.resp_list = []
        self.mne_events = None
        self.name_bdf = None

    def open_file(self, filename):
        # Load data file
        self.raw = mne.io.read_raw(filename, preload=True, stim_channel='Status')
        self.filename = filename
        print(self.raw)
        print(self.raw.info)
        print(self.raw.ch_names)
        if self.raw is not None:
            print("File loaded")
        else:
            print("File is not loaded")

        self.sfreq = self.raw.info['sfreq']

    def get_channel_names(self):
        return self.raw.ch_names

    def apply_bipolar_reference(self, anode1, cathode1, channel1, anode2, cathode2, channel2):
        # Check if the provided channels are valid
        if not all(ch in self.raw.ch_names for ch in [anode1, cathode1, anode2, cathode2]):
            raise ValueError("Invalid channel(s) provided for bipolar reference.")

        # Check if the new channel names are unique
        if channel1 in self.raw.ch_names or channel2 in self.raw.ch_names:
            raise ValueError(
                "New channel name(s) already exist(s). Please provide unique name(s) for the bipolar channels.")

        # Apply bipolar reference
        mne.set_bipolar_reference(self.raw, anode=[anode1, anode2], cathode=[cathode1, cathode2],
                                  ch_name=[channel1, channel2], copy=False)

        # Get updated channel list
        ch_names2 = self.raw.ch_names

        # Check if the new channels were added
        if channel1 in ch_names2 and channel2 in ch_names2:
            print(ch_names2)
            return ch_names2
        else:
            raise ValueError("Failed to apply bipolar reference.")

    def apply_high_pass_filter(self, selected_channels_hp, low_cutoff):
        # Check if the provided channels are valid
        if not all(ch in self.raw.ch_names for ch in selected_channels_hp):
            raise ValueError("Invalid channel(s) provided.")

        # Apply highpass filter
        self.raw = myo.use_mne.apply_filter(self.raw, ch_names=selected_channels_hp, low_cutoff=low_cutoff)
        logging.info(f"\tHigh pass filtering {len(selected_channels_hp)} channels at {low_cutoff}Hz")

    def apply_low_pass_filter(self, selected_channels_lp, high_cutoff):
        # Check if the provided channels are valid
        if not all(ch in self.raw.ch_names for ch in selected_channels_lp):
            raise ValueError("Invalid channel(s) provided.")

        # Apply lowpass filter
        self.raw = myo.use_mne.apply_filter(self.raw, ch_names=selected_channels_lp, high_cutoff=high_cutoff)
        logging.info(f"\tLow pass filtering {len(selected_channels_lp)} channels at {high_cutoff}Hz")

    def plot_raw(self):
        if self.raw is not None:
            self.raw.plot()
            plt.show()

    def extract_events(self):
        self.mne_events = mne.find_events(self.raw, shortest_event=1)
        self.mne_events[:, 2] = self.mne_events[:, 2] - self.mne_events[:, 1]
        self.events = myo.Events(sample=self.mne_events[:, 0], code=self.mne_events[:, 2],
                                 chan=[-1] * self.mne_events.shape[0],
                                 sf=self.raw.info['sfreq'])
        print(self.events)

    def get_events_ids(self):
        event_ids = self.events.code
        return event_ids

    def segment(self, code_t0, tmin, tmax):
        if self.events.code.dtype.kind == "f" or self.events.code.dtype.kind == "i":
            code_t0 = [int(c) for c in code_t0]

        print(code_t0)
        self.epochs_events = self.events.segment(code_t0=code_t0, tmin=tmin, tmax=tmax)
        print(self.epochs_events)
        self.epoch_time = myo.times(tmin, tmax, self.events.sf)
        t0 = myo.find_times(0, self.epoch_time)

    # def get_channel_indices(self, selected_channels: object) -> object:

    def detectemg(self, selected_channels, onset, offset):
        data_raw = self.raw.get_data(picks=selected_channels)
        data_epochs = self.epochs_events.get_data(data_raw)
        thEMG_raw = 8
        thEMG_tk = 10

        for e in range(self.epochs_events.nb_trials()):
            # Onset and offset EMG detection
            for c in range(data_epochs.shape[1]):
                current = data_epochs[e, c, :]

                # Lcal mBl and stBl are recommended, to use global values, use mBlRaw/mBlTk[c] and stBlRaw/stBlTk[c] computed above
                onsets, offsets = myo.get_onsets(current, self.epoch_time, sf=self.events.sf,
                                                 th_raw=thEMG_raw, use_raw=True, time_limit_raw=.025, min_samples_raw=5,
                                                 varying_min_raw=1, mbsl_raw=None, stbsl_raw=None,
                                                 th_tkeo=thEMG_tk, use_tkeo=True, time_limit_tkeo=.025,
                                                 min_samples_tkeo=5,
                                                 varying_min_tkeo=0, mbsl_tkeo=None, stbsl_tkeo=None)

                # Put in event structure
                onsets_events = myo.Events(sample=onsets, time=self.epoch_time[onsets],
                                           code=[onset] * len(onsets), chan=[selected_channels[c]] * len(onsets),
                                           sf=self.epochs_events.sf)
                offsets_events = myo.Events(sample=offsets, time=self.epoch_time[offsets],
                                            code=[offset] * len(offsets), chan=[selected_channels[c]] * len(offsets),
                                            sf=self.epochs_events.sf)

                # Add in epochs events
                self.epochs_events.list_evts_trials[e].add_events(onsets_events)
                self.epochs_events.list_evts_trials[e].add_events(offsets_events)
        self.events = self.epochs_events.as_continuous(drop_duplic=True)[0]
        print(onset)
        print(onsets_events)

    def detect_force(self, selected_channels, onset, offset, peak):
        th_force = 7
        data_raw = self.raw.get_data(picks=selected_channels)
        data_epochs = self.epochs_events.get_data(data_raw)
        for e in range(self.epochs_events.nb_trials()):
            # Onset and offset force detection
            for c in range(data_epochs.shape[1]):
                current_force = data_epochs[e, c, :]
                force_intervals = myo.detector_var(current_force, self.epoch_time, th=th_force, time_limit=.050,
                                                   sf=self.epochs_events.sf, min_samples=15, varying_min=0,
                                                   use_derivative=True, moving_avg_size=10)

                onsets_force = force_intervals[:, 0]
                offsets_force = force_intervals[:, 1]
                # Put in event structure
                onsets_force_events = myo.Events(sample=onsets_force, time=self.epoch_time[onsets_force],
                                                 code=[onset] * len(onsets_force),
                                                 chan=[selected_channels[c]] * len(onsets_force),
                                                 sf=self.epochs_events.sf)
                offsets_force_events = myo.Events(sample=offsets_force, time=self.epoch_time[offsets_force],
                                                  code=[offset] * len(offsets_force),
                                                  chan=[selected_channels[c]] * len(offsets_force),
                                                  sf=self.epochs_events.sf)

                # Get force peaks
                list_signals = myo.get_signal_portions(current_force, onsets_force_events.lat.sample,
                                                       offsets_force_events.lat.sample)
                _, peak_sample = myo.get_signal_max(list_signals)
                peak_sample += onsets_force_events.lat.sample

                # Put in event structure
                if len(peak_sample) > 0:
                    peaks_force_events = myo.Events(sample=peak_sample, time=self.epoch_time[peak_sample],
                                                    code=[peak] * len(peak_sample),
                                                    chan=[c] * len(peak_sample), sf=self.epochs_events.sf)

                    # Add in epochs events
                    self.epochs_events.list_evts_trials[e].add_events(onsets_force_events)
                    self.epochs_events.list_evts_trials[e].add_events(offsets_force_events)
                    self.epochs_events.list_evts_trials[e].add_events(peaks_force_events)

    def viz(self, code_t0, tmin, tmax, onset, offset):
        if self.events.code.dtype.kind == "f" or self.events.code.dtype.kind == "i":
            code_t0 = [int(c) for c in code_t0]
        data_raw = self.raw.get_data()
        viz = myo.Viz(sys.argv)
        print(data_raw.shape)
        print(code_t0)
        viz.load_data(data_raw, self.events, code_t0,
                      tmin=tmin, tmax=tmax,
                      code_movable_1=onset, code_movable_2=offset,
                      sync_chan=[[0, 1], [0, 1], [2, 3], [2, 3]], random_order=False)
        viz.show()

    def save(self, file_path):
        viz = myo.Viz(sys.argv)
        corrected_events = viz.get_events()
        corrected_events.to_csv(file_path, header="sample,time,code,chan", sep=',',
                                save_sample=True, save_time=True, save_code=True,
                                save_chan=True, save_trial_idx=False)
