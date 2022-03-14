from time import sleep
from random import randint
vit=0
print('\033[4mVAMOS JOGAR PAR OU ÍMPAR!\033[m')
while True:
    n=int(input('\033[1mDiga um valor: \033[m'))
    escolhapc=randint(0,11)
    total=n+escolhapc
    es=' '
    while es not in 'PpIi':
       es=str(input('Par ou Ímpar [P/I] ' )).upper() .strip()[0]
    print(f'\033[34mvocê escolheu {n} e o computador escolheu {escolhapc} o total é {total}\033[m')
    print('DEU PAR 'if total%2==0 else 'DEU ÍMPAR')
    if es =='P':
        if total % 2==0:
            print('\033[32mVocê venceu!\033[m')
            vit=vit+1
        else:
            print('\033[31mO computador venceu.\033[m')
            break
    if es == 'I':
        if total %2==1:
            print('\033[32mVocê venceu!\033[m')
            vit=vit+1
        else:
            print('\033[31mO computador venceu.\033[m')
            break
    sleep(1)
    print('\033[32mVamos jogar novamente...\033[m')
print(f'\033[31mGAME OVER! você conseguiu ganhar do computador {vit} vezes.')


