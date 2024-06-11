# Airflow-project/DAG/dag_csv_to_json_csv.py
from datetime import datetime, timedelta
import datetime as dt
import pandas as pd
from os import path
from pathlib import Path
from airflow import DAG
#from airflow.operators.dummy import DummyOperator   
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = '/airflow-project/data_input.csv'

def csvToJson():
    df=pd.read_csv(DATA_PATH)

# Define the default_args
default_args = {
    'owner': 'agung',
    'start_date': dt.datetime(2024, 6, 10),
    'retries': 12,
    'retry_delay': dt.timedelta(minutes=5),
}
# Function to convert CSV to JSON
def csv_to_json(**kwargs):
    input_csv = '/workspaces/Setup-airflow-on-virtual-environtment/airflow-project/data_input.csv'
    output_json = '/workspaces/Setup-airflow-on-virtual-environtment/airflow-project/data_output.csv'
    df = pd.read_csv(input_csv)
    df.to_json(output_json, orient='records', lines=True)

# Function to convert JSON back to CSV
def json_to_csv(**kwargs):
    input_json = '/workspaces/Setup-airflow-on-virtual-environtment/airflow-project/data_output.csv'
    output_csv = '/workspaces/Setup-airflow-on-virtual-environtment/airflow-project/data_reportFIX.csv'
    df = pd.read_json(input_json, orient='records', lines=True)
    df.to_csv(output_csv, index=False)

# Define the DAG
with DAG(
    'csv_to_json_to_csv ',
    default_args=default_args,
    description='A simple DAG to convert CSV to JSON and back to CSV',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 6, 10),
    catchup=False,) as dag:
#Define the tasks
    csv_to_json_task = PythonOperator(
        task_id='csv_to_json',
        python_callable=csv_to_json,
        dag=dag,)

    json_to_csv_task = PythonOperator(
        task_id='json_to_csv',
        python_callable=json_to_csv,
        dag=dag,)

# Setting up Task dependencies using Airflow standard notations        
#Set the task dependencies
csv_to_json_task >> json_to_csv_task