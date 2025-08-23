import debug

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a + b  

def divide(a, b):
    if b == 0:
        raise ValueError("Division by zero!")
    return a / b

# Program logic
def calculator():
    x, y = 6, 0
    print(f"Numbers: {x}, {y}")

    result1 = add(x, y)
    print("Add:", result1)

    result2 = subtract(x, y)
    print("Subtract:", result2)

    result3 = multiply(x, y)   # will stop here automatically
    print("Multiply:", result3)

    result4 = divide(x, y)
    print("Divide:", result4)

if __name__ == "__main__":
    calculator()
