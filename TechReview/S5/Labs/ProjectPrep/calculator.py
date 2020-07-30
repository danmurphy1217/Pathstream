def add(n1,n2):
    return n1 + n2
    


def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1*n2

def divide(n1, n2):
    return n1/n2

def calculate(operation, numbers):
    operation_map = {
        "add" : add,
        "subtract" : subtract,
        "multiply" : multiply,
        "divide" : divide
    }
    n1 = int(numbers[0])
    n2 = int(numbers[1])
    return operation_map[operation](n1, n2)

