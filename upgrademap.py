import os.path

from npcs import *

def getname(c):
    return NPC_DICT[c].__name__ if c!= '0' else ''

for i in range(15):
    fn = os.path.join('map', 'floor%03d.dat' % (i+1))
    with open(fn) as f:
        l = f.readlines()
    l2 = []
    for r in l:
        s = ','.join([getname(c) for c in r[:-1]])
        l2.append(s)
    print l2
    with open(fn, 'w') as f:
        for r in l2:
            print >>f, r
