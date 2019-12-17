import sys
import sqlite3
import os

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


def main():
    dbCheck()
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    c.execute('SELECT todo_id, todo_description FROM todo ')
    result = c.fetchall()
    #resultFinal = [i for i in result]
    print( ", ".join( repr(e) for e in result ) )
    print("""
    1. Take a note
    2. Delete a note
    3. Exit
    """)
    choice = input("")
    if choice == '1':
        createNote()
    elif choice == '2':
        deleteNote()
    elif choice == '3':
        return
    exit(0)
      
#Take an input, Save that input to a list
def createNote():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    newNote = input("Enter your ToDo: ")
    c.execute(f'INSERT INTO todo (todo_description) values ("{newNote}")')
    conn.commit()
    conn.close()
    main()

#Delete note
def deleteNote():
    conn = sqlite3.connect('notes.db')
    c = conn.cursor()  
    idDel = input("Enter task ID to delete")
    c.execute(f"DELETE FROM todo WHERE todo_id={idDel}")
    conn.commit()
    conn.close()
    main()
#show the list
main()