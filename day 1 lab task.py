#Easy task
#1Tempture converter
'''c=int(input("Enter C:"))
F=int(input("Enter F:"))
print("converts it to Fahrenheit:",c*1.8+32)'''


#2Simple interest Calculator
'''P=int(input("Enter the principal amount:"))
R=int(input("Enter the Annual Rate of interest:"))
T=int(input("Enter the Time:"))
print("Simple Interest:",P*R*T/100)'''


#3Square and Cube Generator
'''S=int(input("Enter n:"))
print("Square Value:",S**2)
print("Cube Value:",S**3)'''

#4Total Minutes & Seconds
'''T=float(input("Enter the hours:"))
h=T*60
s=h*60
print(h)
print(s)'''

#5Average of Three Marks
'''t=int(input("Enter Tamil mark:"))
e=int(input("Enter English mark:"))
m=int(input("Enter Maths mark:"))
print("Final Average Score:",t+e+m/3)'''


#hard task
#6)Digits Extractor
f=345
a=f%10
print("Last digit:",a)
d=a//10
print(d)

#7)Swap Without a Third Variable using bitwise operators
'''a=int(input("enter a value:"))
b=int(input("enter b value:"))
a=a^b
b=a^b
a=a^b
print("swap values:")
print("a=",a)
print("b=",b)'''

#8)ATM Cashier breakdown
'''amount=3800
a=amount//500
b=amount%500
c=b//100
print(" 500 notes:",a)
print("leftover:",b)
print("100 notes:",c)'''

#9)Weeks and Leftover Days Converter
'''days=45
w=days//7
l=days%7
print("weeks:",w)
print("leftover days:",l)'''

#10)Reverse a 2-Digit Number Mathematically
num=27
firstdigit=num//10
seconddigit=num%10
R=(seconddigit*10)+firstdigit
print("Reverse 2 digit num:",R)




