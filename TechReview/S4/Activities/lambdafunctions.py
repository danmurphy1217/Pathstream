"""Shell activity for adding two numbers w/ lambda"""
add = lambda a, b : a + b
print(add(5, 10))
divide = lambda a, b : a / b
print(divide(20, 4))

"""Embedded IDE activity for lambda"""
employees_db = {
    "name": ["Amani", "Finn", "Harley", "Kamden", "Nola", "Jaylyn"],
    "age": [29, 24, 33, 37, 27, 40],
    "department": ["Product", "Marketing", "Engineering", "Marketing", "Operations", "Product"],
    "salary": [85000, 62500, 150000, 120000, 68250, 175000]
}

increase_age = lambda num : num + 1
employees_db['age'][0] = increase_age(employees_db['age'][0])
print(employees_db['age'])

clean_name = lambda name : name[:-1]
print(clean_name(employees_db['name'][1]))

"""Code for embedded activity using map and filter with lambda"""
employees_db = {
    "name": ["Amani", "Finn", "Harley", "Kamden", "Nola", "Jaylyn"],
    "age": [29, 24, 33, 37, 27, 40],
    "department": ["Product", "Marketing", "Engineering", "Marketing", "Operations", "Product"],
    "salary": [85000, 62500, 150000, 120000, 68250, 175000]
}

print(f"There are\
 {len(list(filter(lambda age : age < 30, employees_db['age'])))}\
 employees under 30")

print(f"Updated salaries:\
{list(map(lambda salary: salary*1.05, employees_db['salary']))}")