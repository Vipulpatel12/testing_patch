
def add(num1, num2):
    """Adds two numbers together.
    
    Args:
        num1 (int or float): The first number to be added.
        num2 (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    """Subtracts the second number from the first number.
    
    Args:
        num1 (float): The first number from which the second number will be subtracted.
        num2 (float): The second number to be subtracted from the first number.
    
    Returns:
        float: The result of the subtraction of num2 from num1.
    """
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    """Multiplies two numbers.
    
    Args:
        num1 (float or int): The first number to be multiplied.
        num2 (float or int): The second number to be multiplied.
    
    Returns:
        float or int: The product of num1 and num2.
    """
    return num1 * num2

def add_1_(num1, num2):
    """Adds two numbers together.
    
    Args:
        num1 (int or float): The first number to be added.
        num2 (int or float): The second number to be added.
    
    Returns:
        int or float: The sum of num1 and num2.
    """
    return num1 + num2

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
    print(number_1, "+", number_2, "=",
                    add(number_1, number_2))

elif select == 2:
    print(number_1, "-", number_2, "=",
                    subtract(number_1, number_2))

elif select == 3:
    print(number_1, "*", number_2, "=",
                    multiply(number_1, number_2))

elif select == 4:
    print(number_1, "/", number_2, "=",
                    divide(number_1, number_2))
else:
    print("Invalid input")
    
    