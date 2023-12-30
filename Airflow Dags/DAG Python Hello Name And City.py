from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def print_hello(name, city):
    print(f'Hello, {name} from {city}!')

    
default_args = {
    'owner': 'Mohamed-Ali',
    'start_date': datetime(2023, 10, 31),
    'email': ['Mohamed.ali.c2021@gmail.com'],
    'email_on_failure': True,
    'email_on_retry': True,
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
    'schedule_interval': '@hourly'
}


with DAG(dag_id = 'hello_world_With_Variables',
          description ='DAG with greeting',
          start_date = datetime(2023, 10, 31),
          schedule_interval='0 * * * *',
          default_args=default_args
        ) as dag:    

    hello_operator = PythonOperator(task_id='hello_task', 
                                python_callable=print_hello,
                                op_kwargs={'name': 'Mohamed', 'city': 'Alexandria'}
                                )
    hello_operator
