#TODO Date needs to be localdate

import sys
import sqlite3
import os
from time import sleep
from datetime import date
appPath = os.path.dirname(os.path.abspath( __file__ ))
dbPath = os.path.join(appPath, 'notes.db')
#Menu
#Check for DB
def dbCheck():
    if os.path.isfile(dbPath) == False:
        dbChoice = input("Database notes.db was not found, would you like to create a new Database? [Y],[N]").lower()
        if dbChoice == 'y':
            dbCreate()
        elif dbChoice == 'n':
            exit(0)
    elif os.path.isfile(dbPath) == True:
        #print("Database was found...")
        return 

def dbCreate():
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()  
    c.execute('''CREATE TABLE todo
    (todo_id INTEGER PRIMARY KEY, todo_description varchar(250) NOT NULL, Timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)''')
    conn.commit()
    conn.close()


def showNote():
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()  
    c.execute('SELECT todo_id, todo_description, Timestamp  FROM todo ')
    result = c.fetchall()
    print( "\n \n".join( repr(e) for e in result ))
    input("\nPress [Enter] to go back to the menu")
    main()

#Take an input, Save that input to a list
def createNote():
    conn = sqlite3.connect(dbPath)
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
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()  
    c.execute('SELECT todo_id, todo_description, Timestamp  FROM todo ')
    result = c.fetchall()
    print( "\n \n".join( repr(e) for e in result ))
    idDel = input("\nEnter task ID to delete, or press [Enter] to quit back to menu: ")
    try:
        c.execute(f"DELETE FROM todo WHERE todo_id={idDel}")
    except sqlite3.OperationalError:
        main()
    conn.commit()
    conn.close()
    main()

def main():
    dbCheck()
    os.system('clear')
    conn = sqlite3.connect(dbPath)
    c = conn.cursor()  
    c.execute('SELECT todo_id, todo_description FROM todo ORDER BY Timestamp DESC ')
    result = c.fetchall()
    #resultFinal = [i for i in result]
    print("""
  _______        _         _             _______    _____        
 |__   __|      | |       | |           |__   __|  |  __ \       
    | | ___  ___| |__   __| | _____  __    | | ___ | |  | | ___  
    | |/ _ \/ __| '_ \ / _` |/ _ \ \/ /    | |/ _ \| |  | |/ _ \ 
    | |  __| (__| | | | (_| | (_) >  <     | | (_) | |__| | (_) |
    |_|\___|\___|_| |_|\__,_|\___/_/\_\    |_|\___/|_____/ \___/ 
                             version 1.0.2           
                                                                 
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