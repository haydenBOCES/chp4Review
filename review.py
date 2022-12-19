# This is Chapter 4 Review
# If your string length is 9 characters long, the count of characters from 0 to 8
text = "Good Morning!" # 13 characters - count 0-12
print(len(text))

# Subscript operator []
# text[0] - G
# text[7] - r
# check length: len(text)
# Last Character
print(text[-1])
# Count Backwards
print(text[-3]) # n
print(text[-13]) # G

print("Slicing Strings:")
name = 'myfile.txt'
# Entire string
print(name[0:]) # prints entire string
# First Character
print(name[0:1]) # prints character 1 or 'm'
# Entire string example 2:
print(name[:len(name)]) # entire string
# First 2 characters
print(name[0:2]) # prints 2 characters or 'my'
# First 5 characters
print(name[0:5])
# Last 3 characters
print(name[-3:])

# 4-1d Testing for a Substring with the in Operator
print()
print("4-1d Testing for a Substring with the in Operator")
fileList = ["myfile.txt", "myprogram.exe", "yourfile.txt"]
for fileName in fileList:
    if ".txt" in fileName:
        print(fileName)

print()
print("Caesar Cipher:")
plainText = "Welcome to Software Development!"
key = 5
code = ""
for ch in plainText:
    ordVal = ord(ch)
    cipherVal = ordVal + key
    if cipherVal > ord('z'):
        # cipherVal = ord('a') + key - (ord('z') - ordVal + 1) # This works the same but is more complicated
        cipherVal -= 26
    code += chr(cipherVal)
print(plainText)
print(code)

print()
print("Decrypt Caesar Cipher")
# code
# key
plainText = ''
for ch in code:
    ordVal = ord(ch)
    cipherVal = ordVal - key
    if cipherVal < ord("a"):
        # cipherVal = ord('z) - (key - (ord('a') - ordVal - 1))
        cipherVal += 26
    plainText += chr(cipherVal)
print(code)
print(plainText)

print()
print('Binary to Decimal')
bitString = input("Enter a string of bits:")
decimal = 0
exponent = len(bitString) - 1
for digit in bitString:
    decimal = decimal + int(digit) * 2 ** exponent
    exponent -= 1
print("The integer value is: ", decimal)

print()
print("Decimal to Binary")
decimal = input('Enter a decimal integer: ')
if decimal == 0:
    print(0)
else: 
    print("Quotient Remainder Binary")
    bitString = ""
    while decimal > 0:
        remainder = decimal % 2
        decimal = decimal // 2
        bitString = str(remainder) + bitString
        print("%5d%8d%12s" % (decimal, remainder, bitString))
    print("The binary representation is: ", bitString)
    