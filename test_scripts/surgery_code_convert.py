import pandas as pd
import os

folder = 'D:/OneDrive/iiser_data/Prashanti_docs/Database_files/Surgery'

file_coded = 'Reconstruction_nutan_15092018_only_final.csv'
path_coded = os.path.join(folder, file_coded)
data_coded = pd.read_csv(path_coded)
data_dict = {1: 'Right', 2: 'Left', 3: 'Bilateral'}
keys = []
for key in data_dict:
    keys.append

    keys = []
    for key in data_dict[0]:
        keys.append(key)
    index = 0
    patients = pd.DataFrame(columns=keys)
    for patient in patient_list:
        data_list = []
        for key in keys:
            data = patient.get(key)
            data_list.append(data)
        patients.loc[index] = data_list
        index = index + 1