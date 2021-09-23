class Caesar:
    def __init__(self, key, lowest = 32, highest = 127):
       self.key = key 
       self.modulus = highest - lowest
       self.lowest = lowest
       # there are 128 characters in ascii
       # 127 happens to be the delete character
       # printable characters go from 32 to 126
       self.keynumber = ord(key) - ord("a")
    def encrypt(self, message): 
        new_message = [] 
        # take each letter in the message
        for letter in message:
            # convert the letter to a number
            number = (ord(letter))
            # add the number that our key has to the first number
            new_number = (number + self.keynumber - self.lowest) % self.modulus + self.lowest
            # convert back to letters
            new_letter = chr(new_number)
            new_message.append(new_letter)
        return "".join(new_message)
    def decrypt(self, ciphertext):
        # print("ciphertext:", ciphertext)
        # take each letter in the ciphertext
        message = []
        for letter in ciphertext:
            # print("letter:", letter)
            # convert the letter to a number
            cipher_number = (ord(letter))
            # ord uses the order of characters in unicode (which share the first 128 characters with ascii)
            # print("cipher number:", cipher_number)
            # subtract the keynumber 
            message_number = (cipher_number - self.lowest - self.keynumber) % self.modulus + self.lowest
            # print("message number:", message_number)
            # convert back to letters
            message_letter = chr(message_number)
            # print("message letter:", message_letter)
            message.append(message_letter)
        return "".join(message)

# alice = Caeser("q")
# alice.encrypt("Hello eliza")
# bob = Caesar("x")
# bob_ciphertext = bob.encrypt("Hello eliza. How are you today?")
# print("bob ciphertext:", bob_ciphertext)
# print(bob.decrypt(bob_ciphertext))
# print(bob.keynumber)

# for printable_character_number in range(32, 127):
#     printable_character = chr(printable_character_number)
#     print("printable_character:", printable_character)
#     caesar = Caesar(printable_character)
#     print(caesar.decrypt(bob_ciphertext))

# ciphertext = "TRVJRITZGYVIJRIVHLZKVVRJPKFTIRTB"
# for printable_character_number in range(65, 91):
#     printable_character = chr(printable_character_number)
#     print("printable_character:", printable_character)
#     caesar = Caesar(printable_character, 65, 90)
#     print(caesar.decrypt(ciphertext)) 

# for printable_character_number in range(32, 127):
#     printable_character = chr(printable_character_number)
#     print("printable_character:", printable_character)
#     caesar = Caesar(printable_character)
#     print(caesar.decrypt(bob_ciphertext))