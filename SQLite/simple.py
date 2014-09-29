#!/usr/bin/python3

## Simple SQLite database access

import sqlite3
import os
from TDDUtils import *

class Phonebook:
    def __init__(self,database='simple.db',keep=False):

        if keep:
            assert os.path.exists(database)  # TODO: Create database if does not exist when using keep=True
            self.con=sqlite3.connect(database)
            return
        self.new(database)

    def new(self,database):  
        if os.path.exists(database):
            os.unlink(database)
        self.con=sqlite3.connect(database)

        schema=open('simple.sql').read()
        #print(schema)
        cur=self.con.execute(schema)
        cur.close()

    def close(self):
        self.con.commit()
        self.con.close()

    def add(self,name,number):
        statement='INSERT INTO Data (key,value) VALUES (?,?)'
        cur=self.con.execute(statement,(name,number))
        cur.close()
        return True

    def get(self,name):
        statement='SELECT value FROM Data WHERE key=?'
        cur=self.con.execute(statement,(name,))
        data=cur.fetchone()
        if data is None:
            return None
        value=data[0]
        cur.close()
        return value

if __name__=='__main__':
    print("simple.py")
    assertTrue(True)

    db=Phonebook()
    assertTrue(db.add('Bob','5551212'))
    assertEquals('5551212',db.get('Bob'))
    assertEquals(None,db.get('Andy'))
    db.close()

    db=Phonebook(keep=True)
    assertEquals('5551212',db.get('Bob'))
    db.close()    
    
