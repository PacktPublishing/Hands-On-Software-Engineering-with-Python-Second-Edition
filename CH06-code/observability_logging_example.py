import logging
import os
import pprint

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

module_name = __file__.split(os.sep)[-1]


class LocalError(Exception):
    ...


def example_function(
    arg1, arg2=None, *args, kwonly1=None, **kwargs
):
    logger.info(f'{module_name}::example_function called')
    logger.debug(pprint.pformat(locals()))
    try:
        logger.debug(
            f'{module_name}::example_function debugging '
            'message'
        )
        # Comment one of these out to see the
        # differences in how they log messages.
        raise LocalError(
            'Some (recoverable?) error happened'
        )
        raise RuntimeError('Some FATAL error happened')
    except LocalError as error:
        logger.error(
            f'{module_name}::example_function encountered '
            f'{error.__class__.__name__}: {error}',
            exc_info=error
        )
    except Exception as error:
        logger.critical(
            f'{module_name}::example_function encountered a '
            f'{error.__class__.__name__}: {error}',
            exc_info=error
        )
    else:
        logger.debug(
            f'{module_name}::example_function another '
            'debugging message'
        )
        logger.info(
            f'{module_name}::example_function completed '
            'successfully'
        )


if __name__ == '__main__':

    # Logging to the console
    stdout_handler = logging.StreamHandler()
    formatter = logging.Formatter('[%(levelname)8s] %(message)s')
    stdout_handler.setFormatter(formatter)
    logger.addHandler(stdout_handler)

    logger.info(f'{module_name}.__main__ executing')
    example_function('arg1 value')
    logger.info(f'{module_name}.__main__ completed')
