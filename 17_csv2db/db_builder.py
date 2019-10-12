#Clyde "Thluffy" Sinclair
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='salmon.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================

def create_table_sql(cls, table_name, column_titles):
    """Return string that can be used to create SQL data table
    The column_titles should include the DATATYPE as part of the same string
    """
    command = 'CREATE TABLE ' + table_name
    for i in column_titles:
        command += i
    return command

def insert_into_sql(cls, table_name, column_vals):
    """Return string that can be used to add rows to SQL data table
    The column_vals should include the DATATYPE as part of the same string
    """
    command = 'INSERT INTO ' + table_name
    for i in column_vals:
        command += i
    return command

def get_sql_type(cls, var):
    """ Gets the type of the variable in python, and returns the respective SQL type """
    if type(var) is int or type(var) is float:
        return 'NUMERIC'
    if type(var) is str:
        return 'TEXT'

def get_sql_table_headers(cls, csv_dict_reader):
    """ This takes in a csv dictionary reader type, and returns a list of the headings needed to make a table """
    column_names = []
    for row in csv_dict_reader:
        for column in column_names:
            column_names.append('{} {}'.format(column, get_sql_type(row[column])))
        return column_names


def csv_to_table_sql(cls, table_name, csv_dict_reader):
    """Automatically converts a DictReader into a SQL data table"""
    cmd = ''
    column_names = []  # These are the key names
    for row in csv_dict_reader:
        column_names = row.keys()
        break
    column_names_with_datatype = get_sql_table_headers(csv_dict_reader)  # This is used to make the table headings as the datatype is required
    cmd += create_table_sql(table_name, column_names_with_datatype)


# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
with open('students.csv') as studentsFile:
    with open('courses.csv') as coursesFile:
        studentsReader = csv.DictReader(studentsFile)
        coursesReader = csv.DictReader(coursesFile)
        #c.execute(create_table_sql('students
        for i in studentsReader:
            print(i)
        for i in coursesReader:
            print(i)



command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


