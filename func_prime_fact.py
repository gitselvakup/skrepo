# Python program to print first 10
# prime numbers

# A function name prime is defined
# using def
def python_def_prime(n):
    x = 2
    count = 0
    while count < n:
        for d in range(2, x, 1):
            if x % d == 0:
                x += 1
        else:
            print(x)
            x += 1
            count += 1

# Driver Code
n = 10

# print statement
print("First 10 prime numbers are:  ")
python_def_prime(n)

print("\n")

# Python program to find the
# factorial of a number

# Function name factorial is defined
def fact(n):
    if n == 1:
        return n
    else:
        return n*fact(n-1)

# Main code
num = int(input("Enter the value: "))

# check is the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", fact(num))
