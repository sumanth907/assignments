name=input("Enter customer name: ")

print("For industrial slab press I/i, For commercial slab press C/c,"
      "for residential slab press R/r")

a=input("choose slab type: ")

if a=="I" or a=="i":
    n=int(input("Enter no. of units req'd: "))
    ip=5.25*n
    print("Total bil is ",ip)

elif a=="C" or a=="c":
    n = int(input("Enter no. of units req'd: "))
    cp=4.00*n
    print("Total bil is ", cp)

elif a=="R" or a=="r":
    n = int(input("Enter no. of units req'd: "))
    rp=3.08*n
    print("Total bil is ", rp)

else:
    print("Invalid input")

print("Thanks")
