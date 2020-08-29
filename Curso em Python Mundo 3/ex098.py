from time import sleep
def counter(i,f,p):
    if i > f and p < 0:
        p *= 1
    if i < f and p > 0:    
        for c in range(i,f+1,p):
            print(c,end=' ',flush=True)
            sleep(0.5)
    elif p == 0:
        for c in range(i,f,1):
            print(c,end=' ',flush=True)
            sleep(0.5)
    else:
        for c in range(i,f,-p):
            print(c,end=' ',flush=True)
            sleep(0.5)
print('Counter from 1 to 10 pass 1 by 1')            
counter(1,10,1)
print()
print('Counter from 10 to 0 pass 2 by 2')
counter(10,0,2)
print()
start = int(input('enter a number to start: '))
end = int(input('enter a number to end: '))
pas = int(input('enter a number to pass: '))
counter(start,end,pas)
print()