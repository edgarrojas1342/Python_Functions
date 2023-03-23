#Functions - Block of code that is designed to perform a specific task. Only RUNS when its CALLED.
#   - Built in functions
#   - Create custom functions
#   - Break up our code into smaller -- !reusable parts!
# def say_hello(name):
    # print("Hello, " + name + "!")

#Calling the function
# say_hello('Edgar')

def add_numbers(x,y):
    return x + y 

def calculate_total(x,y,z):
    total = add_numbers(x,y)
    sum = add_numbers(total, z)
    return sum


result = calculate_total(3,4,5)
print (result)

def say_hello(name='World!'):
    print("Hello" + name)

say_hello()
say_hello('Edgar')