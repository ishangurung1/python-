def ValidationNum(num):
            while num<0 or num>255:
                        print("\n")
                        print("Input invalid")
                        num=int(input("please! enter valid number (0-255) : "))
            return num
