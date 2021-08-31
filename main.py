import numValidation
import binaryConversion
import reverse
import addition

def Headline():
    print("\n")
    print("\t\t!!Welcome to the Program!!")
    print("\n")
Headline()



Loop=True
while Loop==True:
            FirstNumber=False
            while FirstNumber==False:
                        try:
                                    print("\n")
                                    decimalFirstNumber=int(input("Enter first decimal number: "))
                                    decimalFirstNumber=numValidation.ValidationNum(decimalFirstNumber)
                                    FirstNumber=True
                        except:
                                    print("\n")
                                    print("Invalid Input")
                                    print("\n")
                                    

            SecondNumber=False
            while SecondNumber==False:
                        try:
                                    print("\n")
                                    decimalSecondNumber=int(input("Enter second decimal number: "))
                                    decimalSecondNumber=numValidation.ValidationNum(decimalSecondNumber)
                                    SecondNumber=True
                        except:
                                    print("\n")
                                    print("Invalid Input")
                                    print("\n")
                                    

            Firstnumber=binaryConversion.BinaryConversion(decimalFirstNumber)
            Secondnumber=binaryConversion.BinaryConversion(decimalSecondNumber)

            binaryFirstNumber=reverse.reverse(Firstnumber)
            binarySecondNumber=reverse.reverse(Secondnumber)
            
            binaryAddition=addition.BinaryAddition(binaryFirstNumber,binarySecondNumber)
            print("\n")

            print("Binary number of",decimalFirstNumber," is: ",binaryFirstNumber)
            print("\n")
            print("Binary number of",decimalSecondNumber," is: ",binarySecondNumber)
            print("\n")
            print("Addition of binary number is: ",binaryAddition)
            print("\n")            
            continuous=input("Do you want to continue this application?? (Type no to exit) ").lower()
            if continuous=="no":
                
                
                     break            
            

