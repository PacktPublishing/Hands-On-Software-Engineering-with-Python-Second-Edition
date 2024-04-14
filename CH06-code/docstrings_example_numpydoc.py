from __future__ import annotations

import abc


def find_customers(
    given_name=None, family_name=None
) -> list[Customer]:
    """
    Finds and returns a list of Customer objects.

    Parameters:
    -----------
    given_name : str | None
        The given_name value to use in the customer query.
    family_name : str | None
        The family_name value to use in the customer query.

    Raises:
    -------
    AssertionError
        If given_name and family_name are both None.

    Notes:
    ------
    Connects to the back-end data-store and executes a query
    to retrieve all customers whose given_name and/or family_name
    match the values supplied, in whole or in part.
    """
    ...


def get_customer(customer_id) -> Customer:
    """
    Returns a Customer object for the Customer identified.

    Parameters:
    -----------
    customer_id : UUID | str
        The unique identifier of the customer to be retrieved.
        

    Raises:
    -------
    RuntimeError
        If no customer could be found with the specified
        customer ID.
    """
    ...


class BasePerson(metaclass=abc.ABCMeta):
    """
    ABC providing baseline functionality, interface requirements,
    and type-identity for objects that can represent a Person
    """

    def __init__(self, given_name, family_name):
        """
        Initializes a BasePerson-derived instance.

        Parameters:
        -----------
        given_name : str | None
            The given_name value to store in the instance's state.
        family_name : str | None
            The family_name value to store in the instance's state.
        """
        ...


class Customer(BasePerson):
    """
    Represents a Customer in the system.
    """

    def __init__(self, customer_id, given_name, family_name):
        """
        Initializes a Customer instance.

        Parameters:
        -----------
        customer_id : UUID | str
            The unique identifier of the customer to store in the
            instance's state.
            Will be converted to a UUID value if one is not provided.
        given_name : str | None
            The given_name value to store in the instance's state.
        family_name : str | None
            The family_name value to store in the instance's state.

        Raises:
        -------
        TypeError
            If customer_id is not a UUID or str.
        ValueError
            If customer_id is not a UUID, or is a str but cannot be
            converted to a UUID.
        """
        ...
