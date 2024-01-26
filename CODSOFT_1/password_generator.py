# Password Generator Project

# Import the random module for random choices
import random

# Define character sets
letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
    'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Print a welcome message
print("Welcome to the PyPassword Generator!")

# Get user input for password criteria
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize empty lists for characters, symbols, and numbers
charac = []
symbl = []
num = []

# Generate random letters based on user input
for Pass in range(1, nr_letters + 1):
    random_letter = random.choice(letters)
    charac += random_letter

# Generate random symbols based on user input
for Pass in range(1, nr_symbols + 1):
    random_symbol = random.choice(symbols)
    symbl += random_symbol

# Generate random numbers based on user input
for Pass in range(1, nr_numbers + 1):
    random_number = random.choice(numbers)
    num += random_number

# Combine characters, symbols, and numbers
password = charac + symbl + num

# Shuffle the combined characters to create a random password
random.shuffle(password)

# Convert the list of characters to a string
passworddc = ""
for pchar in password:
    passworddc += pchar

# Print the generated password
print(f"Your Password is:-  {passworddc}")
