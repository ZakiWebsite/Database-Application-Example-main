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
while True:
    # strip whitespace so inputs like '1 ' or ' 1' still work
    user_input = input('What would you like to do?\n1. Print all buildings\n2. Print an ordered list by height\n3. Print an ordered list by year built\n4. Print all buildings considered "supertall" (300m+) \n5. Print all buildings considered "megatall" (600m+)\n6. Exit\n').strip()
    # ask the user which option they would like to print
    if user_input == '1':
        print_all_buildings()
    elif user_input == '2':
        pass
    elif user_input == '3':
        pass
    elif user_input == '4':
        pass
    elif user_input == '5':
        pass
    elif user_input == '6':
        break
    # print out what the user wants to display (placeholder for now)
    else:
        print('Invalid input, please try again.')
    # if input is invalid, tell the user.
