from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup
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

ips = ["group_task1","group_task2"]#config['database']['host']

# Define the DAG
with DAG(
    dag_id='hello_world_dag',
    default_args=default_args,
    description='A simple Hello World DAG',
    schedule_interval=None,  # Set to None for manual execution
    catchup=False,
) as dag:
    
    task1= PythonOperator(
        task_id="task_1",
        python_callable=hello_world,
        op_args={"n": 5, "a": 4}
    )
    task2= PythonOperator(
        task_id="task_2",
        python_callable=hello_world,
        op_args={"n": 5, "a": 4}
    )



        
 
    def task_group_tb():
        g = []
        
        for i in ips:
            with TaskGroup(f"gro{i}") as group:

                # Define the task
                hello_world_task1 = PythonOperator(
                    task_id=f'{i}_hello_world_task1',
                    python_callable=hello_world,
                    op_args={"n":5,"a":4}
                )
                # Define the task
                hello_world_task2 = PythonOperator(
                    task_id=f'{i}_hello_world_task2',
                    python_callable=hello_world,
                    op_args={"n":6,"a":4}
                )

                # Define task dependencies (if any)
                hello_world_task1 >> hello_world_task2
        g.append(group)
        return g

    with TaskGroup(f"gro") as groups:
        task_group_tb()

    task3= PythonOperator(
        task_id="task_3",
        python_callable=hello_world,
        op_args={"n": 5, "a": 4}
    )
    task4= PythonOperator(
        task_id="task_4",
        python_callable=hello_world,
        op_args={"n": 5, "a": 4}
    )

    task1 >> task2 >> groups >> task3 >> task4