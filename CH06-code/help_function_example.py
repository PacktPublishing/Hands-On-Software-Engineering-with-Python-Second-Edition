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
    """
    An example function.

    Parameters:
    -----------
    str_arg : str
        A string value that is used for something.
    int_arg : int
        An integer value that is used for something.
    float_arg : float
        A floating-point value that is used for something.
    bool_arg : bool
        A boolean value that indicates something.
    list_arg : list[Any]
        A list of things.
    dict_arg : dict[str, Any]
        A dictionary of things
    *args : int | float
        The argument-list for the function.
    **kwargs : Any
        The keyword arguments for the function.
    """
    ...


help(example_function)
