
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#unhashthese
print("Welcome to the Password Generator! This tool will help you create a unique password. Remember, a great password has at least 8 characters, and has a mix of numbers, letters, and symbols. ")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

letters_new=random.sample(letters, nr_letters)
symbols_new=random.sample(symbols, nr_symbols)
numbers_new=random.sample(numbers, nr_numbers)

password_old=(letters_new+ numbers_new+symbols_new)
password=(''.join(random.sample(password_old,len(password_old))))

print(f"\nYour new password is  -> {password}. Be safe!")
