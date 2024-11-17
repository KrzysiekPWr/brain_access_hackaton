from oct2py import Oct2Py, get_log
import numpy as np
import scipy.signal as signal
import scipy.io
import logging
import matplotlib.pyplot as plt


import mne
from scipy.io import savemat

# Odczytaj plik .fif
fif_file = "./eeg_data.fif"
raw = mne.io.read_raw_fif(fif_file, preload=True)

# Pobierz dane EEG i metadane
data, times = raw.get_data(return_times=True)  # Dane EEG (kanały x próbki)

sfreq = raw.info["sfreq"]  # Częstotliwość próbkowania
ch_names = raw.info["ch_names"]  # Nazwy kanałów

# Przygotuj dane do zapisu w formacie .mat
mat_data = {
    "data": data,  # Sygnały EEG
    "times": times,  # Oś czasu
    "sfreq": sfreq,  # Częstotliwość próbkowania
    "ch_names": ch_names,  # Nazwy kanałów
}

# Zapisz dane do pliku .mat
mat_file = "eeg_text_data_1.mat"
savemat(mat_file, mat_data)

print(f"Plik zapisano jako {mat_file}")


oc = Oct2Py(logger=get_log())

oc.logger = get_log("new_log")
oc.logger.setLevel(logging.INFO)


oc.eval("pkg load control")
oc.eval("pkg load signal")
oc.eval("pkg load statistics")

result = oc.eval("openibis()")

# print(result)

# print(type(result))


bis_values = np.array(result).transpose()[0]

print(bis_values)


stride = 0.5  # Assuming a 0.5-second stride as per your Octave function
# bis_times = np.arange(0, len(bis) * stride, stride)  # Create time axis for BIS


bis_values = signal.resample(
    bis_values, len(times)
)  # Resample BIS to match EEG data length
print(bis_values)
# print(bis_times)

eeg_data = raw.get_data()
print(eeg_data)

print(eeg_data.shape)


# --- Medicine and Patient Classes ---
class Medicine:
    def __init__(self, name, dose, reduction_of_bis):
        self.name = name
        self.dose = dose
        self.reduction_of_bis = reduction_of_bis

    def __str__(self):
        return f"{self.name} (Dose: {self.dose}, Reduction: {self.reduction_of_bis})"


class Patient:
    def __init__(self, sex, age, weight, height, bis, medicine_potency_resistance):
        self.sex = sex
        self.age = age
        self.weight = weight
        self.height = height
        self.bis = bis.copy()
        self.medicine_potency_resistance = medicine_potency_resistance
        self.medication = []

    def __str__(self):
        return (
            f"Patient: {self.sex}, Age: {self.age}, Weight: {self.weight}, Height: {self.height}, "
            f"Medicine Potency Resistance: {self.medicine_potency_resistance}"
        )

    def apply_resistance(self, bis_value):
        if bis_value < 10:
            return bis_value
        return bis_value + self.medicine_potency_resistance

    # def update_bis(self):
    #     for i in range(len(self.bis)):
    #         self.bis[i] = self.bis[i] - 10


print(p.bis)


fig = plt.figure()

# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)

ax1 = fig.add_subplot(1, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)
ax3 = fig.add_subplot(3, 1, 3)


times = times[1000:-1000]

for i in range(0, 8):
    eeg_data[i] = eeg_data[i][1000:-1000]

bis_values = bis_values[1000:-1000]


# Initialize Patient and Medicine
used_medicine = Medicine("Propofol", 5, 10)
p = Patient("man", 30, 70, 180, bis_values.copy(), 0.0)
p.medication.append(used_medicine)


for i in range(0, 8):
    ax1.plot(times, eeg_data[i], label=f"EEG data {i}")
# ax1.plot(times, eeg_data[0], label='data 1')


ax2.plot(times, p.bis, label="BIS data before medication", color="red")


for i in range(len(p.bis)):
    p.bis[i] = p.bis[i] - (
        p.medication[0].dose * p.medication[0].reduction_of_bis * i
    )

print(p.bis)


ax3.plot(times, p.bis, label="BIS data after medication", color="green")


ax1.set_xlabel("Time (s)")
ax1.set_ylabel("EEG data")


ax2.set_xlabel("Time (s)")
ax2.set_ylabel("BIS data before medication")

ax3.set_xlabel("Time (s)")
ax3.set_ylabel("BIS data after medication")

# Show the plot
plt.show()
