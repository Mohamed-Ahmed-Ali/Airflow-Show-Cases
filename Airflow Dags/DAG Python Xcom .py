from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def fName():
    return 'Mohamed-Ali'
def Print_Name(ti):
    name=ti.xcom_pull(task_ids='fName')
    print(f"Hello My Name is {name} ")

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


with DAG(dag_id = 'hello_world_Xcom',
          description ='DAG with greeting',
          start_date = datetime(2023, 10, 31),
          schedule_interval='0 * * * *',
          default_args=default_args
        ) as dag:    

    name_Task = PythonOperator(
        task_id='fName',
        python_callable=fName
    )
    
    print_Task = PythonOperator(
        task_id='Print_Name',
        python_callable=Print_Name
    )


    name_Task >> print_Task