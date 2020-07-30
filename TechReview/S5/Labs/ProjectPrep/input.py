import calculator 

def main():
    user_numbers = input("Please input two numbers: ").replace(",", " ").split() 
    calc = get_calculation()
    nums = get_numbers()
    print(calculator.calculate(calc, nums))




def get_calculation():
    user_calculation = ""
    while user_calculation not in ["add", "subtract", "multiply", "divide"]:
        user_calculation = input("What calculation would you like to perform? Try add, subtract, multiply or divide.").strip().lower()
    return user_calculation

def get_numbers():
    user_numbers = []
    while len(user_numbers) != 2:
        user_numbers = input("Enter two numbers separated by commas.").replace(",", " ".split())
    return user_numbers


main = main()
