from __future__ import absolute_import

import logging
import os

from dbnd._vendor.dulwich import porcelain
from dbnd._vendor.dulwich.repo import Repo


logger = logging.getLogger(__name__)

GIT_ENV = "DBND_PROJECT_GIT_COMMIT"


def is_git_dirty(path=None, verbose=False):
    try:
        repo = Repo.discover(path)
        status = porcelain.status(repo.path)
        return any(
            [
                status.staged["add"],
                status.staged["delete"],
                status.staged["modify"],
                len(status.unstaged),
                len(status.untracked),
            ]
        )
    except Exception as ex:
        if verbose:
            logger.warning("Failed to get GIT status %s: %s", path, ex)
        return None


def get_git_commit(path, verbose=False):
    if env_commit := os.environ.get(GIT_ENV):
        return env_commit
    try:
        repo = Repo.discover(path)
        return repo.head().decode("utf-8")
    except Exception as ex:
        if verbose:
            logger.warning("Failed to get GIT version of %s: %s", path, ex)
        return None
