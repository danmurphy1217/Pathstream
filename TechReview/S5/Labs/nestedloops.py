census_data = {
    'household_id': [1,2,3,4], 
    'household_address': ["4824 Poplar Street, Neoga, Illinois","4829 Poplar Street, Neoga, Illinois‌","4832 Poplar Street, Neoga, Illinois", "4837 Poplar Street, Neoga, Illinois"],
    'number_of_residents': [5,4,4,6], 
    'residents_ages':[[14,15,18,50,54],[9,9,39,42],[2,4,38,39],[9,12,17,54,58,81]]
}

#Task 1: Complete get_house_numbers() so that it returns a list of the house numbers for each address
# It must use a nested for loop.
def get_house_numbers():
    '''Searches the addresses of households and extracts their house number, returning them as list of integer values'''
    numbers = []
    addresses = census_data['household_address']
    for address in addresses:
        number_str = ""
        for char in address:
            if char.isdigit():
                number_str += char
        final_number = int(number_str)
        numbers.append(final_number)
    return numbers

#---1


#Task 2: Complete count_children() so that it completes the dictionary to contain 2 lists: one with the number of children in each household, and one with the number of adults.
# It must use a nested for loop.
def count_children():
    '''count the number of children and adults in each household and return it as a dictionary.'''
    all_ages = {
        'children': [],
        'adults': []
    }
    house_ages = census_data['residents_ages']
    for house in house_ages:
        children = 0
        adults = 0
        for age in house:
            if age < 18:
                children +=1
            else:
                adults += 1
        all_ages['adults'].append(adults)
        all_ages['children'].append(children)
    return all_ages

#---2



print(get_house_numbers())
print(count_children())
