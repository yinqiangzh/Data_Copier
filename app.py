import pandas as pd
import sqlalchemy as sq
import os
import sys
import pyodbc
import pyarrow as pa
import numpy as np
from read import get_json_reader,write_to_csv

BASE_DIR="D:\\Data_Copier\\retail_data"
DATA_SRC_DEPT="retail_data\\departments\\part-r-00000-3db7cfae-3ad2-4fc7-88ff-afe0ec709f49"
DATA_SRC_CAT="retail_data\\categories\\part-r-00000-ce1d8208-178d-48d3-bfb2-1a97d9c05094"
DATA_SRC_CUST="retail_data\\customers\\part-r-00000-70554560-527b-44f6-9e80-4e2031af5994"
DATA_SRC_ORDITEM="retail_data\\order_items\\part-r-00000-6b83977e-3f20-404b-9b5f-29376ab1419e"
DATA_SRC_ORD="retail_data\\orders\\part-r-00000-990f5773-9005-49ba-b670-631286032674"
DATA_SRC_PROD="retail_data\\products\\part-r-00000-990f5773-9005-49ba-b670-631286032674"

DATA_SRC_PARQUET="retail_data\\parquet\\userdata1.parquet"

DATA_TRG="D:\\Data_Copier\\csv_data"
TABLE_LIST=["customers","departments","categories","products","orders","order_items"]

def main():
    for table_name in TABLE_LIST:
        process_table_load(BASE_DIR, table_name)


def process_table_load(BASE_DIR, table_name):
    json_reader = get_json_reader(BASE_DIR, table_name)
    for df in json_reader:
        write_to_csv(df,DATA_TRG, table_name, df.columns[0])


# file_name=os.listdir(f"{BASE_DIR}\\retail_data\\orders")[0]
# print(file_name)

if __name__ == "__main__":
    main()

# users =[{"User_id":201,"User_name":"John Smith"},{"User_id":405,"User_name":"Peter Yang"}]
# df=pd.DataFrame(users)
# print(df)
# #df=pd.read_json(DATA_SRC_DEPT,lines=True)
# df2= pd.read_parquet(DATA_SRC_PARQUET,engine='pyarrow')
# print(df2.head())
#print(df[df["order_status"]=="PENDING_PAYMENT"].head())

#for idx, df in enumerate(json_reader):
#     print(f'Number of records in chunk with index {idx} is {df.shape[0]}')