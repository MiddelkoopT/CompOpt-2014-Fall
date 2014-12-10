#!/usr/bin/python3

## Simple database.  Overwrite existing database file simple.db

import sqlite3
import os
import subprocess
import configparser as cp
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
        self.hostname=platform.uname()[1]
        print("config>%s" % (self.hostname,))
        self.config=cp.ConfigParser()
        self.config.read(['config.ini','local.ini',"config/%s.ini" % (self.hostname,)])
        self.section='Global'
        
    def __getitem__(self,option):
        value=self.config.get(self.section,option)
        if value=='':
            return None
        elif value in ('True','true'):
            return True
        elif value in ('False','false'):
            return False
        return value

    def __getattr__(self,option):
        return self[option]

class R:
    def __init__(self,config):
        ## Fix envrionment (IDLE Mangles these some how when passing to R!)
        userprofile=os.environ['USERPROFILE']
        if config.r_libs_user[0]!='/' and config.r_libs_user[1]==':':
            assert False ## Untested code
            self.libs=config.r_libs_user
        else:
            self.libs="%s/%s" % (userprofile,config.r_libs_user)
            self.exec=config.R
        self.args=['--vanilla']

    def run(self,script):
        ## Build args every time in case config gets changed.
        args=[self.exec]
        args.extend(self.args)
        args.append(script)

        ## must set env directly, not pass it for some reason (IDLE Workaround)
        os.environ['R_LIBS_USER']=self.libs
        try:
            output=subprocess.check_output(args,universal_newlines=True,stderr=subprocess.STDOUT)
            self.output=output.split("\n")
            return self.output
        except subprocess.CalledProcessError as e:
            print("R Subprocess failed: exitcode %d" % (e.returncode,))
            print("libs: %s" % self.libs)
            print(e.output)
            raise e

class GAMS:
    def __init__(self,config):
        self.program=config.GAMS
        self.args=[]

    def run(self,script):
        ## Build args every time in case config gets changed.
        args=[self.program]
        args.extend(self.args)
        args.append(script)
        print("GAMS.run> %s" % args)
        try:
            output=subprocess.check_output(args,universal_newlines=True,stderr=subprocess.STDOUT)
            self.output=output.split("\n")
            #return self.output
            return False ## TODO: GAMS output is lost!
        except subprocess.CalledProcessError as e:
            print("Subprocess failed: exitcode %d (check console for error)" % (e.returncode,))
            print(e.output)
            raise e

def test():
    db=Database()
    assertTrue(db.put('one',1),"Add first entry")
    assertEquals(1,db.get('one'),"Verify write")
    assertTrue(db.put('two',2),"Add second entry")
    db.close()

    config=Config()
    hostname=platform.uname()[1]
    assertEquals('simple.db',config['database'])
    assertEquals('simple.db',config.database)
    assertTrue(config.local,"config/hostname.ini test)")

    ## Orchastration
    r=R(config)
    output=r.run('simple.R')
    #print(output)
    assertEquals('[1] "simple.R>"',output[0],'Script execution')
    assertEquals('[1] "simple.R> done"',output[-2],'Script execution done')

    g=GAMS(config)
    output=g.run('simple.gms')
    print(output)

if __name__=='__main__':
    print("simple.py>")
    test()
    
