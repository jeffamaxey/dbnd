import os

import airflow

from airflow import DAG
from airflow.hooks.postgres_hook import PostgresHook
from airflow.operators.python_operator import PythonOperator
from numpy import issubdtype, number

from dbnd import log_dataframe, log_metric


REDSHIFT_CONNECTION_ID = os.getenv("REDSHIFT_CONN", default="redshift_conn")
REDSHIFT_TABLE = os.getenv(
    "REDSHIFT_MONITOR_TARGET_TABLE", default="information_schema.columns"
)
REDSHIFT_TABLE_MONITOR_SCHEDULE = os.getenv(
    "REDSHIFT_TABLE_MONITOR_SCHEDULE", default="@daily"
)
REDSHIFT_MONITOR_TABLE_LIMIT = os.getenv("REDSHIFT_MONITOR_TABLE_LIMIT", default=1000)

# query:
SELECT_DATA = f"SELECT * FROM {REDSHIFT_TABLE} LIMIT %s;"

DEFAULT_ARGS = {
    "owner": "databand",
    "start_date": airflow.utils.dates.days_ago(0),
    "provide_context": False,
}


def monitor_redshift_table(**op_kwarg):
    """Redshift table monitor collects the following metrics:
    - record count
    - duplicate records
    - Null/NaN record counts in each column
    - mean, median, min, max, std of each numeric column
    """

    hook = PostgresHook(REDSHIFT_CONNECTION_ID)
    data = hook.get_pandas_df(SELECT_DATA, parameters=[REDSHIFT_MONITOR_TABLE_LIMIT])

    log_dataframe(
        f"{REDSHIFT_TABLE}",
        data,
        with_histograms=True,
        with_stats=True,
        with_schema=True,
    )

    log_metric("record count", data.shape[0])
    log_metric("Duplicate records", data.shape[0] - data.drop_duplicates().shape[0])
    for column in data.columns:
        log_metric(f"{column} null record count", int(data[column].isna().sum()))

        if issubdtype(data[column].dtype, number):
            log_metric(f"{column} mean", round(data[column].mean(), 2))
            log_metric(f"{column} median", data[column].median())
            log_metric(f"{column} min", data[column].min())
            log_metric(f"{column} max", data[column].max())
            log_metric(f"{column} std", round(data[column].std(), 2))


with DAG(dag_id=f"dbnd_redshift_{REDSHIFT_TABLE}_monitor", schedule_interval=f"{REDSHIFT_TABLE_MONITOR_SCHEDULE}", default_args=DEFAULT_ARGS) as dbnd_template_dag:

    redshift_monitor = PythonOperator(
        task_id="monitor_redshift_table", python_callable=monitor_redshift_table
    )
