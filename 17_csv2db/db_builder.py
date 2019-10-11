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

def create_table_sql(cls, table_name, column_names):
    """Return string that can be used to create SQL data table
    The column_names should include the DATATYPE as part of the same string
    """
    command = 'CREATE TABLE ' + table_name
    for i in column_names:
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

def csv_to_table_sql(cls, csv_dict_reader):


# < < < INSERT YOUR POPULATE-THE-DB CODE HERE > > >
with open('students.csv') as studentsFile:
    with open('courses.csv') as coursesFile:
        studentsReader = csv.DictReader(studentsFile)
        coursesReader = csv.DictReader(coursesFile)
        #c.execute(create_table_sql('students
        for i in studentsReader:



command = ""          # test SQL stmt in sqlite3 shell, save as string
c.execute(command)    # run SQL statement

#==========================================================

db.commit() #save changes
db.close()  #close database


