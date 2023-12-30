from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def fNames(ti):
    ti.xcom_push(key='Frist_Name' , value='Mohamed')
    ti.xcom_push(key='Lastt_Name' , value='Ali')


def fAge_Citys(ti):
    ti.xcom_push(key='age' , value='26')
    ti.xcom_push(key='city' , value='Alexandria')

def Prints(ti):
    Frist_Name = ti.xcom_pull(task_ids='fNames', key='Frist_Name')
    Last_Name = ti.xcom_pull(task_ids='fNames', key='Last_Name')
    Age = ti.xcom_pull(task_ids='fAge_Citys', key='age')
    City = ti.xcom_pull(task_ids='fAge_Citys', key='city')
    print(f"Hello My Name is {Frist_Name} {Last_Name} , I'm {Age} Years Old , From {City}")

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


with DAG(dag_id = 'XCom_Pull_Push',
          description ='DAG with greeting',
          start_date = datetime(2023, 10, 31),
          schedule_interval='0 * * * *',
          default_args=default_args
        ) as dag:    

        name_Tasks = PythonOperator(
            task_id='fNames',
            python_callable=fNames
        )

        age_city_Tasks = PythonOperator(
            task_id='fAge_Citys',
            python_callable=fAge_Citys
        )

        print_Tasks = PythonOperator(
            task_id='Prints',
            python_callable=Prints
        )


        [name_Tasks ,age_city_Tasks] >> print_Tasks