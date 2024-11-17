import mne
from scipy.io import savemat

# Odczytaj plik .fif
fif_file = "./20241117_0124-raw.fif"
raw = mne.io.read_raw_fif(fif_file, preload=True)

# Pobierz dane EEG i metadane
data, times = raw.get_data(return_times=True)  # Dane EEG (kanały x próbki)
sfreq = raw.info['sfreq']  # Częstotliwość próbkowania
ch_names = raw.info['ch_names']  # Nazwy kanałów

# Przygotuj dane do zapisu w formacie .mat
mat_data = {
    "data": data,           # Sygnały EEG
    "times": times,         # Oś czasu
    "sfreq": sfreq,         # Częstotliwość próbkowania
    "ch_names": ch_names,   # Nazwy kanałów
}

# Zapisz dane do pliku .mat
mat_file = "example_data12_new_new.mat"
savemat(mat_file, mat_data)

print(f"Plik zapisano jako {mat_file}")
