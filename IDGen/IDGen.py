import random
from datetime import datetime

with open('Names.txt', 'r') as file:
    names = file.read().splitlines()
with open('Surnames.txt', 'r') as file:
    surnames = [surname.replace(',', '') for surname in file.read().splitlines()]

random_name = random.choice(names)
random_surname = random.choice(surnames)

def generate_id_number(date_of_birth):
    year_last_two_digits = date_of_birth.year % 100
    month = date_of_birth.month
    day = date_of_birth.day
    # Namibian ID = 11 Digits. So 5 Extra Digits at the end
    # SA ID = 13 Digits. So then 7 Extra Digits at the end
    random_part = ''.join(str(random.randint(0, 9)) for i in range(5))  # 5 random digits 
    id_number = f"{year_last_two_digits:02d}{month:02d}{day:02d}{random_part}"
    return id_number

name = random.choice(names)
surname = random.choice(surnames)

current_year = datetime.now().year
birth_year = current_year - random.randint(18, 60)
birth_month = random.randint(1, 12)
days_in_month = 31

if birth_month in [4, 6, 9, 11]:  # April, June, September, November
    days_in_month = 30
elif birth_month == 2:  # February
    if birth_year % 4 == 0 and (birth_year % 100 != 0 or birth_year % 400 == 0):
        days_in_month = 29  # Leap year
    else:
        days_in_month = 28

birth_day = random.randint(1, days_in_month)

date_of_birth = datetime(birth_year, birth_month, birth_day)

id_number = generate_id_number(date_of_birth)

print("Nam:", name)
print("Sur:", surname)
print("DOB:", date_of_birth.strftime("%d-%m-%Y"))
print("IDN:", id_number)
