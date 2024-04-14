#!/usr/bin/env python3.11
"""
Provides classes and functionality relating to orders for
applications using the fakeco-namespace code.
"""

from fakeco.core_data import Place, Thing


class BillingAddress(Place):
    """
    Represents a Billing Address Place in the context of the system.
    """
    ...


class ShippingAddress(Place):
    """
    Represents a Shipping Address Place in the context of the system.
    """
    ...


class Order(Thing):
    """
    Represents an Order Thing in the context of the system.
    """
    ...
