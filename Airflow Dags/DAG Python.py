from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta

def print_hello():
    print('Hello, World!')

default_args = {
    'owner': 'Mohamed-Ali',
    'start_date': datetime(2023, 10, 31),
    'email': ['Mohamed.ali.c2021@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    'schedule_interval': '@hourly'
}

with DAG ('hello_world_Python',
          description='Simple tutorial DAG',
          schedule_interval='0 * * * *',
          default_args=default_args
        ) as dag:  

    hello_operator = PythonOperator(task_id='hello_task', 
                                python_callable=print_hello,
                                dag=dag)
    hello_operator
