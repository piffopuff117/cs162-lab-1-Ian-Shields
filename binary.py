userInt=int(input("Input a number "))
print(userInt)
if userInt == 0:
    print("It's just 0")
    
if userInt < 0:
    print("Please enter a positive value")

def intToBinary(x):
    quotient = 1
    binaryStr = ""
    while quotient != 0:
        divInt= divmod(x,2)
        quotient= divInt[0]
        x=quotient
        remainder = str(divInt[1])
        binaryStr += remainder
    print(binaryStr[::-1])

if userInt > 0:
    intToBinary(userInt)
    
