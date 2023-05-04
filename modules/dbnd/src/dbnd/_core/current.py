import logging
import typing

from typing import Optional

from dbnd._core.configuration import get_dbnd_project_config


if typing.TYPE_CHECKING:
    from dbnd._core.context.databand_context import DatabandContext
    from dbnd._core.run.databand_run import DatabandRun
    from dbnd._core.settings import DatabandSettings
    from dbnd._core.task import Task
    from dbnd._core.task_run.task_run import TaskRun


def get_databand_context():
    # type: () -> DatabandContext
    """Databand Context get or create instance."""
    from dbnd._core.context.databand_context import DatabandContext as _DatabandContext

    return _DatabandContext.try_instance()


def try_get_databand_context():
    # type: () -> Optional[DatabandContext]

    from dbnd._core.context.databand_context import DatabandContext as _DatabandContext

    return get_databand_context() if _DatabandContext.has_instance() else None


def dbnd_context():
    """Get or create databand context."""
    context = try_get_databand_context()
    if not context:
        # we are running without Databand Context
        # let create one inplace
        from dbnd._core.context.databand_context import (
            DatabandContext as _DatabandContext,
        )

        context = _DatabandContext.try_instance(name="inplace_run")
    return context


def get_databand_run():
    # type: () -> DatabandRun
    """Returns current Task/Pipeline/Flow instance."""
    from dbnd._core.run.databand_run import DatabandRun as _DatabandRun

    return _DatabandRun.get_instance()


def try_get_databand_run():
    # type: () -> Optional[DatabandRun]
    from dbnd._core.run.databand_run import DatabandRun as _DatabandRun

    return get_databand_run() if _DatabandRun.has_instance() else None


def in_tracking_run():
    return not run.is_orchestration if (run := try_get_databand_run()) else False


def is_orchestration_run():
    return run.is_orchestration if (run := try_get_databand_run()) else False


def current_task():
    # type: () -> Task
    """
    Returns the current task's object.

    Example::

        from dbnd import current_task, task

        @task
        def calculate_alpha(alpha: int = 0.5):
            return current_task().task_version
    """
    from dbnd._core.task_build.task_context import current_task as ct

    return ct()


def try_get_current_task():
    from dbnd._core.task_build.task_context import try_get_current_task as tgct

    return tgct()


def get_task_by_task_id(task_id):
    # type: (str) -> Task
    return get_databand_context().task_instance_cache.get_task_by_id(task_id)


def try_get_current_task_run():
    if run := try_get_databand_run():
        return (
            run.get_task_run(task.task_id)
            if (task := try_get_current_task())
            else None
        )
    else:
        return None


def current_task_run():
    # type: () -> TaskRun
    """
    Returns the current task run.

    Example::

        from dbnd import current_task_run, task

        @task
        def calculate_alpha(alpha: int = 0.5):
            return current_task_run()
    """
    return get_databand_run().get_task_run(current_task().task_id)


def get_settings():
    return get_databand_context().settings


def is_verbose():
    context = try_get_databand_context()
    if (
        context
        and getattr(context, "system_settings", None)
        and context.system_settings.verbose
    ):
        # only if True, otherwise check project config too
        return True

    return get_dbnd_project_config().is_verbose()


def get_target_logging_level():
    context = try_get_databand_context()
    if context and getattr(context, "settings", None):
        return getattr(logging, context.settings.log.targets_log_level)

    else:
        return 10


def is_killed():
    run = try_get_databand_run()
    return run and run.is_killed()


def cancel_current_run(message=None):
    """Kills a run's execution from within the execution."""
    current_databand_run = get_databand_run()
    return current_databand_run.kill_run(message)
