import validators
import regex as re


class Validations:
    NAME_PATTERN = re.compile(r"^\p{L}[\p{L} \'-]*\p{L}$")
    PHONE_PATTERN = re.compile(r"^\+?1?(\(?\d{3}\)?-?\d{3}-?\d{4})$")
    ADDRESS_PATTERN = re.compile(r'^\d+\s[A-Za-z]+\s[A-Za-z]+')
    CITY_PATTERN = re.compile(r"^[A-Za-z]+(?:[\s-][A-Za-z]+)*$")
    ZIP_CODE_PATTERN = re.compile(r'^\d{5}$')
    """
    A class for validating various input fields of a form.
    """

    def __init__(self, first_name, last_name, email, phone, address, city_input, zip_code):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city_input
        self.zip_code = zip_code

    def validate_name(self, name):
        """
        A class for validating various input fields of a form.
        """
        return name.strip() and self.NAME_PATTERN.match(name)

    def validate_email(self):
        """
        Validate the email. It must not be empty and should be a valid email format.
        """
        return self.email.strip() and validators.email(self.email)

    def validate_phone(self):
        return self.phone.strip() and self.PHONE_PATTERN.match(self.phone)

    def validate_address(self):
        return self.address.strip() and self.ADDRESS_PATTERN.match(self.address)

    def validate_city(self):
        return self.city.strip() and self.CITY_PATTERN.match(self.city)

    def validate_zip_code(self):
        return self.zip_code.strip() and self.ZIP_CODE_PATTERN.match(self.zip_code)

    @staticmethod
    def validate_state(selected_state, states):
        """
        Validate the selected state. It should be a valid option from the list of states.
        """
        return selected_state in states and selected_state != states[0]
