#Winston Peng
#SoftDev
#skeleton :: SQLITE3 BASICS
#Oct 2019

import sqlite3   #enable control of an sqlite database
import csv       #facilitate CSV I/O


DB_FILE='salmon.db'

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================


def create_table_sql(table_name, column_titles):
    """Return string that can be used to create SQL data table
    The column_titles should include the DATATYPE as part of the same string
    """
    command = 'CREATE TABLE ' + table_name + ' ('
    print(column_titles)
    for i in column_titles[:-1]:
        command += i + ', '
    command += column_titles[-1]
    return command + ');\n'


def insert_into_sql(table_name, column_vals):
    """Return string that can be used to add rows to SQL data table
    The column_vals should include the DATATYPE as part of the same string
    """
    command = 'INSERT INTO ' + table_name + ' VALUES ('
    for i in column_vals[:-1]:
        command += i + ', '
    command += column_vals[-1]
    return command + ');\n'


def get_sql_type(var):
    """ Gets the type of the variable in python, and returns the respective SQL type """
    try:
        float(var)
        return 'NUMERIC'
    except:
        return 'TEXT'


def get_sql_table_headers(csv_dict_reader):
    """ This takes in a csv dictionary reader type, and returns a list of the headings needed to make a table """
    column_names = []
    for row in csv_dict_reader:
        for column in row:
            column_names.append('{} {} '.format(column, get_sql_type(row[column])))
        return column_names


def csv_to_table_sql(table_name, csv_dict_reader):
    """Automatically converts a DictReader into a SQL data table"""
    cmd = ''
    column_names = []  # These are the key names
    for row in csv_dict_reader:
        column_names = row.keys()
        break
    # This is used to make the table headings as the datatype is required
    column_names_with_datatype = get_sql_table_headers(csv_dict_reader)
    cmd += create_table_sql(table_name, column_names_with_datatype)
    # This iterates through the dict_reader and adds the values
    for row in csv_dict_reader:
        column_vals = []
        for col in column_names:
            # This puts quotes around it if the value is a word
            column_vals.append(row[col] if get_sql_type(row[col]) == 'NUMERIC' else '"{}"'.format(row[col]))
        cmd += insert_into_sql(table_name, column_vals)
    return cmd


with open('students.csv') as studentsFile:
    with open('courses.csv') as coursesFile:
        studentsReader = csv.DictReader(studentsFile)
        coursesReader = csv.DictReader(coursesFile)
        # print(csv_to_table_sql('students', studentsReader))
        students_command_list = csv_to_table_sql('students', studentsReader).split('\n')[:-1]
        print(students_command_list)
        for i in students_command_list:
            c.execute(i)
        # c.execute(csv_to_table_sql('students', studentsReader))
        # c.execute(csv_to_table_sql('courses', coursesReader))

#==========================================================

db.commit() #save changes
db.close()  #close database


