try:
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Result:", a / b)
except ZeroDivisionError:
    print("Error: cannot divide by zero")
except ValueError:
    print("Error: please enter valid numbers")
finally:
    print("Program finished.")
