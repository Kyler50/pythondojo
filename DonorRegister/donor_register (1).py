import datetime
import random

NOT_SUITABLE_PREFIX = "Unfortunately the donor is not suitable for donation because"


def print_separator_line():
    print("-"*32)


def greetings():
    print("Welcome in the blood donor register application!!")
    print_separator_line()
    print("Please enter donor's information:")


def get_name(name_type):
    return input("{0}: ".format(name_type))


def get_weight():
    """
    get the weight from the user
    if it is an empty string then warn the user
    """

    weight_str = input("Weight in kg: ")
    if weight_str == "":
        print("The data what you gave is not a valid weight!")
    # any other validation can come here
    return int(weight_str)


def validate_weight(weight_value):
    if weight_value < 50:
        print("{0} his/her weight is under 50kg!".format(NOT_SUITABLE_PREFIX))


def get_age_by_birthdate(birth_date):
    today = datetime.date.today()
    return (today - birth_date).days // 365


def get_date(input_text):
    return datetime.datetime.strptime(input(input_text + " (mont day year): "), "%m %d %Y").date()


def validate_birth(birth_date):
    if not get_age_by_birthdate(birth_date) < 18:
        print("{0} her/his age under 18!".format(NOT_SUITABLE_PREFIX))


def validate_last_donation(last_donation):
    today = datetime.date.today()
    if (today - last_donation).days < 90:
        print("{0} her/his last donation has been in 3 months!".format(NOT_SUITABLE_PREFIX))


def validate_id_expiration(expiration):
    if expiration < datetime.date.today():
        print("{0} her/his personal document has expired !".format(NOT_SUITABLE_PREFIX))


def validate_email(email):
    is_valid = (email.find("@") > 0) and (email.endswith(".hu") or email.endswith(".com"))
    if not is_valid:
        print("Email address is not valid!")


def validate_mobil_number(number_to_validate):
    providers = ["20", "30", "70"]
    start_is_valid = False
    provider_index = 2

    if number_to_validate.startswith("06"):
        start_is_valid = True
    elif number_to_validate.startswith("+36"):
        start_is_valid = True
        provider_index = 3

    provider_is_valid = number_to_validate[provider_index:provider_index+2] in providers
    ending_is_digit = number_to_validate[provider_index+2:].isdigit()

    is_valid = start_is_valid and \
               provider_is_valid and \
               len(number_to_validate) in [11, 12] \
               and ending_is_digit

    if not is_valid:
        print("Mobil number is not valid!")


def validate_hemoglobin(hemoglobin_level):
    if hemoglobin_level <= 110:
        print("{0} because her/his hemoglobin level is too low!".format(NOT_SUITABLE_PREFIX))


def validate_donor(donor_info):
    validate_weight(donor_info["weight"])
    validate_birth(donor_info["date_of_birth"])
    validate_last_donation(donor_info["last_donation_date"])
    validate_id_expiration(donor_info["id_expiration"])
    validate_email(donor_info["email"])
    validate_mobil_number(donor_info["mobil_number"])
    validate_hemoglobin(donor_info["hemoglobin"])


def get_donor_data():
    return {
        "last_name": get_name("Last name"),
        "first_name": get_name("First name"),
        "weight": get_weight(),
        "gender": input("Male (m) / Female (f): "),
        "date_of_birth": get_date("Date of birth"),
        "last_donation_date": get_date("Last donation date"),
        "was_sick": input("Was she/he sick in the last month? (y/n)"),
        "id": input("Personal document identifier: "),
        "id_expiration": get_date("Expiration of personal document"),
        "blood_type": input("Blood type: "),
        "email": input("Email address: "),
        "mobil_number": input("Mobil number: "),
        "hemoglobin": random.randint(80, 200)
    }


def get_personal_document_type(personal_document):
    if personal_document[:6].isdigit() and personal_document[6:].isalpha():
        return "Identity card"
    else:
        return "Passport"


def print_donor_info(donor_info):
    age = str(get_age_by_birthdate(donor["date_of_birth"]))
    print("""{0}, {1}
    {2}kg
    {3} - {4} years old
    {5}
    """.format(donor_info["first_name"], donor["last_name"],
               donor_info["weight"],
               donor_info["date_of_birth"], age,
               donor_info["email"]))


if __name__ == '__main__':
    greetings()
    donor = get_donor_data()
    print_separator_line()
    validate_donor(donor)
    print_separator_line()
    print_donor_info(donor)
