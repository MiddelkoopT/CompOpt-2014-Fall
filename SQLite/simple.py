#!/usr/bin/python3

## Simple SQLite database access

import sqlite3
import os
from TDDUtils import *

class Data:
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
        cur=self.con.executescript(schema)
        cur.close()

    def close(self):
        self.con.commit()
        self.con.close()

    def add(self,key,value):
        statement='INSERT INTO Data (key,value) VALUES (?,?)'
        cur=self.con.execute(statement,(key,value))
        cur.close()
        return True

    def get(self,key):
        statement='SELECT value FROM Data WHERE key=?'
        cur=self.con.execute(statement,(key,))
        data=cur.fetchone()
        if data is None:
            return None
        value=data[0]
        cur.close()
        return value

if __name__=='__main__':
    print("simple.py")
    assertTrue(True)

    db=Data()
    assertTrue(db.add('one',1))
    assertEquals(1,db.get('one'),"Test get")
    assertTrue(db.add('two',2))
    assertEquals(None,db.get('three'))
    db.close()

    db=Data(keep=True)
    assertEquals(2,db.get('two'))
    db.close()    
    
