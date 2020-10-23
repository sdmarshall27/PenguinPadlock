import random
import string

def genRandomPassword():
    #get random number between 15-35
    passLength = random.randint(15, 35)
    #generate then return passord
    passwordChars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(passwordChars) for i in range(passLength))
    return password

