#TO SWAP TWO VARIABLES
a = int(input("Enter value for a:"))
b = int(input("Enter value for b:"))
print(f"Before swapping: a = {a}, b = {b}")
a,b=b,a
print(f"After swapping: a = {a}, b = {b}")

#COUNTING CHARACTERS IN A STRING
s=input("Enter a string: ")
c=0
for i in s:
    if i!= ' ':
        c+=1
print(f"Number of characters in the string: {c}")

#Given an integer n find the sum of the first n natural number
n = int(input("Enter a natural number: "))
sum=0
for i in range(1, n + 1):
    sum += i
print(f"The sum of the first {n} natural numbers is: {sum}")

#Given an integer n. Write a program to return the last digit of the number
n = int(input("Enter an integer: "))
l = n % 10
print(f"The last digit of the number is: {l}")

#Given two numbers a and b. The task is to find the GCD of a and b. The GCD of two numbers is the largest number that can divide both a and b perfectly.
a=int(input("Enter first number (a): "))
b=int(input("Enter second number (b): "))
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print(f"The GCD of {a} and {b} is: {gcd(a, b)}")

#Given two numbers a and b. The task is to find out their LCM.
def lcm(a, b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            return greater
        greater += 1

a = int(input("Enter first number (a): "))
b = int(input("Enter second number (b): "))

print("LCM of", a, "and", b, "is:", lcm(a, b))


'''You are given a 3-digit number n, Find whether it is an Armstrong number or not.
An Armstrong number of three digits is a number such that the sum of the cubes of its digits is equal to the number itself. 371 is an Armstrong number since 3^3 + 7^3 + 1^3 = 371.'''
n = int(input("Enter a 3-digit number: "))
a=n
l,s=0,0
for i in str(n):
    l=l+1
for i in range(l + 1):
    d = n % 10
    n = n // 10
    s += d ** l
if s == n:
    print(f"{a} is an Armstrong number.")
else:
    print(f"{a} is not an Armstrong number.")

#DECIMAL TO BINARY CONVERSION
n= int(input("Enter a number: "))
s=""
while n > 0:
    s = str(n % 2) + s
    n = n // 2
print(f"The binary representation is: {s}")

#For an integer n, find the number of trailing zeroes in n!
n = int(input("Enter an integer: "))
fac=1
for i in range(1, n + 1):
    fac=fac*i
fac=str(fac)
c=0
for j in fac:
    if j=="0":
        c+=1
print(f"The number of trailing zeroes in {n}! is: {c}")