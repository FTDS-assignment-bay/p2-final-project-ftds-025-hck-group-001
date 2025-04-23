'''
=========================================================
Final Project

This program is made to automate the process of loading
and transforming data from PostgreSQL.

=========================================================
'''

# Import Libraries
from datetime import datetime
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
import pandas as pd
import psycopg2
from sqlalchemy import create_engine

# 1. FETCH DATA
def fetch():
    '''
    This function is used to fetch data from PostgreSQL. The data later will be processed
    in the next function.
    '''
    # Start connection between psycopg2 and postgres
    conn = psycopg2.connect(
        dbname="finpro_hck_025",
        user="postgres",
        password="postgres",
        host="postgres", 
        port="5432"
    )

    # Find the designated data in postgres and save it in "df" variable
    df = pd.read_sql_query("SELECT * FROM table_finpro", conn)

    # Export the data in "df" to a csv file
    df.to_csv("/opt/airflow/data/Finpro_data_raw.csv", index=False)

    # Close connection
    conn.close()

# 2. CLEAN DATA
def clean():
    '''
    This function is used to process the previously fetched data.

    Processes:

    '''
    # Read the previously fetched data
    df = pd.read_csv("/opt/airflow/data/Finpro_data_raw.csv")

    # Function to normalize data
    df.drop(columns=['unnamed_0', 'unnamed_01'], inplace=True) # Drop the first column
    df.drop_duplicates(inplace=True) # Drop duplicates 
    df.dropna(inplace=True) # Drop duplicates   

    # Convert data type to datetime
    df["trans_date_trans_time"] = pd.to_datetime(df["trans_date_trans_time"])
    df["dob"] = pd.to_datetime(df["dob"])
    df["unix_time"] = pd.to_datetime(df["unix_time"], origin='unix', unit='s')

    # Replace commas with dots and convert to numeric
    comma_to_float_cols = ["amt", "lat", "long", "merch_lat", "merch_long"]
    for col in comma_to_float_cols:
        df[col] = df[col].str.replace(",", ".").astype(float)

    # Delete rows with 'fraud' in the 'merchant' column
    df['merchant'] = df['merchant'].str.replace("fraud", "")

    # 4. Strip spaces and and replace underscores with spaces in categorical columns
    cat_cols = ["merchant", "category", "first", "last", "gender", "street", "city", "state", "job"]
    for col in cat_cols:
        df[col] = df[col].str.strip()
        df[col] = df[col].str.replace("_", " ")

    # Drop duplicates
    df = df.drop_duplicates()

    # Drop missing values
    df = df.dropna()

    # Export the processed data to a new csv file
    df.to_csv("/opt/airflow/data/Finpro_data_clean.csv", index=False)

# 3. POST TO POSTGRESQL
def post():
    '''
    This function is used to post the processed data to PostgreSQL.
    '''

    # Create a SQLAlchemy engine for PostgreSQL
    engine = create_engine('postgresql+psycopg2://postgres:postgres@postgres:5432/finpro_hck_025')
    conn = engine.connect()

    # Read the data we want to send
    df = pd.read_csv("/opt/airflow/data/Finpro_data_clean.csv")

    # Send the data to PostgreSQL
    df.to_sql('table_finpro_cleaned', conn, if_exists='replace', index=False)

# Define DAG
default_args = {
    'owner': 'thaliban',
    'start_date': datetime(2024, 4, 23),
    'retries': 1
}

with DAG(
    # Define initial parameters
    dag_id='finpro_data_pipeline',
    default_args=default_args,
    schedule_interval="@daily",
    catchup=False,
    description="Fetch -> Clean -> Post") as dag:

    # Define operations within the DAG

    # Fetch Data
    fetch_data = PythonOperator(
        task_id='fetch_from_postgresql',
        python_callable=fetch
    )
    # Clean Data
    clean_data = PythonOperator(
        task_id='data_cleaning',
        python_callable=clean
    )
    # Post Data
    post_data = PythonOperator(
        task_id='post_to_postgresql',
        python_callable=post
    )

    # DAG Flow
    fetch_data >> clean_data >> post_data
