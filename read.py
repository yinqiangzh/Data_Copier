import os
import pandas as pd

# BASE_DIR = "D:\\Data_Copier\\retail_data"
# DATA_TRG="D:\\Data_Copier\\csv_data"
# TABLE_LIST=["customers","departments","categories","products","orders","order_items"]



def get_json_reader(base_dir,table_name,chunksize=5000):
    file_name = os.listdir(f"{base_dir}\\{table_name}")[0]
    fp=f"{base_dir}\\{table_name}\\{file_name}"
    return pd.read_json(fp,lines=True,chunksize=chunksize)

def write_to_csv(df,trg_dir,table_name,key):
    min_key= df[key].min()
    max_key=df[key].max()
    df.to_csv(f"{trg_dir}\\{table_name}.csv",mode="a")

if __name__ == "__main__":
    BASE_DIR = os.environ.get("BASE_DIR")
    table_name=os.environ.get("table_name")
    json_reader=get_json_reader(BASE_DIR,table_name)
    for indx,df in enumerate(json_reader):
        print(f"Number of records in chunk with index{idx} is {df.shape()[0]}")
