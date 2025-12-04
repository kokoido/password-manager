import random, string, pyperclip, datetime, time, os, sqlite3
import pandas as pd

# List of character types for password generation
PASSWORD_CHAR = [string.ascii_letters, string.digits, string.punctuation]

# Load words for passphrase generation from a local file
with open("words.txt", "r") as file:
    data = file.read()
    words = data.split()


# Validate user input to ensure it's an integer
def validation_for_input(input_message):
    print(input_message)
    try:
        input_to_validate = int(input(">>>>>"))
        return input_to_validate
    except ValueError:
        print("Invalid Input: Please choose an option from the following")
        return validation_for_input(input_message)


# Generate a random password given length and character set
def password_generator(length, passwordtype):
    generated_password = ""
    for i in range(length):
        random_char = random.choice(passwordtype)
        generated_password += random_char
    return generated_password


# Generate a passphrase using 4 random words
def passphrase_generator():
    generated_passphrase = ""
    for i in range(4):
        random_word = random.choice(words)
        generated_passphrase += random_word + "-"
    generated_passphrase = generated_passphrase[:-1]  # remove last dash
    return generated_passphrase


# Ask user for password length and validate it
def length_settings():
    message = "password length(8-128 character)"
    password_length = validation_for_input(message)

    if 8 <= password_length <= 128:
        print("Password length accepted.")
        return password_length

    if password_length > 128:
        print("Invalid length: Please enter a number up to 128.")
    elif password_length < 8:
        print("Invalid length: Passwords must be at least 8 characters long.")
    return length_settings()


# Ask user which character types to include
def char_settings():
    message = (
        "Choose password type:\n"
        "1 = Letters only\n"
        "2 = Letters + Digits\n"
        "3 = Letters + Digits + Special characters"
    )
    password_type = validation_for_input(message)
    if password_type in (1, 2, 3):
        password_type = "".join(j for j in PASSWORD_CHAR[0:password_type])
        return password_type
    else:
        print("Invalid input: please enter a number from 1 to 3")
        return char_settings()


# Handle saving to or viewing the database
def manage_password_dbs(
    operation, service_name=None, pass_word_phrase=None, date_created=None, notes=None
):

    try:
        connection = sqlite3.connect("passwords.db")
        c = connection.cursor()

        # Create table if it doesn't exist
        c.execute(
            """
            CREATE  table if NOT EXISTS passwords (
              id Integer PRIMARY key AUTOINCREMENT,
              service_name Text NOT NULL,
              pass_word_phrase Text NOT NULL,
              date_created datetime NOT NULL,
              notes Text not NULL
            )
            """
        )

        if operation == "save":
            # Insert password/passphrase into DB
            c.execute(
                """
                INSERT INTO passwords(service_name, pass_word_phrase, date_created, notes)
                VALUES(?, ?, ?, ?)
                """,
                (service_name, pass_word_phrase, date_created, notes),
            )
            connection.commit()
            connection.close()
            print(f"Password for '{service_name}' saved successfully!")
            return

        elif operation == "view":
            # Fetch all saved passwords
            c.execute(
                """
                SELECT * FROM passwords
                """
            )
            rows = c.fetchall()
            df = pd.DataFrame(
                rows,
                columns=[
                    "id",
                    "service name",
                    "Password/passphrase",
                    "date created",
                    "notes",
                ],
            )
            connection.close()
            return df
        else:
            print("Invalid operation!")
            connection.close()
            return
    except sqlite3.Error as error:
        print(error)


# Main program loop
def main():
    TITLE = r"""
                                                                                        
  ___                              _   __  __                             
 | _ \__ _ _______ __ _____ _ _ __| | |  \/  |__ _ _ _  __ _ __ _ ___ _ _ 
 |  _/ _` (_-<_-< V  V / _ \ '_/ _` | | |\/| / _` | ' \/ _` / _` / -_) '_|
 |_| \__,_/__/__/\_/\_/\___/_| \__,_| |_|  |_\__,_|_||_\__,_\__, \___|_|  
                                                            |___/  by sandman
       
       -------------------------------------------------------------
        Look, we both know you're using the same password everywhere
                    No judgment—but let's change that!
        -------------------------------------------------------------
            """
    while True:
        os.system("cls" if os.name == "nt" else "clear")  # clear console
        print(TITLE)
        message = (
            "How can I help you?\n"
            "1 - Generate a random password\n"
            "2 - Generate a passphrase\n"
            "3 - View saved passwords\n"
            "4 - Exit the program"
        )
        service_type = validation_for_input(message)

        if service_type in (1, 2, 3, 4):
            if service_type == 3:
                # Display saved passwords
                df = manage_password_dbs("view")
                print(df)
                input("\nPress Enter to return to menu...")
            elif service_type == 1:
                # Generate a new password
                new_password = password_generator(length_settings(), char_settings())
                print("password generated successfully!")
                time.sleep(2)
                print(
                    f"your new password '{new_password}'\nhas been copied to your clipboard"
                )
                pyperclip.copy(new_password)
                print("lets save it to the DBS")
                manage_password_dbs(
                    "save",
                    input("service name: "),
                    new_password,
                    datetime.date.today(),
                    input("notes: "),
                )
                input("\nPress Enter to return to menu...")

            elif service_type == 2:
                # Generate a new passphrase
                new_passphrase = passphrase_generator()
                print("passphrase generated successfully!")
                print(
                    f"your new passphrase '{new_passphrase}' \nhas been copied to your clipboard"
                )
                time.sleep(2)
                pyperclip.copy(new_passphrase)
                print("lets save it to the DBS")
                manage_password_dbs(
                    "save",
                    input("service name: "),
                    new_passphrase,
                    datetime.date.today(),
                    input("notes: "),
                )
                input("\nPress Enter to return to menu...")
            else:
                # Exit countdown
                for i in range(-5):
                    print(f"program will close in {i}")
                    time.sleep(1)
                print("Goodbye!")
                break
        else:
            print("Invalid Input: please choose from the given choices")


if __name__ == "__main__":
    main()  # start the program
