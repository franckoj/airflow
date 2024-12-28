from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'start_date': days_ago(1),
}

with DAG(
    dag_id='second_dag',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag_one:

    start_task = DummyOperator(
        task_id='second_start_task'
    )

    end_task = DummyOperator(
        task_id='second_end_task'
    )
    
    start_task >> end_task
