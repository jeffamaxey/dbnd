from typing import List

from dbnd import Task
from dbnd._core.errors import DatabandError
from dbnd._core.task_ctrl.task_ctrl import TaskSubCtrl


class TaskDescendants(TaskSubCtrl):
    def __init__(self, task):
        super(TaskDescendants, self).__init__(task)

        self.children = set()

    def add_child(self, task_id):
        self.children.add(task_id)

    def get_children(self):
        children = []
        tic = self.dbnd_context.task_instance_cache
        for c_id in self.children:
            child_task = tic.get_task_by_id(c_id)
            if child_task is None:
                raise DatabandError(
                    f"You have created {c_id} in different dbnd_context, can't find task object in current context!"
                )
            children.append(child_task)
        return children
