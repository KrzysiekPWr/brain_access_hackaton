import mne
from scipy.io import savemat

# Wczytaj plik .fif
fif_file = './20241116_2218-raw.fif'
raw = mne.io.read_raw_fif(fif_file, preload=True)

# Wybierz jeden kanał (np. pierwszy kanał z listy)
channel_name = raw.info['ch_names'][0]  # Możesz zmienić na inny kanał
raw.pick_channels([channel_name])  # Wybierz tylko ten kanał

# Pobierz dane z wybranego kanału
data = raw.get_data()  # Dane dla jednego kanału (1 x próbki)
data = data.flatten()  # Spłaszczenie danych do formy wektora

# Pobierz metadane
sfreq = raw.info['sfreq']  # Częstotliwość próbkowania
times = raw.times  # Znaczniki czasu

# Przygotuj strukturę do zapisu w .mat
mat_dict = {
    'data': data,        # Dane dla jednego kanału
    'sfreq': sfreq,      # Częstotliwość próbkowania
    'times': times       # Czas w sekundach
}

# Zapisz dane do pliku .mat
mat_file = 'plik_wyjsciowy2.mat'
savemat(mat_file, mat_dict)

print(f'Plik został zapisany jako {mat_file}')
