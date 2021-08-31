def BinaryConversion(decimalNumber):
            bit=[]
            BinNum=""
            counter=0
            while counter!=8:
                        Remainder=decimalNumber%2
                        bit.append(Remainder)
                        decimalNumber=decimalNumber//2
                        counter=counter+1
            return bit

