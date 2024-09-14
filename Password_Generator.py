import random
import string

def Add_Symbol(Password):
    symbol = string.punctuation
    for _ in range(random.randrange(1,3)):
        Password[random.randint(0,len(Password)-1)] = random.choice(symbol)
    return Password

def Add_Digits(Password):
    for _ in range(random.randrange(1, 4)):
        Password[random.randint(0,len(Password)-1)] = str(random.randrange(0,10))
    return Password

def Password_Generator(length):
    if length > 3:
        words = string.ascii_letters
        words = random.sample(words,len(words))
        Password = []
        for _ in range(length):
            Password.append(random.choice(words))
        Password = Add_Digits(Password)
        Password = Add_Symbol(Password)
        return ''.join(Password)
    else:
        print("Password Generate more the 3 symbol") 

print(Password_Generator(15))