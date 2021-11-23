"""
Load data from Oracle ADW Database in Admin schema to Custo_Assistencial schema
"""

from datetime import datetime

from airflow import DAG

from lib.operator.hello_operator import HelloOperator
from lib.operator.pokeapi_to_json_operator import PokeAPI_JSON

default_args = {
    "owner": "dev",
    "start_date": datetime(2016, 1, 1),
}

dag = DAG(
    dag_id="00_new_dag",
    schedule_interval=None,
    default_args=default_args,
    catchup=False,
)

dag.doc_md = __doc__

hello_task = HelloOperator(
    task_id="hello_task",
    name="Gabu",
    dag=dag,
)

pokemon_task = PokeAPI_JSON(
    task_id="pokemon_task",
    pokemon="pikachu",
    file_path='/opt/airflow/dags/',
    file_name='pikachu.json',
    http_conn_id = 'pokemon_conn',
    dag=dag,
)

hello_task >> pokemon_task
