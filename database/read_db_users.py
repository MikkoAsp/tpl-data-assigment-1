import pandas as pd
from database.connection import engine

#Read the users table in the database and return it as a dataframe
def read_db_users():
    try:   
        df = pd.read_sql("users", engine)
        return df
    except pd.errors.DatabaseError as e:
        print("Missing users table in database: ", e)
        return pd.DataFrame()