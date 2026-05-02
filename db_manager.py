import sqlite3

with open("praktikum_script_database.sql", 'r', encoding = 'utf-8') as sqldb:
    db_script = sqldb.read()

connection = sqlite3.connect('app_db.db')
connection.execute("PRAGMA foreign_keys = ON;")
cursor = connection.cursor()
cursor.executescript(db_script)
connection.commit()
#cursor.execute("INSERT INTO users(id, username, password) values (1, 'Danila', 'qwerty' ) ")
#connection.commit()
#connection.close()

def users_add( name, password): 
    connection = sqlite3.connect('app_db.db')
    connection.execute("PRAGMA foreign_keys = ON;")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO users(username, password) values ( ? , ?)', (name, password))
    connection.commit()
    connection.close()
    return

def expenses_add(user_id, amount, category, date, description=""):
    connection = sqlite3.connect('app_db.db')
    connection.execute("PRAGMA foreign_keys = ON;")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO expenses(user_id, amount, category, date, description) values (?,?,?,?,?)', (user_id, amount, category, date, description))
    connection.commit()
    connection.close()
    return


def expenses_get_all(user_id):
    connection = sqlite3.connect('app_db.db')
    connection.execute("PRAGMA foreign_keys = ON;")
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM expenses WHERE user_id = ?', (user_id,))
    records = cursor.fetchall()    
    connection.close()
    return records

def expenses_update(expense_id, new_amount, new_category, new_date, new_description):
    connection = sqlite3.connect('app_db.db')
    connection.execute("PRAGMA foreign_keys = ON;")
    cursor = connection.cursor()
    cursor.execute('''
        UPDATE expenses 
        SET amount = ?, category = ?, date = ?, description = ? 
        WHERE id = ?
    ''', (new_amount, new_category, new_date, new_description, expense_id))  
    connection.commit()
    connection.close()

def expenses_delete(expense_id):
    connection = sqlite3.connect('app_db.db')
    connection.execute("PRAGMA foreign_keys = ON;")
    cursor = connection.cursor()
    cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    connection.commit()
    connection.close()

#expenses_add(1, 22, "beer", "02.05.2009", "grandfather bought me beer")
#expenses_delete(1)