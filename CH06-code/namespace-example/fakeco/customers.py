#!/usr/bin/env python3.11
"""
Provides classes and functionality relating to customers for
applications using the fakeco-namespace code.
"""

from fakeco.core_data import Person, Place


class Customer(Person):
    """
    Represents a Customer Person in the context of the system.
    """
    ...


class DefaultBillingAddress(Place):
    """
    Represents the default Billing Address Place for a Customer
    in the context of the system.
    """
    ...


class DefaultShippingAddress(Place):
    """
    Represents the default Shipping Address Place for a Customer
    in the context of the system.
    """
    ...


