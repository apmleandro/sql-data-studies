from sqlalchemy import create_engine
from decouple import config 
import os
import pandas as pd

HOST     = config('HOST')
DATABASE = config('DATABASE')
USER     = config('USER')
PASSWORD = config('PASSWORD')
PORT     = config('PORT')
print(type(PORT))
print(PORT)

conn_string = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'



#'postgresql://postgres:33917577@localhost:5432/olist'

engine = create_engine(conn_string)

directory = r"C:\Users\apmle\OneDrive\Documents\Bootcamp\SQL-STUDIES\sql-data-studies\data\olist"

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)  
    if os.path.isfile(f):
        print(f)
        table_name = os.path.splitext(os.path.basename(f))[0]  
        df = pd.read_csv(f) 
        df.to_sql(table_name, engine, if_exists='replace', index=False)

print('Tables sucessfully uploaded to database')