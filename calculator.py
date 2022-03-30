"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def tokenization(str): 
    tokens = str.split(' ')
    if tokens[0] == "add": 
        return add(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "subtract": 
        return subtract(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "multiply": 
        return multiply(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "divide": 
        return divide(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "square": 
        return square(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "cube": 
        return cube(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "power": 
            return power(int(tokens[1]), int(tokens[2]))
    if tokens[0] == "mod": 
            return mod(int(tokens[1]), int(tokens[2]))

print(tokenization("power 3 5"))

