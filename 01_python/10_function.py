# define a function
# a function is a block of code that only runs when it is called 
# a function can take arguments and return a value
# a function can also have default arguments
# # make a function that prints a message
# def my_function():
#     print("Hello from a function")
# my_function()


# # make a function that takes an argument
# def my_function_with_argument(name):
#     print(f"Hello {name} from a function with an argument")
# my_function_with_argument("sami")
# make a function that takes an argument with a default value
def my_function_with_default_argument(name="Guest"):
    print(f"Hello {name} from a function with a default argument")
# my_function_with_default_argument("sami")
my_function_with_default_argument()
 
# return a value from a function
def saquare(number):
    return number * number  
# call the function and print the result
print(saquare(5))



# make a function that takes two arguments and returns their sum
def add_numbers(a, b):
    return a + b
# call the function and print the result
print(add_numbers(3, 4))


# recursion: a function that calls itself
# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         return n * factorial(n - 1)
#     # call the recursive function and print the result
#     print(factorial(5))
 
    # lambda function: a small anonymous function
add_numbers = lambda x, y: x + y
    # call the lambda function and print the result
print(add_numbers(3, 4))