# brain_access_hackaton
Automatic maintenance of a stable patient condition. The algorithm will automatically administer medicine dosage to maintain a level of deep anesthesia or sedation based on the **Bispectral Index -** a value ranging from 0 to 100 which indicates brain activity.  Maintaining values between 40-60 is essential to prevent patients from regaining awareness during a procedure.

Implementing such an algorithm could significantly enhance the effectiveness and safety of medical procedures, particularly in said general anesthesia and sedation. Automating drug administration based on BIS (Bispectral Index) analysis could minimize risks associated with under- or over-administering anesthetic agents, leading to more stable vital signs. This system could respond to sudden changes in a patient's condition faster than a human which proves to be crucial in critical situations or for patients with unstable vitals. It would also free up anesthesiologists to focus on other aspects of patient care, intervening only when specialist oversight is necessary. Furthermore, precise drug dosing control could speed up patient recovery, shorten post-procedure wake-up times, and reduce side effects from prolonged anesthetic use. This technology could prove invaluable in intensive care settings, where continuous sedation level monitoring is vital.

We were able to collect continuous data form BrainAccess MINI device by taking consecutive 10-second samples of EEG data. This data was then used to calculate BIS. This data can be then used as an input to a medicine administration function.

Risks:

1. Overdosing
In effect of a calibration error or delay in feedback its possible for system to deliver excessive amount of medicine, which can lead to serious consequences
2. Underdosing
Insufficient anesthesia could result in intraoperative awareness, causing psychological trauma
3. Interference
Electrical interference may affect BIS readings, which can lead to mistakes in supply of medicine
4. Delay
Time is needed to make medicine work and get a feedback, so we have to be aware of it.

To prevent unexpected behavior and minimalize potential risks its neccessary for doctors to have everything under control throughout all the time and stay focused. The system task is to only support a doctors job.
