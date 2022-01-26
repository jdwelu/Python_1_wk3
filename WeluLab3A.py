# Function that takes two strigs, concatenates them, and then prints 
# Attempt 1
def append0(text0, text1):
    return text0 + " " + text1

x = append0("Hello", "World")
print(x)

# Attempt 2
def append1(arg0, arg1):
    print(arg0 + " " + arg1)

append1("Goodbye", "World")


# Function that has a single number parameter. If less than 0, return 0.
# Otherwise it returns the original value.
# Attempt 1
def positiveNumber0(num0):
    if num0 >= 0:
        return num0
    else:
        return 0 

# Testing 5 numbers in the function. Using print to see results.
print()
print(positiveNumber0(-5))
print(positiveNumber0(-1))
print(positiveNumber0(0))
print(positiveNumber0(1))
print(positiveNumber0(5))
print()


# Function that takes a parameter and figures out if it is odd or even.
# Attempt 1
def evenOdd0(num1):
    mresult = num1 % 2
    if mresult == 0:
        return True
    else:
        return False

# Testing the function for boolean results.
print()
print(evenOdd0(3))
print(evenOdd0(45))
print(evenOdd0(22))
print(evenOdd0(100))
print()


# Function that tests whether a number is between 0-100 (century range).
# Attempt 1
def inCenturyRange0(num2):
    if 0 <= num2 <= 100:
        return True
    else:
        return False

# Testing the function for boolean results.
print()
print(inCenturyRange0(-25))
print(inCenturyRange0(0))
print(inCenturyRange0(25))
print(inCenturyRange0(75))
print(inCenturyRange0(125))
print()


# Function that takes two parameters (string and number) concatenates them
# and prints them a number of times equal to the number given.
def repeater0(text2, num3):
    for a in range(num3):
        print(text2, " ", str(num3))

# Testing the function, following the model from the book page 105.
text2 = "HEY WHAT IS THIS NUMBER -->"
num3 = 3
print()
repeater0(text2, num3)
print()
repeater0("HEY LOOK AT THIS NUMBER -->", 14)

