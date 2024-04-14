class Person:

    def __init__(
        self,
        family_name,
        given_name,
        honorific = None,
        middle_name = None,
        suffix = None,
        email_address = None,
        phone_number = None
    ):
        self.family_name = family_name
        self.given_name = given_name
        self.honorific = honorific
        self.middle_name = middle_name
        self.suffix = suffix
        self.email_address = email_address
        self.phone_number = phone_number

    @property
    def family_name(self):
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.family_name '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._family_name = value

    @family_name.deleter
    def family_name(self):
        if hasattr(self, '_family_name'):
            del self._family_name

    @property
    def given_name(self):
        return self._given_name

    @given_name.setter
    def given_name(self, value):
        if not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.given_name '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._given_name = value

    @given_name.deleter
    def given_name(self):
        if hasattr(self, '_given_name'):
            del self._given_name

    @property
    def honorific(self):
        return self._honorific

    @honorific.setter
    def honorific(self, value):
        if value and not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.honorific '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._honorific = value

    @honorific.deleter
    def honorific(self):
        if hasattr(self, '_honorific'):
            del self._honorific

    @property
    def middle_name(self):
        return self._middle_name

    @middle_name.setter
    def middle_name(self, value):
        if value and not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.middle_name '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._middle_name = value

    @middle_name.deleter
    def middle_name(self):
        if hasattr(self, '_middle_name'):
            del self._middle_name

    @property
    def suffix(self):
        return self._suffix

    @suffix.setter
    def suffix(self, value):
        if value and not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.suffix '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._suffix = value

    @suffix.deleter
    def suffix(self):
        if hasattr(self, '_suffix'):
            del self._suffix

    @property
    def email_address(self):
        return self._email_address

    @email_address.setter
    def email_address(self, value):
        if value and not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.email_address '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._email_address = value

    @email_address.deleter
    def email_address(self):
        if hasattr(self, '_email_address'):
            del self._email_address

    @property
    def phone_number(self):
        return self._phone_number

    @phone_number.setter
    def phone_number(self, value):
        if value and not isinstance(value, str):
            raise TypeError(
                f'{self.__class__.__name__}.phone_number '
                'expects a str value, but was passed '
                f'"{value}" ({type(value).__name__}).'
            )
        self._phone_number = value

    @phone_number.deleter
    def phone_number(self):
        if hasattr(self, '_phone_number'):
            del self._phone_number
