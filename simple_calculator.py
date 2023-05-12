print("Assignment 5".center(42, "="))
print("\033[92m=" * 42)
print("\033[94mCMPE-103-MODULE-3-EXCEPTION-HANDLING-IN-PYTHON")
print("\033[92m=" * 42)

# create a simple app calculator that will ask the user to choose four basic math operations and ask for two numbers,
# the finally, will display the result.
# last goal of the program is to ask whether the user want to try another problem or not.

# pseudocode
while True:
    # ask the user for its choice of operation and save the input
    print("Great Day, a precious well-being!")
    selection = input("Pick a basic math operation among these four (+|-|*|/): ")
    # use try and except function
    if selection in ('+', '-', '*', '/'):
        # ask the user for two variables to
        try:
             var1 = float(input("Enter your first variable number: "))
             var2 = float(input("Enter your second variable number:"))
        except ValueError:
            print("Oops! Take a look back for a second, there must be a problem.")
# recognize the two input numbers and solve for the choice of operation
# print the output
# once again, ask the user if want to try again or not
