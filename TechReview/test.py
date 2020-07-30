def add(num1, num2):
    print("The sum of the numbers is:", num1 + num2)


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
        print(f"{i + 1}: {employees['fnames'][i]} {employees['lnames'][i]}")

def findMax(data):
    """Takes an iterable of integers, data, as input and returns the max item, an integer."""
    max = 0
    for num in data:
        if num > max:
            max = num
    return max


def reverseString(str1):
    '''Takes a string, str1, as input, reverses it, and returns the reversed string.'''
    reverse_str1 = ''
    i = len(str1)
    while i > 0:
        reverse_str1 += str1[i - 1]
        i -= 1 # decrement by 1
    return reverse_str1

def above_zero(num):
    return num >= 0
     
positives = list(filter(lambda num: num%2 == 0, [-1,-3,-5,2,4]))
# print(positives)

my_list = [6,8,10,12,14,16,18,20,22,24,26,28,30]

def my_func(num):
    return num % 4 == 0

x = filter(my_func, my_list)

numbers = [2,4,6,8,10]
squared_numbers = []

for num in numbers:
    squared = num ** 2
    squared_numbers.append(squared)


percentages = ["90.0%", "89.9%", "95%"]

def convert_to_float(num):
    return float(num[:-1])/100

float_list = list(map(convert_to_float, percentages))
product = lambda a,b : a * b

numbers = [-10, 5, 11, -2, -4, 9]

def filter_negatives(num):
    return num >= 0

positive_list = list(filter(filter_negatives, numbers))
positive_list = list(filter(lambda x: x>=0, numbers))

numbers = [2,4,6,8,10]

def square_num(num):
    return num**2

m = map(square_num, numbers)

if __name__ == "__main__":
    # print(findMax.__doc__)
    # print(reverseString("dan murphy"))
    # print(list(x))
    print(squared_numbers)
    print(float_list)
    print(product(3, 5))
    print(positive_list)
    print(list(m))