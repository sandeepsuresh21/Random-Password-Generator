from random import randint, choice, shuffle

characters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
			  'W', 'X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q', 'R',
			  'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n',
			  'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
			  'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

symbols = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

length = int(input("Enter the length of the Password: "))

char_length = int(input("Enter the length of characters in the password: "))

dig_length = int(input("Enter the length of digits in the password: "))

symb_length = int(input("Enter the length of special symbols in the password: "))

random_chars = []

for i in range(char_length):
	random_chars.append(choice(characters))

random_digits = []

for i in range(dig_length):
	random_digits.append(choice(digits))

random_symbols = []
shuffled_password = []

for i in range(symb_length):
	random_symbols.append(choice(symbols))

joined_password = random_chars + random_digits + random_symbols

shuffle(joined_password)

password = ""
password = password.join(joined_password)

print(password)

shift = int(input("Enter the shift value: "))

print(characters.index(random_chars[0]))

encrypted_pass = ""

for letter in password:
	if letter.isalpha():
		index = characters.index(letter)
		encrypted_pass += characters[index + shift]
	else:
		encrypted_pass += letter

print("The Encrypted Password Is :", encrypted_pass)

decrypted_pass = ""

for let in encrypted_pass:
	if let.isalpha():
		index_1 = characters.index(let)
		decrypted_pass += characters[index_1 - shift]
	else:
		decrypted_pass += let

print("The Decrypted Password Is :", decrypted_pass)
