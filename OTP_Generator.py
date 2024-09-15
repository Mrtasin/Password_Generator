import random
import string

def Generate_Digit_OTP(length):
    digit = string.digits
    digit = random.sample(digit, len(digit))
    otp = ''
    for _ in range(length):
        otp += random.choice(digit)
    return otp


def Generate_OTP_With_Character(length):
    char = string.ascii_letters + string.digits
    char = random.sample(char, len(char))
    OTP = ''
    for _ in range(length):
        OTP += char[random.randint(0, len(char) - 1)]

    return OTP

print(Generate_OTP_With_Character(8))