#!/usr/bin/python3

import cProfile
import pstats

class Compute:
    def run(self,n):
        A=[]
        for i in range(0,n):
            A.append(i)
        s=0
        for a in A:
            s+=a
        return s


if __name__=='__main__':
    print("simple>")
    p=cProfile.Profile()
    c=Compute()
    c.run(10)
    p.runcall(c.run,10000)
    p.create_stats()
    s=pstats.Stats(p)
    s.sort_stats('cumtime')
    s.print_stats()
