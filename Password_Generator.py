#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password = ""

print("Welcome to the PyPassword Generator!")

#letter part of the password
nr_letters= int(input("How many letters would you like in your password?\n")) 
for char in range(0, nr_letters):
  password += random.choice(letters)

#symbol part of the password
nr_symbols = int(input(f"How many symbols would you like?\n"))
for char in range(0, nr_symbols):
  password += random.choice(symbols)


#number part of the password
nr_numbers = int(input(f"How many numbers would you like?\n"))
for char in range(0, nr_numbers):
  password += random.choice(numbers)

#Shuffling the passwoord string to form a strong password
l = list(password)
random.shuffle(l)
result = ''.join(l)
print(result)