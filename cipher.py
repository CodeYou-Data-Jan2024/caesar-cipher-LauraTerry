#move alphabet by 5 spaces to the right and add to dictionary

cipher_alphabet ={'a': 'f', 'b':'g', 'c':'h', 'd':'i', 'e':'j', 'f':'k', 'g':'l', 'h':'m', 'i':'n', 'j':'o', 'k':'p', 'l':'q', 'm':'r', 'n':'s', 'o':'t', 'p':'u', 'q':'v', 'r':'w', 's':'x', 't':'y', 'u':'z', 'v':'a', 'w':'b', 'x':'c', 'y':'d', 'z':'e'}

print("Let's encrypt a message!")
#convert original sentence to lowercase
original_sentence = input("Please, enter a message you'd like to encrypt: ").lower()
#placeholder for new sentence
encrypted_sentence = ''

#identify first value pair as letter, tell it to correlate with other letter and add to new variable encrypted_sentence
for letter in original_sentence:
    if letter in cipher_alphabet:
        encrypted_sentence += cipher_alphabet.get(letter, letter)
        #create a case for things that aren't letters
    else:
        encrypted_sentence += letter

print("The encrypted sentence is:" , encrypted_sentence)
