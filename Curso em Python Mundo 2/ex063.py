num = int(input('Digite um número: '))
count = 0
fn1 = 0
fn2 = 1
#0 + 1 + 1 + 2 + 3 + 5 + 8
while count < num:
    tot = fn1 + fn2
    print(tot,end=' -> ')
    fn2 = fn1
    fn1 = tot
    count += 1
print('FIM')