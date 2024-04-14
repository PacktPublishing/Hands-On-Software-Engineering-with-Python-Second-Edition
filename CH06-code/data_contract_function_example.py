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

    def __repr__(self) -> str:
        return f'<{self.__class__.__name__} at {hex(id(self))} ' \
            f'given_name={self.given_name} ' \
            f'middle_name={self.middle_name} ' \
            f'family_name={self.family_name}>'


@typechecked
def do_person_things(
    person: Person | None = None,
    *,
    given_name: str | None = None,
    family_name: str | None = None,
    middle_name: str | None = None
):
    _no_person_data = 'do_person_things expects either a ' \
        'Person object or a given_name and family_name ' \
        'value (with an optional middle_name value) ' \
        'that can create one'

    # Assure that we have a Person, or create one
    if person is None:
        # No person supplied, try to create one
        assert given_name and family_name, _no_person_data
        person = Person(given_name, family_name, middle_name)

    # Either person was provided, or successfully created
    assert isinstance(person, Person), _no_person_data

    # Do some computationally-expensive things
    # with the Person created before returning it
    ...
    return person


# A simple Person-creation example
try:
    result = Person('Havelock', 'Vetinari')
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

# Creating a dict of arguments, and passing that
drumknot = {
    'given_name': 'Rufus', 'family_name': 'Drumknot'
}
try:
    result = Person(**drumknot)
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

# An invalid example: Names must be string values!
try:
    result = Person(1, 2)
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

# A simple do_person_things example
ridcully = Person('Mustrum', 'Ridcully')
try:
    result = do_person_things(ridcully)
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

# Creating a dict of arguments, and passing that
stibbons = {
    'given_name': 'Ponder',
    'family_name': 'Stibbons'
}
try:
    result = do_person_things(**stibbons)
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

# An invalid example: There is no given_name
rincewind = {
    'family_name': 'Rincewind'
}
result = do_person_things(**rincewind)
try:
    result = do_person_things(**rincewind)
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

# Another invalid example: Names must be string values!
try:
    result = do_person_things(given_name=1, family_name=2)
    print(result)
except Exception as error:
    print(f'{error.__class__.__name__}: {error}')

