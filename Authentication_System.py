import string
import random
def Read_File(file_name):
    try:
        with open(file_name,'r') as file :
            return file.read()
    except FileNotFoundError:
        return "File not Found"

def Write_File(file_name, Data):
    with open(file_name,'w') as file :
        file.write(Data)
        
def Login():
    u_name = input("Enter the User Name : ")
    Pass = Read_File(u_name)
    if Pass != 'File not Found':
        u_pass = input("Enter the User Password : ")
        if u_pass == Pass:
            print("|------------------|")
            print("| Login Successful |")
            print("|------------------|")
            print()
        else:
            print("Password is invalid")
    else:
        print("User Name is invalid")

def New_Registration():
    FirstName = input("Enter the First Name : ")
    LastName = input("Enter the Last Name : ")
    Age = int(input("Enter the Age : "))
    MobNo = int(input("Enter the Phone Number : "))
    u_pass = input("Enter the User Password : ")
    symbol = string.punctuation
    symbol = random.choice(symbol)
    u_name = FirstName.lower() + LastName.lower() + symbol + str(Age) + str(MobNo%100)
    Write_File(u_name,u_pass)
    print("User Name is : {}".format(u_name))
    print("Password  is : {}".format(u_pass))


while True:
    print("Enter 1 For Login")
    print("Enter 2 For New Registration")
    print("Enter 3 For Exit")
    choice = int(input("Enter a choice : "))
    match(choice):
        case 1:
            Login()
        case 2:
            New_Registration()
        case 3:
            print("Thank you...!")
            break 
        case _:
            print("Enter valid choice...!")