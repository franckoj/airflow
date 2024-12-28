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
    dag_id='dag_one',
    default_args=default_args,
    schedule_interval=None,
    catchup=False,
) as dag_one:

    start_task = DummyOperator(
        task_id='start_task'
    )

    # Trigger the second DAG
    trigger_dag_two = TriggerDagRunOperator(
        task_id='trigger_dag_two',
        trigger_dag_id='second_dag',  # ID of the second DAG,
        conf={"val":"values"},
        wait_for_completion=True,  # Doesn't
    )
    
    end_task = DummyOperator(
        task_id='end_task'
    )
    
    start_task >> trigger_dag_two >> end_task
