import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd


string_connection= 'postgresql://postgres:33917577@localhost:5432/olist' #DATABASE_URI
conn_olist = create_engine(string_connection)
#Run through files in a given directory
import os
#Assign a directory
directory = r"C:\Users\apmle\OneDrive\Documents\Bootcamp\SQL-STUDIES\sql-data-studies\data\olist"
for filename in os.listdir(directory):
    f = os.path.join(directory, filename) #https://www.geeksforgeeks.org/python-os-path-join-method/?ref=lbp
    # checking if it is a file - os.path.isfile(path) : This function specifies whether the path is existing file or not. 
    if os.path.isfile(f):
        print(f)
        table_name = os.path.splitext(os.path.basename(f))[0]
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv(f)
        # Write the DataFrame to a PostgreSQL table
        table_name = os.path.splitext(os.path.basename(f))[0]
        df.to_sql(table_name, conn_olist, if_exists='replace', index=False)
        