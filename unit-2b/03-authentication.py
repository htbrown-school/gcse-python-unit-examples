# Authentication - Unit 2b

# Example of simple (insecure) authentication selection.
user1 = input("Enter your username: ")
pass1 = input("Enter your password: ")
if user1 != "user1" and pass1 != "asD3e!": # Selection checking against username/password. Would normally be encrypted and checked from database.
    print("Access denied.")
else:
    print("Access granted.")

# Example of authentication selection with loop.
user2 = input("Enter your username: ")
pass2 = input("Enter your password: ")

while user2 != "user2" and pass2 != "ffsi*K": # Essentially replaced if statement with while loop - make sure you re-run the input statements inside.
    print("Access denied.")
    user2 = input("Enter your username: ")
    pass2 = input("Enter your password: ")
print("Access granted.")
