name=input("Enter Employee name: ")
sal=float(input("Enter salary: "))
d=input("Enter designation(m/a/c): ")

if d=="m" or d=="M" :
    bonus= sal*20/100

elif d=="a" or d=="A" :
    bonus = sal * 10 / 100

elif d=="c" or d=="C" :
    bonus = sal * 5 / 100

else:
    print("Invalid input")

ts=sal+bonus
print(name)
print("Total salary= ",ts)
print("Thanks")
