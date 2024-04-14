from __future__ import annotations

import abc


def find_customers(
    given_name=None, family_name=None
) -> list[Customer]:
    """
    Finds and returns a list of Customer objects.

    @param given_name: The given_name value to use in the
        customer query.
    @type given_name: str or None
    @param family_name: The family_name value to use in the
        customer query.
    @type family_name: str or None
    @return: the Customer object(s) that matched the supplied
        criteria, in whole or in part
    @rtype: list[Customer]

    Raises an AssertionError if given_name and family_name
    are both None.
    """
    ...


def get_customer(customer_id) -> Customer:
    """
    Returns a Customer object for the Customer identified.

    @param customer_id: The unique identifier of the customer
        to be retrieved.
    @type given_name: UUID or str

    Raises a RuntimeError if no customer could be found with
    the specified customer ID.
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

        @param given_name: The given_name value to store in the
            instance's state.
        @type given_name: str
        @param family_name: The family_name value to store in the
            instance's state.
        @type family_name: str
        @return: the BasePerson instance
        @rtype: BasePerson
        """
        ...


class Customer(BasePerson):
    """
    Represents a Customer in the system.
    """

    def __init__(self, customer_id, given_name, family_name):
        """
        Initializes a Customer instance.

        @param customer_id: The unique identifier value for
            the customer to store in the instance's state.
        @type customer_id: UUID or str
        @param given_name: The given_name value to store in the
            instance's state.
        @type given_name: str
        @param family_name: The family_name value to store in the
            instance's state.
        @type family_name: str
        @return: the Customer instance
        @rtype: Customer

        Raises a TypeError or ValueError if customer_id is not a
        UUID, and cannot be converted to one.
        """
        ...
