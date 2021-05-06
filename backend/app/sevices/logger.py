from aiologger import Logger
from aiologger.formatters.base import Formatter


def get_logger(level):
    return Logger.with_default_handlers(
        name=__name__,
        level=level,
        formatter=Formatter(
            fmt=(
                "%(levelname)05s [%(asctime)s.%(msecs)03d]"
                "[%(module)s:%(lineno)d]: %(message)s"
            )
        )
    )
