class Encryp:
    def __init__(self, text):
        self.text = text
        self.encrypted_text = ''
        self.decrypted_text = ''
        self.dictionary = []
        for letter in range(ord('A'), ord('Z') + 1):
            self.dictionary.append(chr(letter))

    def Encrypt(self):
        for char in self.text:
            if char.isalpha():
                char = char.upper()
                if char in self.dictionary:
                    index = self.dictionary.index(char)
                    encrypted_index = (index + 3) % 26
                    print(index)
                    print(encrypted_index)
                    self.encrypted_text += self.dictionary[encrypted_index]
                else:
                    self.encrypted_text += char
            else:
                self.encrypted_text += char
        print("Encrypted:", self.encrypted_text)

    def Decrypt(self):
        for char in self.encrypted_text:
            if char.isalpha():
                char = char.upper()
                if char in self.dictionary:
                    index = self.dictionary.index(char)
                    decrypted_index = (index - 3) % 26  # Decrypt by shifting 3 positions to the left
                    self.decrypted_text += self.dictionary[decrypted_index]
                else:
                    self.decrypted_text += char
            else:
                self.decrypted_text += char
        print("Decrypted:", self.decrypted_text)

encrypt = Encryp('Farooq')
encrypt.Encrypt()
encrypt.Decrypt()
