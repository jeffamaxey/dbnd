_SHOWN_ATTR = "_dbnd_shown"


def set_shown(ex):
    setattr(ex, _SHOWN_ATTR, True)


def is_shown(ex):
    return getattr(ex, _SHOWN_ATTR, False) if ex else False


def log_error(logger, ex, msg, *msg_args):
    if is_shown(ex):
        logger.error(msg, *msg_args)
    else:
        logger.exception(msg, *msg_args)
