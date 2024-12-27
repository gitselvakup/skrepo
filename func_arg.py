#Exercise 2: Create a function with variable length of arguments
def func1(*args):
    for i in args:
        print(i)

func1(20, 40, 60,70,80,90,100)
func1(80, 100)
func1(120,140)

print("\n")
#Exercise 3: Return the function multiple values from a function

def calc(a, b):
    addition = a + b
    subtraction = a - b
    multiple= a * b
    # return multiple values separated by comma
    return addition, subtraction, multiple

# get result in tuple format
res = calc(40, 10)
res1=calc(50,60)
print(res)
print(res1)
print("\n")

#Ex 4: Create a function with a default argument

def show_employee(name, salary=9000):
    print("Name:", name, "salary:", salary)

show_employee("John", 12000)
show_employee("Julie")

# argument with int values
def int_def(a, b=10):
    print("fval:", a, "sval:", b)

int_def(10,30)
int_def(15)




