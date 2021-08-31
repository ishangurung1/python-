a=int(input("enter the number"))
f=1
i=1
while i<=a:
    f=f*i
    i=i+1
    print("factorial in ascending order"+str(f))
f=1
while a>=1:
    f=f*a
    a=a-1
    print("factorial in decending order"+str(f))
