from operator import truediv
import sqlite3

def check_details(username,password):
    connection_obj = sqlite3.connect('login.db')
    cursor_obj = connection_obj.cursor()

    # table = """ CREATE TABLE LoginDetails (
    #             Username VARCHAR(16) NOT NULL,
    #             Password CHAR(16) NOT NULL
    #         ); """

    # insert = """ INSERT INTO LoginDetails
    #             VALUES("shivang.negi", "12345678"   
    #             );"""

    statement = f'''SELECT * FROM LoginDetails WHERE Username="{username}" AND Password="{password}"'''
    cursor_obj.execute(statement)
    output = cursor_obj.fetchall()
    x = 0
    for row in output:
        x=1

    connection_obj.commit()
    connection_obj.close()

    if x==1:
        return 1
    else:
        return 0