class InvalidAgeException(Exception):
    "Raised  when  age is less than 18 "
    pass
number = 18
try:
    age = int(input("Enter  your  age "))
    if age < number:
        raise InvalidAgeException
    else:
        print("Eligible  to  vote ")
except InvalidAgeException:
    print("Exception  is  occured: Invalid  Age ")