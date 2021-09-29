# Subroutines - Unit 2

# Proceedure - no returned value
def exampleProceedure(msg):
    print("Example proceedure ran.")
    print("Message:", msg)

exampleProceedure("This is an example proceedure which doesn't return a value.") # Call the proceedure. Includes "msg" parameter.

# Function - returns a value
def exampleFunction(msg):
    print("Example function ran.")
    print("Message:", msg)
    return msg

var1 = exampleFunction("This is an example function which returns a value.") # Call the function and set variable "var1" to the returned value.
print(var1) # Print the variable generated when the function was called.

