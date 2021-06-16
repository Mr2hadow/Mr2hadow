from random import choices
import random

data = [

    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",

    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z",

    '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
]

while 1:
    password_len = int(input("How long do you want the password to be? : "))
    password_count = int(input("How many passwords do you want? : "))
    for x in range(0,password_count):
        password = ""
        for x in range(0,password_len):
            password_data = random.choice(data)
            password      =password + password_data
        print("There is your password9 :", password)