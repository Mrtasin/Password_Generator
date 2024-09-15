def Encryption(Data_Item, Key, keyDigit = 0):
    if keyDigit == 0:
        keyDigit = Key
    Encrypt_Data = ''
    for _ in Data_Item:
        if _ >= 'A' and _ <= 'Z':
            Encrypt_Data += chr(65 + (ord(_) - 65 + Key) % 26)
        elif _ >= 'a' and _ <= 'z':
            Encrypt_Data += chr(97 + (ord(_) - 97 + Key) % 26)
        elif _ >= '0' and _ <= '9':
            Encrypt_Data += chr(48 + (ord(_) - 48 + keyDigit) % 10)
        else:
            Encrypt_Data += _
    
    return Encrypt_Data

def Decryption(Data_Item,Key):
    return Encryption(Data_Item,26-Key,10 - Key)

data = Encryption("Tasin@786",8)
print(data)
print(Decryption(data,8))