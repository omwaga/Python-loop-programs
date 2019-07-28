#outputs multiplication table according to user input

num = int(input("Show the multiplication table of:"))

#using for loop to iterate 10 times
for i in range(1, 11):
    print(num, 'x', i, '=', num*i)