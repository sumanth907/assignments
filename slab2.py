name=input("Enter customer name: ")

print("Industrial, commercial and residential slabs available ")

i=int(input("Enter the no. of industrial slabs req'd: "))
ip=5.25*i

c=int(input("Enter the no. of commercial slabs req'd: "))
cp=4.00*c

r=int(input("Enter the no. of residential slabs req'd: "))
rp=3.08*r

total=ip+cp+rp

print("The total bill is: ",total)
print("Thanks")

