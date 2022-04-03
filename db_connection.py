import pyodbc
from sqlalchemy import create_engine
import pandas as pd

from sqlalchemy.engine import URL

import pypyodbc

connection = pypyodbc.win_connect_mdb("D:\\Data_Copier\\Access_db\\retail.accdb")

# connection_string = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=dagger;DATABASE=test;UID=user;PWD=password"
# connection_url = URL.create("mssql+pyodbc", query={"odbc_connect": connection_string})
#
# connection_string = "DRIVER={Microsoft Access Driver (*.mdb, *.accdb);DBQ=D:\\Data_Copier\\Access_db\\retail.accdb;"
# connection_url = URL.create("access+pyodbc", query={"odbc_connect": connection_string})
#
# engine = create_engine(connection_url)
# df = pd.read_sql("select * from TestTbl",engine)

class MSAccessConnector:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def test_connection(self):
        try:

            conn = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=D:\Data_Copier\Access_db\retail.accdb;')

            # cursor = conn.cursor()
            #return conn
            str_sql = "select * from TestTbl"
            df = pd.read_sql(str_sql, conn)
            print(df.count())
        except Exception as e:
            print(e)
        finally:
            conn.close()

#cn=MSAccessConnector().test_connection()
