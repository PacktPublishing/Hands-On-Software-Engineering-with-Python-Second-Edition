from hms.core.business_objects import Artisan, Address
from pydantic import EmailStr, NameEmail
from typing import Union

def input_to_artisan(data: dict) -> Artisan:
    # Manually rehydrate nested address
    address = Address(**data.pop("businessAddress"))

    # Manually coerce email string to EmailStr or NameEmail
    email_raw = data.pop("emailAddress")
    try:
        email = EmailStr(email_raw)
    except ValueError:
        email = NameEmail(email_raw)

    return Artisan(business_address=address, email_address=email, **data)

def artisan_to_dict(artisan: Artisan) -> dict:
    return {
        "oid": str(artisan.oid),
        "honorific": artisan.honorific,
        "givenName": artisan.given_name,
        "middleName": artisan.middle_name,
        "familyName": artisan.family_name,
        "suffix": artisan.suffix,
        "companyName": artisan.company_name,
        "emailAddress": str(artisan.email_address),
        "businessAddress": artisan.business_address.model_dump(mode="json")
    }
