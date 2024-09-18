import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(value):   
    if value < 0:
        return False
    
    return is_perfect_square(5 * value * value + 4) or is_perfect_square(5 * value * value - 4)

number = int(input("Enter a number: "))
if is_fibonacci(number):
    print(f"{number} is a Fibonacci number.")
else:
    print(f"{number} is not a Fibonacci number.")
        
    
    