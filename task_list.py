#!/usr/bin/env python
# coding: utf-8

"""
    Title: Task list manager
    Author: Radoslaw Binek
"""

import sqlite3



# Creating database
def create_db():
    '''
    This function create new database of tasks (id, name, deadline, description).
    '''
        
    con = sqlite3.connect('task.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute("DROP TABLE IF EXISTS task;")

    cur.execute("""
        CREATE TABLE IF NOT EXISTS task (
            task_id INTEGER PRIMARY KEY ASC,
            name varchar(250) NOT NULL,
            deadline varchar(250) NOT NULL,
            description varchar(250) NOT NULL
        )""")
    print("The database was created successfully")

# Add task to database
def add(name, deadline, description):
    '''
    This function add new task to the db. Please insert name, deadline and description.
    '''
    
    con = sqlite3.connect('task.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute('INSERT INTO task VALUES(NULL, ?, ?, ?);', (name, deadline, description))
    con.commit()


# List all elements
def list():
    '''
    This function list all elements from db.
    '''
    
    con = sqlite3.connect('task.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute(
        """
        SELECT task.task_id,name,deadline,description FROM task
        """)
    
    tasks = cur.fetchall()
    
    for task in tasks:
        r_id = task['task_id']
        r_task = task['name']
        r_deadl = task['deadline']
        r_desc = task['description']
        print(f'Id: {r_id}, Name: {r_task}, Deadline: {r_deadl}, Description: {r_desc}')


# Remove task from db
def remove(task_id):
    '''
    This function remove task by id. Please insert id number.
    '''
    
    con = sqlite3.connect('task.db')
    con.row_factory = sqlite3.Row
    
    sql = 'DELETE FROM task WHERE task_id=?'
    cur = con.cursor()
    cur.execute(sql, (task_id,))
    con.commit()


# Remove task by hash value of task name
def remove_hash(name_hash):
    '''
    This function remove task by hash value of name (hash(name) function). Please insert name hash value.
    '''
    
    id_list = []
    name_list = []
    
    
    con = sqlite3.connect('task.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    cur.execute(
        """
        SELECT task.task_id,name,deadline,description FROM task
        """)
    
    tasks = cur.fetchall()
    
    for task in tasks:
        r_id = task['task_id']
        r_task = task['name']
        r_deadl = task['deadline']
        r_desc = task['description']
        
        id_list.append(r_id)
        name_list.append(r_task)
        
    for n in name_list:
        print(hash(n))
        if hash(n) == name_hash:
            sql = 'DELETE FROM task WHERE name=?'
            cur = con.cursor()
            cur.execute(sql, (n,))
            con.commit()


# Update task in db
def update(task_id, name, deadline, description):
    '''
    This function update task in db. Please insert id number and new name, deadline, description.
    '''
    
    con = sqlite3.connect('task.db')
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    
    sql = ''' UPDATE task
            SET name = ? ,
                deadline = ? ,
                description = ?
            WHERE task_id = ?'''

    data = (name, deadline, description, task_id)
    cur.execute(sql, data)
    con.commit()






