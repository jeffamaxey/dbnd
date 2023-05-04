from __future__ import absolute_import

import sys

from dbnd._core.errors import (
    DatabandBuildError,
    DatabandConfigError,
    DatabandError,
    DatabandRuntimeError,
    TaskClassAmbigiousException,
)
from dbnd._core.errors.errors_utils import safe_value
from dbnd._core.errors.friendly_error import (  # noqa: F401
    api,
    config,
    execute_engine,
    executor_k8s,
    graph,
    targets,
    task_build,
    task_execution,
    task_parameters,
    task_registry,
    tools,
)
from dbnd._core.errors.friendly_error.helpers import (
    _band_call_str,
    _run_name,
    _safe_target,
    _safe_task_family,
)
from dbnd._core.utils.basics.format_exception import format_exception_as_str


def task_found_in_airflow_dag(root_task):
    return DatabandError(
        f"Task '{root_task}' implementation has been discovered via DAGs loading",
        help_msg="Your task %s were loaded via dags folder, currently we don't support that.\n"
        "You should define your tasks not in airflow/dag folder, but inside your project.\n"
        "Use module key in a [databand] section of config file ( $DBND__DATABAND__MODULE )"
        % root_task,
        show_exc_info=False,
    )


def task_has_not_complete_but_all_outputs_exists(task):
    return DatabandRuntimeError(
        "Something wrong, task %s has been executed, "
        "but _complete function returns False while all outputs exist! "
        % _safe_task_family(task),
        help_msg="Check your implementation of %s, validate that you _complete override is correct",
        show_exc_info=False,
    )


def task_has_missing_outputs_after_execution(task, missing_str):
    return DatabandRuntimeError(
        "Task %s has been executed, but some outputs are missing!\n\t%s"
        % (_safe_task_family(task), missing_str),
        help_msg="Check your implementation of %s, validate that all outputs has been written. "
        "If it's directory, validate that you have _SUCCESS flag "
        "(self.your_task_output.mark_success())" % _run_name(task),
        show_exc_info=False,
    )


def task_data_source_not_exists(task, missing, downstream=None):
    if downstream:
        tasks = ",".join(map(str, downstream))
        dependent = "Tasks that depend on this input are: %s\n" % tasks
    else:
        dependent = ""
    if len(missing) == 1:
        missing_target = missing[0]

        from targets.dir_target import DirTarget

        if (
            isinstance(missing_target, DirTarget)
            and missing_target.folder_exists()
            and missing_target.flag_target
        ):
            # we are missing flag!
            return DatabandRuntimeError(
                f"Data source '{missing_target.flag_target}' success flag is missing! {dependent}",
                help_msg="Check that SUCCESS flag exists and your configurations is ok. "
                "You can override flag check by \n"
                "1. adding '[noflag]' to your path: '%s[noflag]' \n"
                "2. --PARAMETER-target '[noflag]' \n"
                "3. Define parameter using 'parameter.folder.with_flag(None)' \n"
                "4 .Create the flag if you think that the input is ok"
                % missing_target,
                show_exc_info=False,
            )
        return DatabandRuntimeError(
            f"Task input at location '{missing_target}' is missing! {dependent}",
            help_msg="Validate that this data exists. "
            "This string considered as a path, as it defined as 'data' in our system",
            show_exc_info=False,
        )

    if len(missing) > 5:
        missing_msg = f"{missing[:10]}... ({len(missing)} files)"
    else:
        missing_msg = ",".join(map(str, missing))

    return DatabandRuntimeError(
        f"Data source '{missing_msg}' is missing! {dependent}",
        help_msg="Check that file exists and your configurations is ok. "
        "If it's directory, validate that you have _SUCCESS flag, "
        "or override that via target config ('noflag')",
        show_exc_info=False,
    )


def ambiguous_task(full_task_name):
    return TaskClassAmbigiousException(
        "Task %r is ambiguous, you have more than one task with the same name!"
        % full_task_name,
        help_msg="Check whether this module contains more than one methods with the same name. "
        "Please use full reference (like 'a.b.c') ",
        show_exc_info=False,
    )


def no_matching_tasks_in_pipeline(tasks, tasks_regexes):
    all_tasks_names = ",".join([t.task_id for t in tasks])
    return DatabandConfigError(
        f"None of '{tasks_regexes}' tasks have been found at current pipeline!",
        help_msg="check your run.selected_tasks_regex switch, "
        "select one of following tasks: %s" % all_tasks_names,
        show_exc_info=False,
    )


def dag_with_different_contexts(task_id):
    return DatabandRuntimeError(
        f"The task '{task_id}' isn't part of the current context!",
        help_msg="The task '%s' isn't part of the current context! \n"
        "Make sure you did not fiddle with internal APIs" % task_id,
        show_exc_info=False,
    )


def dbnd_module_not_found_tip(module):
    if str(module).startswith("dbnd"):
        dbnd_module = module.split(".")[0]
        return f"""Do you have '{dbnd_module.replace("_", "-")}' installed?"""
    return ""


def failed_to_import_user_module(ex, module, description):
    s = format_exception_as_str(sys.exc_info())
    msg = f"Module '{module}' can not be loaded: {dbnd_module_not_found_tip(module)}"
    return DatabandError(
        f"{msg} exception: {s}.",
        help_msg=" Databand is trying to load user module '%s' as required by %s: \n "
        "Probably, it has compile errors or not exists."
        % (module, description),
        show_exc_info=False,
    )


def unknown_args_in_task_call(parent_task, cls, call_args, call_repr):
    return DatabandBuildError(
        f"You are trying to create {_run_name(cls)} from {_band_call_str(parent_task)} with {len(call_args)} *args, please use named arguments only: {call_repr}",
        show_exc_info=True,
        help_msg=f"Check your {_band_call_str(parent_task)} logic",
    )


def failed_to_create_task(exc_desc, nested_exceptions):
    msg = f"Failed to create task {exc_desc}"
    if nested_exceptions:
        msg += ": "
        msg += ",".join([str(e) for e in nested_exceptions[:3]])
        if len(nested_exceptions) > 3:
            msg += f" (showing 3 errors out of {len(nested_exceptions)})"
    return DatabandBuildError(
        msg, show_exc_info=False, nested_exceptions=nested_exceptions
    )


def failed_to_convert_value_to_target(value):
    return DatabandBuildError(
        f"Can't convert '{safe_value(value)}' of type {type(value)} to target.",
        help_msg="You can convert only values with type of "
        "Target, Tasks and strings to the Path/PathStr/Target",
    )


def failed_to_calculate_task_parameter_value(ex, task_family, p_name, exc_desc):
    return DatabandBuildError(
        f"Failed to process parameter {p_name} for {exc_desc}: {ex}",
        nested_exceptions=[ex],
        help_msg=f"Please validate your config/commandline/.band that creates runs {exc_desc}",
    )


def failed_to_read_pandas(ex, target):
    return DatabandError(
        "There is an error while reading {target}: {ex}".format(
            target=_safe_target(target), ex=ex
        ),
        nested_exceptions=[ex],
    )


def failed_to_set_index(ex, df, set_index, target):
    return DatabandError(
        "Failed to set index to '{set_index}' "
        "for data frame with columns {columns} "
        "while reading from {target}: {ex}".format(
            set_index=set_index, columns=df.columns, target=_safe_target(target), ex=ex
        ),
        nested_exceptions=[ex],
    )


def failed_to_read_target_as_task_input(ex, task, parameter, target):
    return DatabandError(
        "Failed to read '{task.task_name}.{p.name}' from "
        "'{target}' as format '{target.config}' to {p.value_type.type_str}: {ex}"
        "".format(p=parameter, target=target, task=task, ex=ex),
        nested_exceptions=ex,
    )


def failed_to_read_task_input(ex, task, parameter, target):
    return DatabandError(
        "Failed to read '{task.task_name}.{p.name}' from "
        "'{target}' to {p.value_type.type_str}: {ex}"
        "".format(p=parameter, target=target, task=task, ex=ex),
        nested_exceptions=ex,
    )


def failed_to_write_task_output(ex, target, value_type):
    return DatabandError(
        "Failed to write '{target.name}' to '{target} {target.config}  ({value_type}): {ex}"
        "".format(value_type=value_type, target=target, ex=ex),
        nested_exceptions=ex,
    )


def failed_to_write_pandas(ex, target):
    return DatabandError(
        "There is an error while writing to {target} {ex}".format(
            target=_safe_target(target), ex=ex
        ),
        nested_exceptions=ex,
    )


def marshaller_no_merge(marshaller, target, partitions):
    return DatabandError(
        "Can't merge {p_len} partitions on read from {target} "
        "as current marshaller {marshaller} doesn't support merge funcitonality".format(
            p_len=len(partitions), target=target, marshaller=marshaller
        )
    )


def airflow_bad_user_configuration(ex, file_path):
    return DatabandConfigError(
        f"Error while trying to load additional airflow configuration from {file_path}",
        help_msg=f"Please make sure that the configuration file {file_path} does exist.",
        nested_exceptions=ex,
        show_exc_info=False,
    )
