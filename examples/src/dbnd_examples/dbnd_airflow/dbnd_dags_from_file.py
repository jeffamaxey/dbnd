from dbnd_airflow.scheduler.dags_provider_from_file import get_dags_from_file


if dags := get_dags_from_file():
    globals().update(dags)
