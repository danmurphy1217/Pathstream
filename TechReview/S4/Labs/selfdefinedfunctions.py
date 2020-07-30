employees = {
    "fnames": ["Samantha", "George", "Terry", "Sylvia", "Noreen"],
    "lnames": ["Johnson", "Foreman", "Gergitch", "Plath", "Abar"],
    "depts": ["Marketing", "Product", "Accounting", "Marketing", "Manager"],
    "salaries": [45000, 75000, 35000, 60000, 90000]
}

#TASK 1: Define the names of 3 functions: print_names(), find_emp(), and add_emp() in the areas marked for tasks 2, 3, and 4 below.

#TASK 2: Write a function that prints the full names of employees in a list
def print_names():
    for i in range(len(employees['fnames'])):
        print(f"{i+1}: {employees['fnames'][i]} {employees['lnames'][i]}")

#---2

#TASK 3: Write a function that finds the whole name of an employee given their first name or last name
def find_emp(col_name, name):
    names = employees[col_name]
    if name in names:
        i = names.index(name)
        # return str(employees['fnames'][i]) + " " + str(employees['lnames'][i])
        return f"{employees['fnames'][i]} {employees['lnames'][i]}"
    else:
        return "Name not found."
#---3

#TASK 4: Write a function that adds a new employee to the dictionary, as long as the department is valid.
def add_emp(first_name, last_name, department, salary):
    if department not in employees['depts']:
        return False
    employees['fnames'].append(first_name)
    employees['lnames'].append(last_name)
    employees['depts'].append(department)
    employees['salaries'].append(salary)
    return True
#---4
#---1


while True:
    print("What do you want to do? Choose the options below or 0 to exit")
    option = input("1 -> Print employees | 2 -> Find Employee | 3 -> Add employee  :")
    if option == "1":
        print_names()
    elif option == "2":
        criteria = input("Search by 'fnames' or 'lnames'?: ")
        name = input("Enter the name: ")
        print(find_emp(criteria, name))
    elif option == "3":
        fname = input("First Name: ")
        lname = input("Last Name: ")
        dept = input("Department: ")
        salary = input("Salary: ")
        if add_emp(fname, lname, dept, salary):
            print(f"Employee added: {employees['fnames'][-1]}")
        else:
            print("Error adding employee")
    elif option == "0":
        print("Goodbye!")
        break
    else:
        print("Not a valid choice.")