import random
import string
codeOrDecode=input("enter code or decode\n")
string1=input("enter string\n")

def code(stri):
    #code logic
    if len(stri)<3:
        return stri[::-1]
    else:
        encodedString=stri[1:]+stri[0]
        alphabets = random.choices(string.ascii_lowercase, k=3)
        alphabets=alphabets[0]+alphabets[1]+alphabets[2]
        encodedString=alphabets+encodedString+alphabets
        return encodedString

def decode(stri):
    if len(stri)<3:
        return stri[::-1]
    else:
        decodedString=stri[3:-3]
        decodedString=decodedString[-1]+decodedString[:-1]
        return decodedString



if codeOrDecode =='code':
    print(code(string1))
elif codeOrDecode =='decode':
    print(decode(string1))



