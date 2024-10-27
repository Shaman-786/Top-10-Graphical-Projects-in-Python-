import random

# A function to shuffle all the characters of a string
def shuffle(string):
    tempList = list(string)
    random.shuffle(tempList)
    return ''.join(tempList)

# Main program starts here
# Generate 3 random Uppercase letters
uppercaseLetters = [chr(random.randint(65, 90)) for _ in range(3)]

# Generate 3 random Lowercase letters
lowercaseLetters = [chr(random.randint(97, 122)) for _ in range(3)]

# Generate 1 random digit
digit = str(random.randint(0, 9))

# Generate 1 '#' symbol
symbol = '#'

# Combine all parts for the password
all_characters = uppercaseLetters + lowercaseLetters + [digit] + [symbol]

# Shuffle to create a random order
password = shuffle(''.join(all_characters))

# Ensure the password is exactly 8 characters long
password = password[:8]

# Output
print(password)
