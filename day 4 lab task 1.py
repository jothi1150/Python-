#Task 1
'''i=0
while i<10:
    print(i)
    i+=1'''

#Task 2
'''i=11
while i>1:
    print(i)
    i-=1'''
#Task 3
'''num=2
while num<=20:
    print(num)
    num+=2'''
#Task 4
'''num=1
while num<20:
    print(num)
    num+=2'''
#Task 5
'''num=1
total=0
while num<=50:
   total+=num
   num+=1
print("sum=",total)'''
#Task 6
'''num=int(input("Enter a number:"))

i=1
while i<=10:
    print(num ,"X", i ,"=",num*i)
    i+=1'''
#Task 7
'''num=int(input("Enter the number:"))
count=0
while num>0:
    num//=10
    count+=1
print("number of digits=",count)'''
#Task 8
'''num = int(input("Enter a number: "))
rev = 0

while num > 0:
    digit = num % 10       
    rev = rev * 10 + digit
    num //= 10  

print("Reversed number =", rev)'''
#Task 11
'''a=int(input("Enter num:"))
b=0
t=a
while t>0:
     d=t%10
     b=(b*10)+d
     t=t//10
print(b)
if b==a:
    print("palindrome")
else:
    print("Not a palindrome")'''
#Task 12
'''a=int(input("Enter n:"))
b=0
c=1
t=a
while t>0:
    d=t%10
    b+=d
    c*=d
    t=t//10
print(b)
print(c)
if b==c:
    print("Spy numbers")
else:
    print("Not a spy numbers")'''
#Task 13
'''num=int(input("Enter a numbers:"))
total=0
while num>0:
    digit=num%10
    total+=digit
    num//=10
print("sum of digits",total)'''
#Task 14
'''num=int(input("Enter a numbers:"))
pro=1
while num>0:
    digit=num%10
    pro*=digit
    num//=10
print("productnof digits",pro)'''
#Task 15



    

