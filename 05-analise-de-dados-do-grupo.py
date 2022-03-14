print('=-='*12)
print('CADASTRE UMA PESSOA')
print('=-='*12)
tot18=0
totmasc=0
totfem20=0
while True:
    idade=int(input('IDADE: '))
    sexo=' '
    while sexo not in 'MmFf':
     sexo=str(input('SEXO [M/F] ')).strip().upper()[0]
    if idade >=18:
        tot18=tot18+1
    if sexo =='M':
        totmasc=totmasc+1
    if sexo=='F' and idade<20 :
        totfem20=totfem20+1
    continuar=' '
    while continuar not in 'SsNn':
        continuar=str(input('DESEJA CONTINUAR? [S/N] ')).strip() .upper()[0]
    if continuar=='N':
        break
print(f'\033[32mO total de pessoa com mais de 18 anos é {tot18}.')
print(f'O número de homens cadastrados é de {totmasc}.')
print(f'O número de mulheres com menos de 20 anos é de {totfem20}.')
print('FIM.')
