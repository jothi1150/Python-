#Task 1
'''i=1
while i<=100:
     if i==50:
        break
     print(i)
     i+=1'''
#Task 2
correct_password="jothi123"
while True:
    password=input("Enter the password:")
    if password==correct_password:
        print("you can access")
        break
    else:
        print("Wrong password")
