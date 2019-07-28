#Taake input from the user
lower = int(input("Enter a lower range:"))
upper = int(input("Enter the upper range:"))

for num in range(lower, upper + 1):
    if num > 1:
        for i in range(2, num):
            if(num % i) == 0:
                break
        else:
            print(num)