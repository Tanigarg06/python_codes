#Given a positive integer x, the task is to print the numbers from 1 to x in the order as 12, 22, 32, 42, 52, ... (in increasing order).
x = int(input("Enter a positive integer: "))
for i in range(1,x):
        if (i*i)<=x:
            print(i*i, sep=" ", end=" ")

#Given two number n1 and n2, n1 > n2. Find the differences between mathematical tables of n1 and n2 and print in a single line
n1 = int(input("Enter first number (n1): "))
n2 = int(input("Enter second number (n2): "))
for i in range(1, 11):
    diff = (n1 * i) - (n2 * i)
    print(diff, sep=" ", end=" ")

#Print Square Wall 
n=int(input("Enter the size of the square wall: "))
for i in range(n):
    for j in range(n):
        print("*", end="")
    print()

#RIGHT ANGLE TRIANGLE
n = int(input("Enter the number of rows for the right angle triangle: "))
for i in range(1, n + 1):
    for j in range(i):
        print("*", end="")
    print()

#RIGHT ANGLE TRIANGLE (OUTLINE)
n = int(input("Enter the number of rows for the right angle triangle: "))
for i in range(1, n + 1):
    for j in range(i):
        if j == 0 or j == i - 1 or i == n:
            print("*", end="")
        else:
            print(" ", end="")
    print()

#Inverted Right AngleTriangle
n = int(input("Enter the number of rows for the inverted right angle triangle: "))
for i in range(n, 0, -1):
    for j in range(i):
        print("*", end="")
    print()

#PASCAL'S TRIANGLE

#SORTING(GREATEST TO SMALLEST)
