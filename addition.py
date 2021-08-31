import reverse
def _xor(x,y):
    if (x==y):
        return '0'
    else:
        return '1'

def _and(x,y):
    if (x=='1' and y== '1'):
        return '1'
    else:
        return '0'
    
def _or(x,y):
    if (x=='0' and y=='0'):
        return '0'
    else:
        return '1'         


           


            

def BinaryAddition(number1,number2):
    str1= str(number1)
    str2= str(number2)

    for i in range (0,(8-len(str1)),+1):
        str1='0' + str1

    for i in range (0,(8-len(str2)),+1):
        str2='0' + str2

    _sum = ''
    carry ='0'

    for i in range (7,-1,-1):
        x,y = str1[i], str2[i]
        _sum= _xor (_xor(x,y),carry) + _sum
        carry= _or(_and(x,y),_and(_xor(x,y),carry))

    if(carry=='0'):
        return _sum
    else:
         print("\n")
         print("Sorry!this program only supports 8-bit addition")

        

