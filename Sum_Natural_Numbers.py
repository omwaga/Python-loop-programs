"""
As the name specifies, a natural number is the number that occurs commonly and obviously in the nature.
 It is a whole, non-negative number
"""

num = int(input("Enter a number: "))

if num < 0:
    print("Enter a positive number")
else:
    sum = 0
    # use while loop to iterate un till zero
    while (num > 0):
        sum += num
        num -= 1
    print("The sum is", sum)