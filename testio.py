import sqlite3

from datetime import da



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
         


