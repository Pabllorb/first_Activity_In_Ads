#Questão 2
print('     Bem-vindo à açaiteria do Pablo Ramon Galdino Barros     ')
print(25 * '-', 'CARDÁPIO', 25 * '-')
print('-----------| Tamanho | Cupuaçu (CP) | Açaí (AC) |-----------')
print('-----------|    P    |   R$ 10,00   |  R$ 12,00 |-----------')
print('-----------|    M    |   R$ 15,00   |  R$ 17,00 |-----------')
print('-----------|    G    |   R$ 19,00   |  R$ 21,00 |-----------')
acumulador = 0
while True:
    sabor = input('Entre com o sabor desejado (CP/AC): ')
    #Como forma de evitar mais erros usei o ".lower()" para todas as entradas
    if sabor.lower() == 'cp' or sabor.lower() == 'ac':
        print()
        tamanho = input('Entre com o tamanho desejado (P/M/G): ')
        if tamanho.lower() == 'p' or tamanho.lower() == 'm' or tamanho.lower() == 'g':
            if sabor.lower() == 'cp' and tamanho.lower() == 'p':
                preco = 10.00
                sabor = 'CUPUAÇU'
            elif sabor.lower() == 'cp' and tamanho.lower() == 'm':
                preco = 15.00
                sabor = 'CUPUAÇU'
            elif sabor.lower() == 'cp' and tamanho.lower() == 'g':
                preco = 19.00
                sabor = 'CUPUAÇU'
            elif sabor.lower() == 'ac' and tamanho.lower() == 'p':
                preco = 12.00
                sabor = 'AÇAÍ'
            elif sabor.lower() == 'ac' and tamanho.lower() == 'm':
                preco = 17.00
                sabor = 'AÇAÍ'
            elif sabor.lower() == 'ac' and tamanho.lower() == 'g':
                preco = 21.00
                sabor = 'AÇAÍ'
            acumulador += preco
            print()
            print('Você pediu {} Tamanho {}: R$ {:.2f}'.format(sabor, tamanho.upper(), preco))

            maispedidos = input('Deseja mais alguma coisa? [S]im ou [N]ão? ')
            if maispedidos.upper() == 'S':
                continue
            else:
                print('Total à pagar: R$ {:.2f}'.format(acumulador))
                break

        else:
            print('Tamanho inválido. Tente novamente.')
            continue

    else:
        print('Sabor inválido. Tente novamente.')
        continue



