def reverse(NumberList):
            Binary=[]
            BinaryNumber=""
            for i in range(len(NumberList)-1,-1,-1):
                        Binary.append(NumberList[i])
                        BinaryNumber=BinaryNumber+str(NumberList[i])
            return BinaryNumber
