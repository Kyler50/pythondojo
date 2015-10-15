__author__ = 'Vas Richard Roland'
from datetime import datetime
available_cities = ("miskolc", "szerencs", "sarospatak", "kazincbarcika")


def parse_date(date_string):
    return datetime.strptime(date_string,'%Y.%m.%d')
def check_date_and_time_of_event(date_and_time_of_event):
      date_parts = date_and_time_of_event.split(".")
      if len(date_parts) == 3:
        for part in date_parts:
            if not part.isdigit():
                print("Bad date format ! It should be YYYY.MM.DD !")
                return False
        return True
      print("Bad date format ! It should be YYYY.MM.DD !")
      return False


def parse_time_text(time_string):
    return datetime.strptime(time_string,'%H.%M')


def check_time_text(time_text):
      text_parts = time_text.split(".")
      if len(text_parts) == 2:
        for part in text_parts:
            if not part.isdigit():
                print("Bad time format ! It should be HH.MM !")
                return False
        return True
      print("Bad date format ! It should be HH.MM !")
      return False

def calculate_duration_in_minutes(start, end):
    return (end - start).seconds // 60

def max_donor_number(duration_in_minutes, preparation_time, donation_time, available_beds):
    return ((duration_in_minutes - preparation_time) / donation_time) * available_beds

def check_zip_code(zip_code):
   if not zip_code.isdigit():
        print("Zip code should be digits !")
        return False
   return True


def check_available_beds(available_beds):
    if available_beds == "":
        print("Beds number can't be empty")
    if not available_beds.isdigit():
        print("Beds number should be digits!")
        return False
    return True


def check_planned_donor_number(planned_donor_number):
   if planned_donor_number == "":
        print("Donors number can't be empty")
        return False
   return True


def validate_date_and_time_of_event(date_and_time_of_event):
    date_event = parse_date(date_and_time_of_event)
    date_and_time_of_event = date_event - datetime.now()
    if date_and_time_of_event.days < 10:
        print("The event should be kept after 10 days")
        return False
    if date_event.isoweekday() == 6 or date_event.isoweekday() == 7:
        print("Datetime can be only on weekdays")
        return False
    return True
def get_date_and_time_of_event():
    date_and_time_of_event_string = ""
    while not validate_date_and_time_of_event(date_and_time_of_event_string):
        date_and_time_of_event_string = input("Enter the date of event")
    return date_and_time_of_event_string



def validate_zip_code(zip_code):
  if (zip_code.startswith("0")):
    print("Zip code can't start with 0")
    return False
  if len(zip_code) != 4:
    print("Zip code should be exactly 4 characters long !")
    return False
  return True
def get_zip_code():
    zip_code_string = ""
    while not validate_zip_code(zip_code_string):
        zip_code_string = input("Enter the zip code")
    return zip_code_string



def validate_address(address):
    if not len(address) <= 25:
        print("Too long")
        return False
    return True
def get_address():
    address_string = ""
    while not validate_address(address_string):
        address_string = input("Enter the address")
    return address_string



def validate_city(city):
    if city.lower() not in available_cities:
        print("Not good city")
        return False
    return True
def get_city():
    city_string = ""
    while not validate_city(city_string):
        city_string = input("Enter the city")
    return city_string


def get_start_time():

    while start_time_text == "":
        start_time_text = ""
        if not (check_time_text(start_time_text)):
            start_time_text = input("Start time:")

    return start_time

def get_event_data():
    date_and_time_of_event = get_date_and_time_of_event()
    start_time_text = get_start_time()
    end_time_text = ""
    zip_code = get_zip_code()
    city = get_city()
    address = get_address()
    available_beds_string = ""
    available_beds = None
    planned_donor_number = ""
    preparation_time = 30
    donation_time = 30


if __name__ == "__main__":
    while date_and_time_of_event == "":
        date_and_time_of_event = input("Event day:")
        if not (check_date_and_time_of_event(date_and_time_of_event) and validate_date_and_time_of_event(date_and_time_of_event)):
            date_and_time_of_event = ""

    while zip_code == "":
        zip_code = input("Code:")
        if not (check_zip_code(zip_code) and validate_zip_code(zip_code)):
            zip_code = ""

    while city == "":
        city = input("City:")
        if not (validate_city(city)):
            city = ""

    while address == "":
        address = input("Address:")
        if not (validate_address(address)):
            address = ""

    while available_beds_string == "":
        available_beds_string = input("Beds number:")
        if not (check_available_beds(available_beds_string)):
            available_beds_string = ""

    available_beds = int(available_beds_string)



    while end_time_text == "":
        end_time_text = input("End time:")
        if not (check_time_text(end_time_text)):
            end_time_text = ""



    start_time = parse_time_text(start_time_text)
    end_time = parse_time_text(end_time_text)
    duration = calculate_duration_in_minutes(start_time, end_time)


    donor = max_donor_number(duration, preparation_time, donation_time, available_beds)
    print(donor)