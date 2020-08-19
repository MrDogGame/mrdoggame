n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2
if m < 5:
    print('Aluno esta reprovado!')
elif m >= 5 and m <= 6.9:
    print('Aluno esta de recuperação!')
else:
    print('Aluno foi aprovado!')