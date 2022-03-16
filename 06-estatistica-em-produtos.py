#NESSE EXERCICOS DESENVOLVI UM PROGRAMA CAPAZ DE CALCULAR O TOTAL GASTO EM UMA COMPRA, DIZER QUAL É O PRODUTO MAIS BARATO E DIZER QUANTOS PRODUTOS CUSTAM MAIS DE MIL REAIS
soma=barato=totmil=cont=menor=0
while True:
    produ=str(input('Nome do produto:'))
    preço=int(input('Preço: R$:'))
    soma=soma+preço
    cont=cont+1
    if preço>1000:
        totmil=totmil+1
    if cont==1:
        menor=preço
    else:
        if preço<menor:
            menor=preço
    continuar=' '
    while continuar not in 'SN':
        continuar=str(input('Deseja adicinar mais algum produto? [S/N]')) .strip() .upper() [0]
    if continuar=='N':
        break
print(f'O total de gastos na compre é de R$:{soma}.')
print(f'O número de produtos que custam mais de MIL REAIS é {totmil}.')
print(f'O produto com o menor preço é {menor}.')