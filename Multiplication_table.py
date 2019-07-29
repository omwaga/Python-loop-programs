"""outputs multiplication table according to user input
you can make a program to display the multiplication table of any number.
The following program displays the multiplication table (from 1 to 10) according to the user input."""

num = int(input("Show the multiplication table of:"))

#using for loop to iterate 10 times
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)