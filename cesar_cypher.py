#ASCII value--
#A-Z-- 65-90
#a-z-- 97-122
#0-1-- 48 to 57
alphabet = []
number = []
for ascii_value in range(97,123):
    alphabet.append(chr(ascii_value))
print(alphabet)
#print(alphabet.index('-'))
for ascii_value in range(48,58):
    number.append(chr(ascii_value))
print(number)
#declarer variables
cipher_text = ""
key = ""

#taking inputs
choice = input("encrypt/decrypt: \n")

if (choice != "encrypt") and (choice != "decrypt"):
    print("invalid choice")
else:
    #taking inputs
    word = input("enter message: \n")
    shift = input("enter shift: \n")
    direction = input("right/ left shift: \n")

    if direction == "right":
        key = "+" + shift
    elif direction == "left":
        key = "-" + shift
    else:
        print("invalid choice")
    key = int(key) 
    #processing input
    def ciser_code(key, alphabet, cipher_text, letter, choice):
        word_index = alphabet.index(letter)
        if choice.lower()=="encrypt":
            new_index = encrypt(key, word_index)
        elif choice.lower()=="decrypt":
            new_index = decrypt(key, word_index)
        else:
            print("invalid choice")
        cipher_text += alphabet[new_index]
        return cipher_text

    def decrypt(key, word_index):
        if (len(alphabet)-word_index)<key:
            return word_index-key
        else:
            key = word_index-key
            return key%len(alphabet)

    def encrypt(key, word_index):
        if (len(alphabet)-word_index)>key:
            return word_index+key
        else:
            key = word_index+key
            return key%len(alphabet)

    for letter in word:
        if letter != " " and letter in alphabet:
            cipher_text = ciser_code(key, alphabet, cipher_text, letter, choice)
        # elif letter in number:
        #     cipher_text += ciser_code(key, number, cipher_text, letter, choice)
        else:
            cipher_text+= letter

    print(f"your {choice}ed message with {direction} shifted: {cipher_text}")