name=input("enter the name")
mark1=int(input("enter the marks of 1 subject"))
mark2=int(input("enter the marks of 2subject "))
mark3=int(input("enter the marks of 3 subject"))
mark4=int(input("enter the marks of 4 subject"))
mark5=int(input("enter the marks of 5 subject"))
avg=(mark1+mark2+mark3+mark4+mark5)/5
print("marks obtained ="+str(avg))
if (avg>=70 ):
    print("name="+name+" "+"marks:"+str(avg)+" "+"Grade is A")
elif(avg>=60 ):
    print("name="+name+" "+"marks:"+str(avg)+" "+ "Grade is B")
elif(avg>=50):
    print("name="+name+" "+"marks:"+str(avg)+" "+"Grade is c")
elif(avg>=43 ):
    print("name="+name+" "+"marks:"+str(avg)+" "+"Grade is D")
elif(avg>=40):
    print("name="+name+" "+"marks:"+str(avg)+" "+"Grade is e")
else:
    print(name+" "+"marks:"+str(avg)+" "+"Grade is f")
