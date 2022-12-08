import sqlite3

def DataUpdate(name):
    '''
    Pushes Descriptive Analytics Data to the Database
    '''
    db = sqlite3.connect('database.db')

    mycursor = db.connect()
    
    postgres_insert_query = """INSERT INTO Customer(name) VALUES (%s);""".format(name)
    
    mycursor.execute(postgres_insert_query)
    
    db.commit()

    print("Record inserted successfully into table")