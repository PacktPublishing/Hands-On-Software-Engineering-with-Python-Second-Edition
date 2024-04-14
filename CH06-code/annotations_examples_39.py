"""
Examples of type-annotation as of Python 3.9
"""

# Additions to the built-in typing module:
# • Support for [] annotation notations for:
#   builtins.dict
#   builtins.frozenset
#   builtins.list
#   builtins.set
#   builtins.tuple
#   builtins.type
#   collections.ChainMap
#   collections.Counter
#   collections.Deque
#   collections.OrderedDict
#   collections.abc.AsyncGenerator
#   collections.abc.AsyncIterable
#   collections.abc.AsyncIterator
#   collections.abc.Awaitable
#   collections.abc.ByteString
#   collections.abc.Callable
#   collections.abc.Collection
#   collections.abc.Container
#   collections.abc.Coroutine
#   collections.abc.Generator
#   collections.abc.Hashable
#   collections.abc.ItemsView
#   collections.abc.Iterable
#   collections.abc.Iterator
#   collections.abc.KeysView
#   collections.abc.Mapping
#   collections.abc.MappingView
#   collections.abc.MutableMapping
#   collections.abc.MutableSequence
#   collections.abc.MutableSet
#   collections.abc.Reversible
#   collections.abc.Sequence
#   collections.abc.Set
#   collections.abc.Sized
#   collections.abc.ValuesView
#   collections.defaultdict
#   contextlib.AsyncContextManager
#   contextlib.ContextManager
# • Annotated
# • Literal updates
# • NamedTuple updates
# • re.Match
# • re.Pattern
# • get_type_hints function

import os
from typing import Any, Union


def example_function(
    str_arg: str,
    int_arg: int,
    float_arg: float,
    bool_arg: bool,
    list_arg: list[Any],
    dict_arg: dict[str, Any],
    *args: Union[int, float],
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
