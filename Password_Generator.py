import random

# A Function to shuffle all the characters of a string


def shuffle(string):

    templist = list(string)
    random.shuffle(templist)
    return ''.join(templist)

# Main program


uppercaseLetter1 = chr(random.randint(65, 90))  # Generate a random Uppercase letter
uppercaseLetter2 = chr(random.randint(65, 90))
lowercaseLetter1 = chr(random.randint(97, 122))  # Generate a random lowercase letter
lowercaseLetter2 = chr(random.randint(97, 122))
digit1 = chr(random.randint(48, 57))  # Generate a random number
digit2 = chr(random.randint(48, 57))
punctuationSign1 = chr(random.randint(32, 38))  # Generate a random sign
punctuationSign2 = chr(random.randint(32, 38))


# Generate Password using all the characters,in random order


password = uppercaseLetter1 + uppercaseLetter2 + lowercaseLetter1 + lowercaseLetter2 \
           + punctuationSign1 + punctuationSign2
password = shuffle(password)

# output


print(password)

