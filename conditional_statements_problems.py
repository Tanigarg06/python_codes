#Given a positive integer x. Your task is to check, if it is even or odd
x = int(input("Enter a positive integer: "))
if x % 2 == 0:
    print(f"{x} is even.")
else:
    print(f"{x} is odd.")

#EVEN_ODD_GAME
'''Given a number n, number of apples in a bag. You and your friend are picking one apple turnwise from the bag. It is given that the first attempt is always by you. The person picking the last apple will be the winner. 
If you will win: print "You" (without quotes)
If your friend will win: print "Friend" (without quotes)'''
n = int(input("Enter the number of apples: "))
if n % 2 == 1:
    print("WINNER:You")
else:
    print("WINNER:Friend")

#Given three numbers a, b, and c. You need to find which is the greatest of them all.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print(f"Greatest: {a}")
elif b > a and b > c:
    print(f"Greatest: {b}")
else:
    print(f"Greatest: {c}")

#leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("True")
else:
    print("False")

#PRIME_NUMBER
n= int(input("Enter a number: "))
fac=0
for i in range(1, n+1):
    if n % i == 0:
        fac += 1
if fac == 2:
    print("Prime")
else:
    print("Not Prime")  

#FIBONACCI SERIES
n= int(input("Enter the number of terms in Fibonacci series: "))
a, b = 0, 1
c=a+b
cnt=3
print("Fibonacci Series:\n",a,"\n",b)
while cnt<=n:
    print(c)
    a=b
    b=c
    c=a+b
    cnt+=1

#PERFECT_NUMBER
n = int(input("Enter a number: "))
sum=0
for i in range(1, n):
    if n % i == 0:
        sum += i
if sum == n:
    print("Perfect")
else:
    print("Not Perfect")

#Given a number N, write a program to check whether given number is Adam Number or not.
N= int(input("Enter a number: "))
n2=N*N
rev=str(N)
rev = rev[::-1]
print("reverse of inputed number is:", rev)
rev=int(rev)
rev2=rev*rev
print("square of reversed inputed number is:", rev2)
r=str(n2)
r = r[::-1]
r=int(r)
print("reverse of squared inputed number is:", r)
if rev2 == r:
    print("Adam Number")
else:       
    print("Not Adam Number")

#STRONG_NUMBER
n = int(input("Enter a number: "))
sum=0
for i in str(n):
    temp=int(i)
    fact=1
    for j in range(1,temp+1):
        fact *= j
    sum += fact
    temp=0
if sum == n:
    print("Strong Number")      
else:
    print("Not Strong Number")