# Write a program to print all the prime numbers which come in the range entered by the user?

num1 = int(input("Enter the starting number in the range"))

num2 = int(input("Enter the ending number in the range"))

for i in range(num1, num2 + 1):

    if i > 1:

        for j in range(2, i):

            if i % j == 0:

                break

        else:

            print(i)