num = float(input("Enter a number"))
if num > 0:
    print("{0} is a postive number".format(num))
elif num == 0:
    print("{0} is zero".format(num))
else:
    print("{0} is a negative number".format(num))

"""
In the above example, elif statement is used. 
The elif statement is used to check multiple expressions for TRUE and executes a block of code when one of the conditions becomes TRUE.
"""