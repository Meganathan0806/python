try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another  number: "))
    result = num1 / num2
    print("Result:", result)

except ZeroDivisionError:
    print(" Cannot divide by zero!")

except ValueError:
    print(" Please enter valid numbers only!")

else:
    print(" Division successful!")

finally:
    print(" Program execution completed.")
