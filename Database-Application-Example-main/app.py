''' Skyscraper Database Example '''
# imports
import sqlite3

# variables
DATABASE = 'skyscrapers.db'


# functions
def print_all_buildings():
    '''print all the aircraft nicely'''
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    sql = "SELECT * FROM building_list;"
    cursor.execute(sql)
    results = cursor.fetchall()
    # print out the heading
    print('Name                           Height(m)  City               Year Built')
    # loop through all the results
    for tower in results:
        print(f"{tower[1]:<30} {tower[2]:<10} {tower[3]:<18} {tower[4]}")
    # loop finish
    db.close()
# main code
print_all_buildings()