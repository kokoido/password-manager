import random, string, pyperclip, datetime, time, sqlite3

passwrd_char = [string.ascii_letters,  string.digits, string.punctuation]

with open("words.txt", "r") as file:
    data = file.read()
    words = data.split()



def validation_for_input(input_message):
    print(input_message)
    try:
        input_to_validate = int(input(">>>>>"))
        return input_to_validate
    except ValueError:
        print("Invalid Input: Please choose an option from the following")
        return validation_for_input(input_message)



def password_generator(length, passwordtype):
    generated_password = ""
    
    for i in range(length+1):
        random_char = random.choice(passwordtype)
        generated_password += random_char
    return generated_password



def passphrase_generator():
    generated_passphrase = ""
    
    for i in range(4):
        random_word = random.choice(words)
        generated_passphrase += random_word + "-"
    generated_passphrase = generated_passphrase[:-1]
    return generated_passphrase


def length_settings(): 
    message = "password length(8-128 character)"
    password_length = validation_for_input(message)
    
    if 8 <= password_length <= 128 :
        print("Password length accepted.")
        return password_length
    
        
    if password_length > 128:
        print("Invalid length: Please enter a number up to 128.")
    elif password_length < 8:
        print("Invalid length: Passwords must be at least 8 characters long.")
    return length_settings()




def char_settings():
    message = "Choose password type:\n1 = Letters only2\n = Letters + Digits\n3 = Letters + Digits + Special characters"
    password_type = validation_for_input(message)
    if password_type in (1, 2, 3):
        password_type = "".join(j for j in passwrd_char[0:password_type])
        return password_type
    else:
        print("Invalid input: please enter a number from 1 to 3")
        return char_settings()


def save_to_dbs(service_name, pass_word_phrase, datecreated, notes):
    
    try:
        connection =  sqlite3.connect("passwords.db")
        c = connection.cursor()
        
        
         c.execute('''
            CREATE  table if NOT EXISTS passwords (
              id Integer PRIMARY key AUTOINCREMENT,
              service_name Text NOT NULL,
              pass_word_phrase Text NOT NULL,
              date_created datetime NOT NULL,
              notes Text not NULL
            )
         ''')
     
     
         c.execute('''
            INSERT INTO passwords(service_name, pass_word_phrase, date_created, notes)
            VALUES(?, ?, ?, ?)
         ''', (service_name, pass_word_phrase, date_created, notes))
         connection.commit()
         connection.close()
     
         print(f"Password for '{service_name}' saved successfully!")
        
    
    except sqlite3.Error as error:
        print(error)

def main():
    message = (
    "How can I help you?\n"
    "1 - Generate a random password\n"
    "2 - Generate a passphrase\n"
    "3 - View saved passwords"
    )
    service_type = validation_for_input(message)
    if service_type in (1, 2, 3):
        if service_type == 3:
            with open("savedpasswords.txt", "a") as file:
                file.readall()
        elif service_type == 1:
            new_password =  password_generator(length_settings(), char_settings())
            return new_password
            
        else:
            new_passphrase = passphrase_generator()
            return new_passphrase
    else:
        print("Invalid Input: please choose from the given choices")
        main()
    
    
    
    
    


new_pass = main()

print(new_pass)
    
    




    