# Local and Global Variables - Unit 2

var1 = "This is a global variable." # Defining a global variable is simple - it just has to be outside of any subroutines in Python.

def func(param):
    var1 = "This is a local variable." # Because this variable is in a function, it is only usable within the function's boundaries.
    print(var1) # Will output "This is a local variable." because it is referencing the local variable inside the function.
    return param # Subroutine parameters also have a local scope - they can only be used in their specific function.
print(func("This is a parameter."))

print(var1) # Will output "This is a global variable." as it is referencing the global variable defined at the top.