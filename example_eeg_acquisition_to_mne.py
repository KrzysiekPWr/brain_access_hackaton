""" EEG measurement example

Example how to get measurements and
save to fif format
using acquisition class from brainaccess.utils

Change Bluetooth device name (line 23)
"""

from audioop import bias
from weakref import ref
import matplotlib.pyplot as plt
import matplotlib
import time
from scipy.signal import resample
import mne

from brainaccess.utils import acquisition
from brainaccess.core.eeg_manager import EEGManager

matplotlib.use("TKAgg", force=True)

eeg = acquisition.EEG()

# define electrode locations
cap: dict = {
    0: "F3",
    1: "F4",
    2: "C3",
    3: "C4",
    4: "P3",
    5: "PO4",
    6: "O1",
    7: "O2",
}

# define device name
device_name = "BA MINI 015"

# start EEG acquisition setup
with EEGManager() as mgr:
    eeg.setup(mgr, device_name=device_name, cap=cap)
    
    while True:
        # Start acquiring data
        eeg.start_acquisition()
        time.sleep(3)

        start_time = time.time()
        annotation = 1
        while time.time() - start_time < 10:
            time.sleep(1)
            # send annotation to the device
            print(f"Sending annotation {annotation} to the device")
            eeg.annotate(str(annotation))
            annotation += 1

        # get all eeg data and stop acquisition
        eeg.get_mne()
        eeg.stop_acquisition()
        print (time.time())
        print (eeg.info)

    mgr.disconnect()

# save EEG data to MNE fif format
eeg.data.save(f'{time.strftime("%Y%m%d_%H%M")}-raw.fif')

# Close brainaccess library
eeg.close()
# Show recorded data
print (eeg.info)

eeg.data.mne_raw.filter(1, 40).plot(scalings="auto", verbose=False)


plt.show()

