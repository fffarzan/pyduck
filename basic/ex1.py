from datetime import datetime

birth_year = input('What year were you born? ')

current_year = datetime.today().year
age = current_year - int(birth_year)

print(f'Your age is {age}')