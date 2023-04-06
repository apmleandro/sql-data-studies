import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd

#criar string de coneccao- Basicamente criar uma variavel string com a direcao a base de dados no postgres ja com 
# as informacoes como senha do postgres, o endereco do local host e o nome da data base
string_connection= 'postgresql://postgres:33917577@localhost:5432/olist' #DATABASE_URI

# criar uma engine que sera criada usando a a funcao create_engine do sqlalchemy que cria a conecao 
# com o endereco da data base
# The create_engine() function in SQLAlchemy is used to create a connection to a database. 
# It takes a connection string as an argument, which specifies the location and credentials 
# needed to connect to a particular database.

# The connection string usually includes information such as the database type, host name or IP address,
# port number, and authentication details.
# Once you have created the Engine object, you can use it to create Connection objects, which represent individual
# database sessions. You can then use these Connection objects to execute SQL queries and manage database transactions.

engine = create_engine(string_connection)
# The create_engine() function returns an instance of the Engine class, which represents the database connection. 
# This Engine object provides a number of methods for interacting with the database, such as executing SQL queries, 
# managing transactions, and reflecting database schema information.

# Run through files in a given directory
# os - This module provides a portable way of using operating system dependent functionality.
# If you just want to read or write a file see open(), if you want to manipulate paths, see the os.path module, 
# and if you want to read all the lines in all the files on the command line see the fileinput module. 
# For creating temporary files and directories see the tempfile module, and for high-level file and directory 
# handling see the shutil module.
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
        # DataFrame.to_sql(name, con, schema=None, if_exists='fail', index=True, index_label=None, 
        # chunksize=None, dtype=None, method=None)

        # if_exists{‘fail’, ‘replace’, ‘append’}, default ‘fail’
        # How to behave if the table already exists.
        # fail: Raise a ValueError.
        # replace: Drop the table before inserting new values.
        # append: Insert new values to the existing table.

        # index - Write DataFrame index as a column. Uses index_label as the column name in the table.

        # index_label - str or sequence, default None
        # Column label for index column(s). If None is given (default) and index is True, 
        # then the index names are used. A sequence should be given if the DataFrame uses MultiIndex.

        df.to_sql(table_name, engine, if_exists='replace', index=False)

print('Tables sucessfully uploaded to database')
        