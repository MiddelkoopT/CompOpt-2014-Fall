
print("TDD.py>")

assert True==True
#assert True==False

def addInt(a,b):
    return a+b

def subInt(a,b):
    return a-b


assert 5==addInt(2,3)
assert 2==subInt(5,3)
