from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable

from common.loader import hello_world

# Default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 1, 1),
    'retries': 1,
}

var = Variable.get("greet")

import configparser

config = configparser.ConfigParser()
config.read('/opt/airflow/dags/common/config.cfg')

ips = config['database']['host']

# Define the DAG
with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=None,  # Set to None for manual execution
    catchup=False,
) as dag:

    # for i in ips:

        # Define the task
        hello_world_task = PythonOperator(
            task_id=f'{ips}_hello_world_task',
            python_callable=hello_world,
            op_args={"n":5,"a":4}
        )

        # Define task dependencies (if any)
        hello_world_task
