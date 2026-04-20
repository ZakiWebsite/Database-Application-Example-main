''' Skyscraper Database Example '''
# imports
import sqlite3

# variables
DATABASE = 'skyscrapers.db'

# functions

# main code

db = sqlite3.connect(DATABASE)
cursor = db.cursor()
sql = "SELECT * FROM building_list;"
cursor.execute(sql)
results = cursor.fetchall()
print(results)
db.close()