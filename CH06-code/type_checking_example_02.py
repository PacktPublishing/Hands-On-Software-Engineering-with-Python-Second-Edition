"""
Example type-narrowing process, using isinstance for
each parameter
"""

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
    for name, value in vars().items():
        annotation = example_function.__annotations__[name]
        args = getattr(annotation, '__args__', None)
        if annotation is Any:
            pass
        elif hasattr(annotation, '__args__'):
            if annotation.__args__ is Any or Any in annotation.__args__:
                pass
            elif isinstance(value, (tuple, list)):
                if not all(
                    [isinstance(arg, (int, float)) for arg in value]
                ):
                    raise TypeError(
                        f'{name} check: Replace this with a '
                        'meaningful error-message'
                    )
            elif not isinstance(
                value, example_function.__annotations__[name].__args__
            ):
                raise TypeError(
                    f'{name} check: Replace this with a '
                    'meaningful error-message'
                )
        else:
            if not isinstance(value, annotation):
                raise TypeError(
                    f'{name} check: Replace this with a '
                    'meaningful error-message'
                )
            ...
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

    try:
        print('Invalid str_arg:')
        example_function(
            None, 1, 2.345, True,
            ['list', 'values', 6, 7.89],
            {'name': 'string', 'value': 2},
            0, 1.234,
            kw1='kwarg-string', kw2=5, kw3=6.789
        )
    except Exception as error:
        print(f'{error.__class__.__name__}: {error}')
        print()

    try:
        print('Invalid int_arg:')
        example_function(
            None, 1, 2.345, True,
            ['list', 'values', 6, 7.89],
            {'name': 'inting', 'value': 2},
            0, 1.234,
            kw1='kwarg-string', kw2=5, kw3=6.789
        )
    except Exception as error:
        print(f'{error.__class__.__name__}: {error}')
        print()

    try:
        print('Invalid *args:')
        example_function(
            'string', 1, 2.345, True,
            ['list', 'values', 6, 7.89],
            {'name': 'string', 'value': 2},
            0, 1.234, None,
            kw1='kwarg-string', kw2=5, kw3=6.789
        )
    except Exception as error:
        print(f'{error.__class__.__name__}: {error}')
        print()
