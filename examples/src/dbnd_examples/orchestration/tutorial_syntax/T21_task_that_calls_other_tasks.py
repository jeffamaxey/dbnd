import pandas as pd

from dbnd import task


@task
def task_that_spawns(value=1.0):
    # type: (float)-> float

    value_task = task_that_runs_inline.task(value=value)
    value_task.dbnd_run()

    return value_task.result.read_pickle() + 0.1


@task
def task_that_runs_inline(value=1.0):
    # type: (float)-> float
    return value + 0.1


@task
def func_return_df():
    return pd.DataFrame(data=[[3, 1]], columns=["c1", "c2"])


@task
def prepare_data(df):
    return df


@task
def func_pipeline(p: int):
    df = pd.DataFrame(data=[[p, 1]], columns=["c1", "c2"])
    d1 = prepare_data(df)
    return prepare_data(d1)


@task
def func_pipeline2(p: int):
    df = func_return_df()
    return func_gets(df)


if __name__ == "__main__":
    import os

    os.environ["DBND__TRACKING"] = "true"
    func_pipeline2(4)
