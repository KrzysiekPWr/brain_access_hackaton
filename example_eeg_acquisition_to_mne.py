import matplotlib.pyplot as plt
import time
from brainaccess.utils import acquisition
from brainaccess.core.eeg_manager import EEGManager
import mne
import numpy as np

# Initialize EEG acquisition
eeg = acquisition.EEG()

Fs = 128  # Initial sampling frequency in Hz
T = 1 / Fs  # Interval between samples (seconds)
new_fs = 128
# Define electrode locations
cap = {
    0: "F3",
    1: "F4",
    2: "C3",
    3: "C4",
    4: "P3",
    5: "P4",
    6: "O1",
    7: "O2",
}

# Define device name
device_name = "BA MIDI 015"

# Start EEG acquisition setup
with EEGManager() as mgr:
    eeg.setup(mgr, device_name=device_name, cap=cap)

    # Start acquiring data
    eeg.start_acquisition()
    time.sleep(1)

    start_time = time.time()
    annotation = 1
    while time.time() - start_time < 200:
        time.sleep(1)
        # Send annotation to the device
        print(f"Sending annotation {annotation} to the device")
        eeg.annotate(str(annotation))
        annotation += 1

    # Get all EEG data and stop acquisition
    eeg.get_mne()
    eeg.stop_acquisition()
    eeg.data.mne_raw.resample(new_fs)
    eeg.data.save(f'{time.strftime("%Y%m%d_%H%M")}-raw.fif')
    mgr.disconnect()

# Check sampling frequency (existing sample rate)
sampling_frequency = eeg.data.mne_raw.info['sfreq']
print(f"Sampling Frequency: {sampling_frequency} Hz")

# Plot the Power Spectral Density (PSD)
eeg.data.mne_raw.plot_psd(fmax=50)
low_freq = 8  # Hz
high_freq = 12  # Hz

# Apply a bandpass filter for the alpha band
eeg.data.mne_raw.filter(low_freq, high_freq)
# Plot the filtered data (for alpha band)
eeg.data.mne_raw.plot(scalings="auto", verbose=False)
# Show the frequency content using FFT
data = eeg.data.mne_raw.get_data()  # Get the EEG signal
data = data[0]  # First channel (adjust as needed)
fft_values = np.fft.fft(data)
frequencies = np.fft.fftfreq(len(data), 1 / sampling_frequency)
positive_frequencies = frequencies[:len(data) // 2]
positive_fft_values = np.abs(fft_values)[:len(data) // 2]

# Plot the FFT (frequency content)
plt.figure(figsize=(10, 6))
plt.plot(positive_frequencies, positive_fft_values)
plt.title("EEG Signal Frequency Content (FFT)")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.grid(True)
plt.show()
# Close BrainAccess library
eeg.close()

plt.show()
