morse_dict = {'A': '.-',
              'B': '-...',
              'C': '-.-.',
              'D': '-..',
              'E': '.',
              'F': '..-.',
              'G': '--.',
              'H': '....',
              'I': '..',
              'J': '.---',
              'K': '-.-',
              'L': '.-..',
              'M': '--',
              'N': '-.',
              'O': '---',
              'P': '.--.',
              'Q': '--.-',
              'R': '.-.',
              'S': '...',
              'T': '-',
              'U': '..-',
              'V': '...-',
              'W': '.--',
              'X': '-..-',
              'Y': '-.--',
              'Z': '--..',
              '1': '.----',
              '2': '..---',
              '3': '...--',
              '4': '....-',
              '5': '.....',
              '6': '-....',
              '7': '--...',
              '8': '---..',
              '9': '----.',
              '0': '-----',
              ', ': '--..--',
              '.': '.-.-.-',
              '?': '..--..',
              '/': '-..-.',
              '-': '-....-',
              '(': '-.--.',
              ')': '-.--.-'}


# def encrypt(message):
#     cipher = ' '
#     for letter in message:
#         if letter != ' ':
#             cipher += morse_dict[letter] + ' '
#         else:
#             cipher += ' '
#     return cipher
#
#
# def decrypt(en_message):
#     en_message += ' '
#     decipher = ' '
#     citext = ' '
#
#     for letter in en_message:
#         if letter != ' ':
#             i = 0
#             citext += letter
#         else:
#             i += 1
#             if i == 2:
#                 decipher += ' '
#             else:
#                 decipher += list(morse_dict.keys())[list(morse_dict.values()).index(citext)]
#                 citext = ' '
#
#     return decipher
#
#
# def main():
#     operation = input(f'Would you like to (1) encrypt or (2) decrypt a message?')
#     if operation == '1':
#         message = input(f'What would you like encrypted? ')
#         decryption = encrypt(message.upper())
#         print(decryption)
#     if operation == '2':
#         en_message = input(f'What would you like to decrypt? ')
#         decryption = decrypt(en_message)
#         print(decryption)
#
#
# if __name__ == '__main__':
#     main()

user_input = input('Welcome to the Morse Code Encoder.\nPlease enter your text:\n')

encoded = ''
for char in user_input:
    if char.upper() in morse_dict:
        encoded += f'{morse_dict[char.upper()]} '


print(encoded)
