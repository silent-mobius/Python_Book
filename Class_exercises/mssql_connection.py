import sqlite3

try:
	sqliteConnection = sqlite3.connect("Sqlite_py.db")
	curser = sqliteConnection.cursor()
	print("Database created and successfully connected via sqlite3")
	
	sqlite_select_query = 'select sqlite_version();'
	curser.execute(sqlite_select_query)
	record = curser.fetchall()
	print('sqlite database version is: ',record)
	curser.close()
	
except sqlite3.Error as err:
	print("error occured while conenction to sqlite: ", err)
