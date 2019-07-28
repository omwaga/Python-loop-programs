"""
Factorial is a non-negative integer.
It is the product of all positive integers less than or equal to that number for which you ask for factorial.
 It is denoted by exclamation sign (!).
 """

num = int(input("Enter a number:"))

factorial = 1
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)