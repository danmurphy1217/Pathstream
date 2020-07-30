# needs to be fixed
from calculator import add

def main():
    user_numbers = user_numbers = input("Please input two numbers separated by commas: ").replace(",", " ").split()
    n1 = user_numbers[0]
    n2 = user_numbers[1]
    return add(n1, n2)
    

print(main())