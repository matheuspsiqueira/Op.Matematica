import os
def potencia():
    os.system('cls')
    n1 = int(input('Digite o valor da base: '))
    n2 = int(input('Digite o valor da potência: '))
    pot = n1 ** n2
    print('O número', n1,'elevado à', n2,'é igual a:', pot)

    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_comp()
    elif e == 9:
        print('')

def fatorial():
    os.system('cls')
    n = int(input('Digite o número: '))
    fat = 1
    i = 2
    while i <= n:
        fat = fat*i
        i += 1
    print('O fatorial do número é: ', fat)
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_comp()
    elif e == 9:
        print('')

def primo():
    os.system('cls')
    n = int(input('Digite um número: '))
    mult = 0
    for i in range(2, n):
        if n % i == 0:
            mult += 1
    if mult == 0:
        print('O número é primo')
    else:
        print('O número não é primo')
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_comp()
    elif e == 9:
        print('')

def par_impar():
    os.system('cls')
    n = int(input('Digite o número: '))
    if n % 2 == 0:
        print('O número é par')
    else:
        print('O número é ímpar')
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_comp()
    elif e == 9:
        print('')

def soma():
    os.system('cls')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('O resultado da equação é: ', n1 + n2)
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_ariti()
    elif e == 9:
        print('')

def sub():
    os.system('cls')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('O resultado da equação é: ', n1 - n2)
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_ariti()
    elif e == 9:
        print('')

def mult():
    os.system('cls')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('O resultado da equação é: ', n1 * n2)
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_ariti()
    elif e == 9:
        print('')

def div():
    os.system('cls')
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    print('O resultado da equação é: ', n1 / n2)
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_ariti()
    elif e == 9:
        print('')

def creditos():
    os.system('cls')
    print('''
╭━┳━╭━╭━╮╮
┃┈┈┈┣▅╋▅┫┃
┃┈┃┈╰━╰━━━━━━╮
╰┳╯┈┈┈┈┈┈┈┈┈◢▉◣
╲┃┈┈┈┈┈┈┈┈┈▉▉▉
╲┃┈┈┈┈┈┈┈┈┈◥▉◤
╲┃┈┈┈┈╭━┳━━━━╯
╲┣━━━━━━┫
    ''')
    print('Obrigado por utilizar o programa!!')
    print('')
    e = int(input('Digite 5 para voltar ao programa ou 9 para sair: '))
    if e == 5:
        op_comp()
    elif e == 9:
        print('')

def config():
    os.system('cls')
    print('|-------------------------------|')
    print('|         Configurações         |')
    print('|-------------------------------|')
    print('| 1 - Alterar cor               |')
    print('| 5 - Voltar                    |')
    print('|                               |')
    print('|                               |')
    print('|                               |')
    print('|...............................|\n\n')
    op = int(input('Escolha uma das opções acima: '))
    print('')
    if op == 1:
        print('Alterar cor')
    elif op == 5:
        print(menu_principal())
    else:
        print('Digite uma opção inválida')
        print(config())

def op_comp():
    os.system('cls')
    print('|-------------------------------|')
    print('|     Operações Complexas       |')
    print('|-------------------------------|')
    print('| 1 - Par ou Ímpar              |')
    print('| 2 - Número Primo              |')
    print('| 3 - Fatorial                  |')
    print('| 4 - Potências                 |')
    print('| 5 - Voltar                    |')
    print('|...............................|\n\n')
    op = int(input('Escolha uma das opções acima: '))
    print('')
    if op == 1:
        par_impar()
    elif op == 2:
        primo()
    elif op == 3:
        fatorial()
    elif op == 4:
        potencia()
    elif op == 5:
        print(menu_principal())
    else:
        print('Digite uma opção inválida')
        print(op_comp())

def op_ariti():
    os.system('cls')
    print('|-------------------------------|')
    print('|     Operações Aritiméticas    |')
    print('|-------------------------------|')
    print('| 1 - Soma                      |')
    print('| 2 - Subtração                 |')
    print('| 3 - Multiplicação             |')
    print('| 4 - Divisão                   |')
    print('| 5 - Voltar                    |')
    print('|...............................|\n\n')
    op = int(input('Escolha uma das opções acima: '))

    if op == 1:
        soma()
    elif op == 2:
        sub()
    elif op == 3:
        mult()
    elif op == 4:
        div()
    elif op == 5:
        print(menu_principal())
    else:
        print('Digite uma opção inválida')
        print(op_ariti())

def tela_inicial():
    print('Programa de operações Matemáticas')
    print('..................................')
    print('.                                .')
    print('.                                .')
    print('.                                .')
    print('.       Seja bem vindo....       .')
    print('.                                .')
    print('.                                .')
    print('.                                .')
    print('..................................')
    print('')
    print('')
    print('')
    print('Criado por: Matheus Siqueira\n\n\n')
    input('Digite qualquer tecla para entrar no programa: ')
    os.system('cls')

tela_inicial()

def menu_principal():
    os.system('cls')
    op = 0
    if op != 5:
        print('|---------Menu Principal--------|')
        print('|-------------------------------|')
        print('| 1 - Operações Aritiméticas    |')
        print('| 2 - Operações Complexas       |')
        print('| 3 - Configurações             |')
        print('| 4 - Créditos                  |')
        print('| 5 - Sair                      |')
        print('|...............................|\n\n')
        op = int(input('Escolha uma das opções acima: '))
        if op == 1:
            print(op_ariti())
        elif op == 2:
            print(op_comp())
        elif op == 3:
            print(config())
        elif op == 4:
            print(creditos())
        elif op == 5:
            print()
        else:
            print('Opcção Inválida')

menu_principal()