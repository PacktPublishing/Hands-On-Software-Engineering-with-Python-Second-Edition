from __future__ import annotations

from typeguard import typechecked

@typechecked
class Person:

    def __init__(
        self,
        given_name: str,
        family_name: str,
        middle_name: str | None = None
    ):
        self.given_name = given_name
        self.family_name = family_name
        self.middle_name = middle_name

if __name__ == '__main__':
    # Works as expected
    try:
        ridcully = Person('Mustrum', 'Ridcully')
    except Exception as error:
        print('This should not fail')

    # If typechecked works as expected, this should raise
    # an error, but it does not
    try:
        rincewind = Person(None, 'Rincewind', None)
    except Exception as error:
        print('Expected failure (rincewind): None is not a string')
    else:
        print('This should fail (rincewind)')

    # This also should fail, but does not
    try:
        should_fail = Person(1, 2, 3)
    except Exception as error:
        print('Expected failure (should_fail): 1 is not a string')
    else:
        print('This should fail (should_fail)')
