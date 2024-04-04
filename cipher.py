alpha = ("abcdefghijklmnopqrstuvwxyz")

print("Welcome to the Caeser Cypher!")
begin = input("Would you like to encode (e) or decode (d) ? ").lower()
textgiven=input("What is your text? ").lower()
shift=5

def encrypt(textgiven, shift):
    encodedtext = ' '
    for letter in textgiven:
        index = alpha.find(letter)
        newalpha = index + shift
        if newalpha >= 26 :
            newalpha -=26
        encodedtext += alpha[newalpha]
    return encodedtext

def decrypt(textgiven, shift):
    decodedtext = ' '
    for letter in textgiven:
        index = alpha.find(letter)
        newalpha = index - shift
        if newalpha <0 :
            newalpha +=26
        decodedtext += alpha[newalpha]
    return decodedtext

if begin == "e":
    encodedtext = encrypt(textgiven, shift)
    print (encodedtext)

if begin == "d":
    decodedtext = decrypt(textgiven, shift)
    print(decodedtext)





    
