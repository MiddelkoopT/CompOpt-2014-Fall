#!/usr/bin/python3

## Simple database.  Overwrite existing database file simple.db

import sqlite3
import os
import configparser
import platform

from TDDUtils import *

class Database:
    def __init__(self,database='simple.db'):
        if os.path.exists(database):
            os.unlink(database)
        schema=open('simple.sql').read()
        #print(schema)
        self.con=sqlite3.connect(database)
        self.con.execute(schema)
    def put(self,key,value):
        statement='INSERT INTO Data (key,value) VALUES (?,?)'
        cur=self.con.execute(statement,(key,value))
        cur.close()
        return True

    def get(self,key):
        statement='SELECT value FROM Data WHERE key=?'
        cur=self.con.execute(statement, (key,))
        value=cur.fetchone()
        cur.close()
        return value[0]

    def close(self):
        self.con.commit()
        self.con.close()

class Config:
    def __init__(self):
        self.config=configparser.ConfigParser()
        self.config.read('simple.ini')
        
    def __getitem__(self,index):
        return self.config['Simple'][index]

    def __getattr__(self,index):
        return self[index]
        
def test():
    db=Database()
    assertTrue(db.put('one',1),"Add first entry")
    assertEquals(1,db.get('one'),"Verify write")
    assertTrue(db.put('two',2),"Add second entry")
    db.close()

    config=Config()
    hostname=platform.uname()[1]
    print(hostname)
    assertEquals('simple.db',config['database'])
    assertEquals('simple.db',config.database)

if __name__=='__main__':
    print("simple.py>")
    test()
    
