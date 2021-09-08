def add(a,b):
    print(f"ADDING {a} + {b}")
    return a + b

def substract(a, b):
    print(f"SUBSTRACTING {a} - {b}")
    return a - b

def returno():
    print("you could return just this:")
    return 10000

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b
# %%
print("Let's do some math with just functions!")

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

# age + (substract - iq/2*weight)
what = add(age, substract(height, multiply(weight,divide(iq,2))))
print("That becomes: ", what, "\tCan you do it by hand?")
# formula
tt = divide(add(24,32),substract(100,1023))