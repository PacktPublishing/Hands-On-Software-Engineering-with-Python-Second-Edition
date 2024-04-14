"""
Examples of type-annotation as of Python 3.10
"""

# Additions to the built-in typing module:
# • Callable update
# • Concatenate
# • Generic update
# • NewType update
# • ParamSpec
# • ParamSpecArgs
# • ParamSpecKwargs
# • TypeAlias
# • TypeGuard
# • Union type expressions with |
#   Optional as type | None
# • is_typeddict function

import os
from typing import Any


def example_function(
    str_arg: str,
    int_arg: int,
    float_arg: float,
    bool_arg: bool,
    list_arg: list[Any],
    dict_arg: dict[str, Any],
    *args: int | float,
    **kwargs: Any
) -> None:
    print(
        f'{__file__.split(os.sep)[-1].split(".")[0]}'
        '::example_function called:'
    )
    print(f'str_arg ..... ({type(str_arg).__name__}) {str_arg}')
    print(f'int_arg ..... ({type(int_arg).__name__}) {int_arg}')
    print(f'float_arg ... ({type(float_arg).__name__}) {float_arg}')
    print(f'bool_arg .... ({type(bool_arg).__name__}) {bool_arg}')
    print(f'list_arg .... ({type(list_arg).__name__}) {list_arg}')
    print(f'dict_arg .... ({type(dict_arg).__name__}) {dict_arg}')
    print(f'args ........ ({type(args).__name__}) {args}')
    print(f'kwargs ...... ({type(kwargs).__name__}) {kwargs}')


if __name__ == '__main__':
    from inspect import getfullargspec
    from pprint import pprint
    example_function(
        'str_arg', 1, 2.345, True,
        ['list', 'values', 6, 7.89],
        {'name': 'string', 'value': 2},
        0, 1.234,
        kw1='kwarg-string', kw2=5, kw3=6.789
    )
    print('== Annotations of example_function '.ljust(59, '='))
    pprint(getfullargspec(example_function).annotations)
