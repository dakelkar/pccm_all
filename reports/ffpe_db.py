import sql.add_update_sql as sql
import modules.pccm_names as names
import pandas as pd
import os

class FFPECSVData ():
    def __init__(self, conn, cursor, folder_name, file_name):
        self.table = 'Block_list'
        self.cursor = cursor
        self.folder_name = folder_name
        self.file_name = file_name
        self.conn = conn
        self.columns = ", ".join(names.name_ffpe_csv())

    def read_file(self):
        file_path = os.path.join(self.folder_name, self.file_name)
        new_data = pd.read_csv(file_path)
        new_data = new_data.dropna(axis=0, how='any', thresh=None, subset=['patient_name'], inplace=False)
        return new_data

    def write_file(self, new_data):
        for i in range(0, new_data.shape[0]):
            data_add =list(new_data.loc[i , :]) + [self.file_name]
            sql.insert(self.conn, self.cursor, self.table, self.columns, data_add)


