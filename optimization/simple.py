#!/usr/bin/python3

from gurobipy import * 

m = Model("simple")
x1 = m.addVar(name="x1")
x2 = m.addVar(name="x2")
m.update()

print("x1:%s x2:%s" % (x1,x2))

m.setObjective(x1 + 2*x2, GRB.MAXIMIZE)
m.addConstr(x1 + x2 <= 40, "C1")
m.addConstr(2*x1 + x2 <= 60, "C2")

m.optimize()

print("Solution: %f" % (m.objVal,))
for v in m.getVars():
    print("%s:%f" % (v.varName, v.x))


