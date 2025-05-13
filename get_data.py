from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.empty import EmptyOperator
from datetime import datetime
from data_utils import get_data

with DAG(
    dag_id='get_data',
    start_date=datetime(2024, 4, 25),
    schedule_interval='@daily',  # run every day
    catchup=False,
    tags=['data_pipeline', 'preprocessing']
) as dag:

    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')

    preprocess_task = PythonOperator(
        task_id='get_data',
        python_callable=get_data
    )

    # Set task dependencies
    start >> preprocess_task >> end