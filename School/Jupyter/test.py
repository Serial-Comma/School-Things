import time
n=10000000
print('%12s%16s'%('problem sizee N', 'seconds'))
for count in range(5):
    start=time.time()
    work=1
    for k in range(n):
        work+=1
        work-=1
    elapsed = time.time()-start
    print('%12d%16.12f'%(n,elapsed))
    n*=2