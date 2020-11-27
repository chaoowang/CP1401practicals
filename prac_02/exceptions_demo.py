"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
#When user enter a non-number, eg.a, b
2. When will a ZeroDivisionError occur?
#When user enter 0 as denominator
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#While loop added
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator can not be 0.")
        denominator = int(input("Enter the denominator:"))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
