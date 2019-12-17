import sys
import sqlite3
import os
from time import sleep

#Menu
#Check for DB
def dbCheck():
    if os.path.isfile('notes.db') == False:
        dbChoice = input("Database notes.db was not found, would you like to create a new Database? [Y],[N]").lower()
        if dbChoice == 'y':
            dbCreate()
        elif dbChoice == 'n':
            exit(0)
    elif os.path.isfile('notes.db') == True:
        #print("Database was found...")
        return 

def dbCreate():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    c.execute('''CREATE TABLE todo
    (todo_id INTEGER PRIMARY KEY, todo_description varchar(250) NOT NULL)''')
    conn.commit()
    conn.close()


def showNote():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    c.execute('SELECT todo_id, todo_description FROM todo ')
    result = c.fetchall()
    print( "\n".join( repr(e) for e in result ) )
    input("Press [Enter] to go back to the menu")
    main()

#Take an input, Save that input to a list
def createNote():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    newNote = input("Enter your Note: ")
    print(f'Added {newNote} to Database')
    sleep(1)
    c.execute(f'INSERT INTO todo (todo_description) values ("{newNote}")')
    conn.commit()
    conn.close()
    main()

#Delete note
def deleteNote():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    idDel = input("Enter task ID to delete")

    try:
        c.execute(f"DELETE FROM todo WHERE todo_id={idDel}")
    except sqlite3.OperationalError:
        input("Whoops, something went wrong. Press [Enter] to return to the menu")
        main()
    conn.commit()
    conn.close()
    main()

def main():
    dbCheck()
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    c.execute('SELECT todo_id, todo_description FROM todo ')
    result = c.fetchall()
    #resultFinal = [i for i in result]
    print("""
  _______        _         _             _______    _____        
 |__   __|      | |       | |           |__   __|  |  __ \       
    | | ___  ___| |__   __| | _____  __    | | ___ | |  | | ___  
    | |/ _ \/ __| '_ \ / _` |/ _ \ \/ /    | |/ _ \| |  | |/ _ \ 
    | |  __| (__| | | | (_| | (_) >  <     | | (_) | |__| | (_) |
    |_|\___|\___|_| |_|\__,_|\___/_/\_\    |_|\___/|_____/ \___/ 
                                                                 
                                                                 
                            1. Take a note
                            2. Delete a note
                            3. Show Notes
                            4. Exit
    """)
    choice = input("")
    if choice == '1':
        createNote()
    elif choice == '2':
        deleteNote()
    elif choice == '3':
        showNote()
    elif choice == '4':
        exit(0)
    else:
        main()
    

#show the list
if __name__ == "__main__":
    main()