import logging

from dbnd._core.constants import ClusterPolicy
from dbnd._core.task_run.task_run_ctrl import TaskJobCtrl


logger = logging.getLogger(__name__)


class TaskEnginePolicyCtrl(TaskJobCtrl):
    @classmethod
    def create_engine(cls):
        return None

    @classmethod
    def terminate_engine(cls):
        return None

    @classmethod
    def get_engine_policy(cls):
        return ClusterPolicy.NONE

    @classmethod
    def apply_engine_policy(cls, root_task):
        policy = cls.get_engine_policy()
        if policy == ClusterPolicy.NONE:
            return root_task

        if policy in [ClusterPolicy.CREATE, ClusterPolicy.EPHERMAL]:
            if create_task := cls.create_engine():
                root_task.set_global_upstream(create_task)

        if policy in [ClusterPolicy.KILL, ClusterPolicy.EPHERMAL]:
            if delete_cluster := cls.terminate_engine():
                root_task.set_downstream(delete_cluster)

        return root_task
