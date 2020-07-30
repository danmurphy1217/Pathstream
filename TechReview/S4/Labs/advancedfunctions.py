employees = {
    "id": [0,1,2,3,4],
    "fnames": ["Samantha", "George", "Terry", "Sylvia", "Noreen"],
    "lnames": ["Johnson", "Foreman", "Gergitch", "Plath", "Abar"],
    "depts": ["Marketing", "Product", "Accounting", "Marketing", "Manager"],
    "salaries": [45000, 75000, 35000, 60000, 90000]
}

#Task 2: Write a function change_salary changes a persons salary by a percent. 
#It should take 2 parameters: emp_id and percent, which has a default value of 0.03


#Task 3: Write a function that raises everyones salary by inflation, using change_salary to do so


#TASK 1: Fix this version of print_names so that the variables are not confused
def print_names(emp_list=[-1]):
    print("Employees: ")
    if(emp_list[0]==-1):
        for i in range(len(employees['fnames'])):
             print(f"{i+1}: {employees['fnames'][i]} {employees['lnames'][i]}")
    else:
        for i in emp_list:
            print(f"{i+1}: {employees['fnames'][i]} {employees['lnames'][i]}")

#---2
def change_salary(emp_id, percent = 0.03):
    new_salary = (1 + percent)*(employees['salaries'][emp_id])
    employees['salaries'][emp_id] = new_salary
    return employees['salaries'][emp_id]

def all_inflation_raise():
    for emp_id in employees['id']:
        change_salary(emp_id, percent = 0.03)

while True:
    print("What do you want to do? Choose the options below or 0 to exit")
    option = input("1 -> Print employees | 2 -> give raise | 3 -> Raise all for inflation : ")
    if option == "1":
        # print_names()
        print_names([1,2,3])
    elif option == "2":
        emp_id = int(input("employee id: "))
        percent = float(input("Enter the raise percentage: "))
        print(f"Raised to: {change_salary(emp_id, percent)}")
    elif option == "3":
        all_inflation_raise()
        print(f"New salaries: {employees['salaries']}")
    elif option == "0":
        print("Goodbye!")
        break
    else:
        print("Not a valid choice.")

