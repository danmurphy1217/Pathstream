# INCOMPLETE

census_data = {
    'household_id': [1,2,3,4], 
    'household_address': ["4824 Poplar Street, Neoga, Illinois","4829 Poplar Street, Neoga, Illinois‌","4832 Poplar Street, Neoga, Illinois", "4837 Poplar Street, Neoga, Illinois"],
    'number_of_residents': [5,4,4,6], 
    'residents_ages':[[14,15,18,50,54],[9,9,39,42],[2,4,38,39],[9,12,17,54,58,81]]
}

#Task 1: Write a function called get_years_born(), that fits the docstring below.

#---1

def get_years_born(house_ages):
    '''Takes a list of a single household's ages as input, and returns a list of the years they were born.'''
    return [2020-age for age in house_ages]

#Task 2: Write a function called get_all_years_born(), that fits the doctring below.
    
    '''Returns a list of lists of the years residents were born, based on their ages'''

#---2


#Task 3: Revise the inner for loop of this function to use a list comprehension.
def get_house_numbers():
    '''Searches the addresses of households and extracts their house number, returning them as list of integer values'''
    addresses = census_data['household_address']
    numbers = []
    for address in addresses:
        number = ""
        #Change to list comprehension:
        for char in address:
            if char.isdigit():
                number = number + char
            else:
                break
        numbers.append(int(number))
    return numbers
#---3
print(get_years_born([age for ages in census_data['residents_ages'] for age in ages]))            
# print(get_all_years_born())
# print(get_house_numbers())
