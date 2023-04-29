import random
import string

def genrate_password(length):

    chars = string.ascii_letters+string.digits+string.punctuation
    password = " "
    for i in range(length):
        password+=random.choice(chars)

    return password

length = int(input("Enter the length of the Password "))
print("Generated Password: ",genrate_password(length))