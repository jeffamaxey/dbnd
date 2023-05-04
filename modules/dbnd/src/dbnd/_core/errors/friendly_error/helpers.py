def _task_name(task):
    return task.task_definition.full_task_family


def _band_call_str(task):
    if not task:
        return
    if task.task_decorator:
        return f"{_task_name(task)}()"
    return f"{_task_name(task)}.band()"


def _run_name(task):
    return task.task_definition.run_name()


def _safe_task_family(task):
    if not task:
        return "unknown"

    from dbnd._core.task import Task

    return _task_name(task) if isinstance(task, Task) else str(task)


def _parameter_name(task, parameter):
    return f"{task.friendly_task_name}.{parameter.name}"


def _safe_target(target):
    msg = str(target)
    if target and target.source_task:
        msg += " created by {task}".format(task=_safe_task_family(target.source_task))
    return msg
