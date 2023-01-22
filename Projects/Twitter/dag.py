from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime
from etl import run_twitter



default_args = {'owner' : 'airflow',
                'depends_on_past' : False,
                'start_date' : datetime(2023, 1, 21),
                'email' : ['airflow@example.com'],
                'email_on_failure' : False,
                'email_on_retries' : False,
                'retries' : 1,
                'retry_delay' : timedelta(minutes=1)
                }

dag = DAG('twitter',
          default_args = default_args,
          description = 'Twitter and Airflow project')

run_etl = PythonOperator(
    task_id = 'complete_twitter_etl',
    python_callable = run_twitter,
    dag = dag)


run_etl
