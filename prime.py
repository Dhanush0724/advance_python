prime = int(input("enter a number to check prime"))

for i in range(2,prime):
    if prime%i==0:
        print("not a prime number")
        break
else :
    print("Prime number")