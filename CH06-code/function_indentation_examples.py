from typing import Any


def example_function_1(str_arg: str, int_arg: int, float_arg: float, bool_arg: bool, list_arg: list[Any], dict_arg: dict[str, Any], *args: int | float, **kwargs: Any):
    ...


def example_function_2(str_arg: str, int_arg: int, float_arg: float,
                       bool_arg: bool, list_arg: list[Any],
                       dict_arg: dict[str, Any], *args: int | float,
                       **kwargs: Any):
    ...


def example_function_3(
    str_arg: str, int_arg: int, float_arg: float, bool_arg: bool,
    list_arg: list[Any], dict_arg: dict[str, Any],
    *args: int | float,
    **kwargs: Any
):
    ...

