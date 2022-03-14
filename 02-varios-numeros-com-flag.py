#NESSE EXERCICIO DESENVOLVI UM PROGRAMA CAPAZ DE SOMAR TODOS OS NÚMERO ESCOLHIDOS PELO USÚARIO, E DIZER QUAL O VALOR DA SOMA E QUANTOS NÚMEROS FORAM DIGITADOS.
print('DIGITE UM VALOR (DIGITE 999 PARA PARAR.)')
cont=soma=0
while True:
    n=int(input('Digite um valor: '))
    if n==999:
        break
    cont=cont+1
    soma=soma+n
print(f'a soma dos números digitas é {soma}, você digitou {cont} números no total')