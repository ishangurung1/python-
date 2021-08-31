number=int(input("enter the number"))
i=2
prime=True
while i<number:
    if number%i==0:
        print("the numberis not prime")
        prime=False
    i+=1
if prime==True:
    print("the number is prime")
