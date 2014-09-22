#/usr/bin/python3
# Python and TDD Examples Copyright 2014 by Timothy Middelkoop CC by SA

print("TDD.py>")

assert True==True

# Ensure our test fails
failed=False
try:
    assert True==False
except AssertionError:
    failed=True
assert failed

# Basic functions.
def addInt(a,b):
    return a+b

def subInt(a,b):
    return a-b

assert 5==addInt(2,3)
assert 2==subInt(5,3)

# Basic classes

class Compute:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __repr__(self):
        return "<a:%d b:%d>" % (self.a,self.b)

    def addInt(self):
        return self.a+self.b

    def subInt(self):
        return self.a-self.b


c=Compute(2,3)
assert c is not None
assert c.a==2
assert c.b==3

assert 5==c.addInt()
assert -1==c.subInt()

## New assertion tools
def assertEquals(expected,returned,message=None):
    if not expected==returned:
        if message:
            print("assertEquals Failed: |%s| |%s| %s" % (expected,returned,message))
        assert expected==returned

failed=False
try:
    assertEquals('<a:2, b:3>',str(c),message=False)
except AssertionError:
    failed=True
assert failed

assertEquals('<a:2 b:3>',str(c),'Test output of the Compute instance')

