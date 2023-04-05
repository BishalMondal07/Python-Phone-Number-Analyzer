import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Prompt user for phone number input (including country code)
number = input("Enter your phone number (including country code): ")

try:
    # Parse phone number using phonenumbers library
    phone = phonenumbers.parse(number)

    # Get timezone information for phone number
    timezones = ", ".join(timezone.time_zones_for_number(phone))

    # Get carrier information for phone number
    carrier_name = carrier.name_for_number(phone, "en")

    # Get geographic location information for phone number
    location = geocoder.description_for_number(phone, "en")

    # Output results to user
    print(f"Phone number: {phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
    print(f"Timezone(s): {timezones}")
    print(f"Carrier: {carrier_name}")
    print(f"Location: {location}")

except phonenumbers.NumberParseException:
    print("Invalid phone number format!")

except phonenumbers.NumberTypeException:
    print("Invalid phone number type - please enter a valid mobile or landline number!")
import phonenumbers
from phonenumbers import timezone, geocoder, carrier

# Prompt user for phone number input (including country code)
number = input("Enter your phone number (including country code): ")

try:
    # Parse phone number using phonenumbers library
    phone = phonenumbers.parse(number)

    # Get timezone information for phone number
    timezones = ", ".join(timezone.time_zones_for_number(phone))

    # Get carrier information for phone number
    carrier_name = carrier.name_for_number(phone, "en")

    # Get geographic location information for phone number
    location = geocoder.description_for_number(phone, "en")

    # Output results to user
    print(f"Phone number: {phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
    print(f"Timezone(s): {timezones}")
    print(f"Carrier: {carrier_name}")
    print(f"Location: {location}")

except phonenumbers.NumberParseException:
    print("Invalid phone number format!")

except phonenumbers.NumberTypeException:
    print("Invalid phone number type - please enter a valid mobile or landline number!")
