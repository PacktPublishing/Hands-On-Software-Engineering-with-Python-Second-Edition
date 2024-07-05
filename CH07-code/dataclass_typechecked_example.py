from dataclasses import dataclass
from typing import Optional

from typeguard import typechecked

@typechecked
@dataclass
class Person:
    given_name: str
    family_name: str
    middle_name: str | None = None

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
    print('Expected failure: None is not a string')
else:
    print('This should fail (rincewind): None is not a string')

# This also should fail, but does not
try:
    should_fail = Person(1, 2, 3)
except Exception as error:
    print('Expected failure: 1 is not a string')
else:
    print('This should fail (should_fail): 1 is not a string')
