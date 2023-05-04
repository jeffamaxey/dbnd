from dbnd._core.errors import DatabandRuntimeError
from dbnd._core.errors.friendly_error.helpers import (
    _parameter_name,
    _run_name,
    _task_name,
)


def failed_to_save_value_to_target(ex, task, parameter, target, value):
    if parameter.name == "result":
        return DatabandRuntimeError(
            f"Can't save return value of {_parameter_name(task, parameter)} to {target}': {ex}",
            show_exc_info=True,
            nested_exceptions=[ex],
            help_msg=f"Check your {_run_name(task)} return value and it definition ('{parameter.value_type.type}')",
        )
    return DatabandRuntimeError(
        f"Can't save {_parameter_name(task, parameter)} to {target}': {ex}",
        show_exc_info=True,
        nested_exceptions=[ex],
        help_msg=f"Check your {task.friendly_task_name} logic. ",
    )


def failed_to_read_value_from_target(ex, task, parameter, target):
    return DatabandRuntimeError(
        f"Can't read {_parameter_name(task, parameter)} from {target}': {ex}",
        show_exc_info=True,
        nested_exceptions=[ex],
        help_msg=f"Check your {task.friendly_task_name} logic. ",
    )


def failed_to_assign_result(task, result_parameter):
    return DatabandRuntimeError(
        "The result of the band/run call is None, "
        "it can not be assigned to {schema}".format(
            task=task, schema=result_parameter.schema
        ),
        help_msg=f"Check your {_task_name(task)} return value",
    )


def failed_to_process_non_empty_result(task, result):
    return DatabandRuntimeError(
        "Can' process non empty result of {task} while it's marked as task without outputs: result={result}".format(
            task=_task_name(task), result=result
        ),
        help_msg="Please, use @task(result=YOU RESULT SCHEMA)",
    )


def can_run_only_tasks(task):
    return DatabandRuntimeError(
        "Databand can run only Tasks, got {task} instead".format(task=type(task)),
        help_msg="Please, use check that you don't call function while providing it to databand. "
        "Use YOUR_TASK_FUNCTION.task()",
    )


def wrong_return_value_type(task_def, names, result):
    return DatabandRuntimeError(
        "Returned value from '{task}' should be tuple/list/dict as task has multiple result."
        "Expected tuple of '{names}', got value of type '{result}'".format(
            task=task_def.run_name(), names=names, result=type(result)
        )
    )


def wrong_return_value_len(task_def, names, result):
    return DatabandRuntimeError(
        "Returned result from '{task}' doesn't match expected schema. "
        "Expected tuple of '{names}', got tuple of length '{result}'".format(
            task=task_def.run_name(), names=names, result=len(result)
        )
    )


def failed_to_run_spark_script(task, cmd, application, return_code, error_snippets):
    return DatabandRuntimeError(
        f"spark_submit failed with return code {return_code}. Failed to run: {cmd}",
        show_exc_info=False,
        nested_exceptions=error_snippets,
        help_msg=f"Check your  {application} logic and input data {list(task.relations.task_inputs_user.values())}. Inspect spark logs for more info.",
    )


def failed_to_run_cmd(name, cmd_str, return_code):
    return DatabandRuntimeError(
        "{name} has failed, returncode='{return_code}'. Failed to run: {cmd}".format(
            name=name, return_code=return_code, cmd=cmd_str
        ),
        show_exc_info=False,
        help_msg="Inspect logs for more info.",
    )


def failed_spark_status(msg):
    return DatabandRuntimeError(msg, show_exc_info=False)


def failed_to_run_emr_step(reason, logs_path, error_snippets):
    if logs_path and error_snippets:
        return DatabandRuntimeError(
            f"EMR Spark step failed with reason: {reason} ",
            show_exc_info=False,
            nested_exceptions=error_snippets,
            help_msg="Check your application logic. Inspect spark emr logs for more info.\n "
            "Logs are available at %s." % logs_path,
        )
    return DatabandRuntimeError(
        f"EMR Spark step failed with reason: {reason}. Additionally Databand failed to get EMR logs.",
        show_exc_info=False,
        help_msg="Check your application logic. Inspect emr console for logs and more info\n ",
    )


def system_exit_at_task_run(task, ex):
    return DatabandRuntimeError(
        f"Task execution has been aborted with sys.exit() call: {ex}",
        nested_exceptions=ex,
        show_exc_info=False,
        help_msg="Check your task run()\n ",
    )


def databand_context_killed(interrupt_location):
    return DatabandRuntimeError(
        "Databand Context has been killed externaly. Interrupted at %s",
        interrupt_location,
    )
