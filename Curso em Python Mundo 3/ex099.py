from time import sleep
def maior(*num):
    m = 0
    count = 0
    for v in num:
        print(v,end=' ',flush=True)
        count += 1
        sleep(0.5)
        if v > m:
            m = v
    print(f'Ao todo foram informados {count} valores.')
    print(f'O maior número informado foi {m}')        

maior(2,9,4,5,7,1)

maior(4,7,0)

maior(1,2)

maior(6)

maior()