import random, string, pyperclip, datetime

passwrd_char = [string.ascii_letters,  string.digits, string.punctuation]

def password_generator(length, passwordtype):
    generated_password = ""
    
    for i in range(length+1):
        random_char = random.choice(passwordtype)
        generated_password += random_char
    return generated_password
    o


def length_settings(): 
    try :
        password_length = int(input("password length: "))
    except ValueError:
        print("Invalid input: please enter a number.")
        return length_settings()
    
    
    if 8 <= password_length <= 128 :
        print("Password length accepted.")
        return password_length
    
        
    if password_length > 128:
        print("Invalid length: Please enter a number up to 128.")
    elif password_length < 8:
        print("Invalid length: Passwords must be at least 8 characters long.")
    return length_settings()




def char_settings():
    print("Choose password type:\n1 = Letters only")
    print("1 = Letters only")
    print("2 = Letters + Digits")
    print("3 = Letters + Digits + Special characters")
    try :
        password_type = int(input(">>>>> "))
    except ValueError:
        print("Invalid input: please enter a number.")
        return char_settings()
    
    if password_type in (1, 2, 3):
        password_type = "".join(j for j in passwrd_char[0:password_type])
        return password_type
    else:
        print("Invalid input: please enter a number from 1 to 3")
        return char_settings()
    





new_password = password_generator(length_settings(), char_settings())
pyperclip.copy(new_password)
print("new password generated successfully:")
    
    




    