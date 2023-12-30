from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta

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

with DAG(dag_id = 'hello_world_Bash',
          description='Simple tutorial DAG using BashOperator',
          schedule_interval='0 * * * *',
          default_args=default_args
        ) as dag:  

    hello_operator = BashOperator(task_id='hello_task', 
                              bash_command='echo "Hello, World!"',
                              dag=dag)
    hello_operator




