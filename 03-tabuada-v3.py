#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE CALCULAR A TABUDADA DE QUALQUER NÚMERO ESOCOLHIDO PELO USUÁRIO, SE ELE DIGITAR UM NÚMERO NEGATIVO O PROGRAMA É FINALIZADO.
while True:
    n=int(input('\033[4mQUER VER A TABUADA DE QUAL NÚMERO? \033[m'))
    if n <0:
     break
    for t in range(1,11):
        v=n*t
        print(f'\033[32m{n} x {t}= {v}\033[m')
print('Calculador de tabuada finalizado.')
