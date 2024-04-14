"""
Examples of type-annotation as of Python 3.10
"""

import os
from typing import Any

from typeguard import typechecked


@typechecked
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
    good_strings = ('this is a string',)
    good_ints = (1, 2, 3)
    good_floats = (1.23, 4.56)
    good_bools = (True, False)
    good_lists = (
        [True, None, 1, 2.3, object()],
    )
    good_dicts = (
        {'name': 'Librarian', 'says': 'Oook!', 'ape': True},
    )

    bad_strings = (True, None, 1, 2.3, object())
    bad_ints = (1.22, None)
    bad_floats = (None, object())
    bad_bools = ('true', 'false')
    bad_dicts = (
        {
            1: 'Bad key',
            'name': 'Librarian',
            'says': 'Oook!',
            'ape': True
        },
    )


    for str_arg in good_strings:
        for int_arg in good_ints:
            for float_arg in good_floats:
                for bool_arg in good_bools:
                    for list_arg in good_lists:
                        for dict_arg in good_dicts:
                            example_function(
                                str_arg, int_arg,
                                float_arg, bool_arg,
                                list_arg, dict_arg
                            )

    print('== invalid str_arg types '.ljust(59, '='))
    for str_arg in bad_strings:
        try:
            example_function(
                str_arg, int_arg, float_arg, bool_arg,
                list_arg, dict_arg
            )
        except Exception as error:
            print(error)
    str_arg = good_strings[0]

    print('== invalid int_arg types '.ljust(59, '='))
    for int_arg in bad_ints:
        try:
            example_function(
                str_arg, int_arg, float_arg, bool_arg,
                list_arg, dict_arg
            )
        except Exception as error:
            print(error)
    int_arg = good_ints[0]

    print('== invalid float_arg types '.ljust(59, '='))
    for float_arg in bad_floats:
        try:
            example_function(
                str_arg, int_arg, float_arg, bool_arg,
                list_arg, dict_arg
            )
        except Exception as error:
            print(error)
    float_arg = good_floats[0]

    print('== invalid bool_arg types '.ljust(59, '='))
    for bool_arg in bad_bools:
        try:
            example_function(
                str_arg, int_arg, float_arg, bool_arg,
                list_arg, dict_arg
            )
        except Exception as error:
            print(error)
    bool_arg = good_bools[0]

    print('== invalid dict_arg types '.ljust(59, '='))
    for dict_arg in bad_dicts:
        try:
            example_function(
                str_arg, int_arg, float_arg, bool_arg,
                list_arg, dict_arg
            )
        except Exception as error:
            print(type(error))
            print(error)
    dict_arg = good_dicts[0]
