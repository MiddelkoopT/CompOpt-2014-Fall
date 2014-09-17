#!/usr/bin/python
# In class example CompOpt Fall 2014 CC by SA

print("convert1>")
f=open('dataset1.csv')
w=open('dataset1-convert.csv','w')

header=f.readline()[:-1]
assert "x1,x2" == header
w.write("x1,x2,x1px2,x1mx2\n")

for l in f:
    l=l[:-1]
    #print(l)
    x1,x2=l.split(',')
    x1,x2=float(x1),float(x2)
    #print(x1,x2)
    r=[x1,x2,x1+x2,x2-x1]
    r=map(lambda x: str(x),r)
    w.write(','.join(r)+"\n")

w.close()
