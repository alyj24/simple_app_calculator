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
        if selection == '+':
            result1 = ((var1+var2))
        # print the output
            print("The outcome of your input is: ", result1)
        elif selection == '-':
            result2 = ((var1-var2))
            print("The outcome of your input is: ", result2)
        elif selection == '*':
            result3 = ((var1*var2))
            print("The outcome of your input is: ", result3)
        elif selection == '/':
            result4 = ((var1/var2))
            print("The outcome of your input is: ", result4)
        # once again, ask the user if want to try again or not
        option = input("Nice choice of your operation and number! Do you want to try again? (yes, indeed/already satisfied): ")
        if option == "already satisfied"
            print("Thank you!")
            break
    else:
        print("Oh no! There must be a problem in your input to be invalid.")