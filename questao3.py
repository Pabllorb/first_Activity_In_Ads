print('-' * 10,'Bem-Vindo(a) à Copiadora do Pablo Ramon Galdino Barros', '-' * 10)
#cria função que pede um serviço extra
def servico_extra():
    while True:
        print()
        print('Deseja adicionar mais algum serviço?')
        print('1 - Encadernação Simples - R$ 10,00')
        print('2 - Encadernação Capa Dura - R$ 25,00')
        print('0 - Não desejo mais nenhum serviço')
        ext1 = input(': ')
        if ext1 == '1'or ext1 == '2' or ext1 == '0':
            if ext1 == '1':
                return 10.00
            elif ext1 == '2':
                return 25.00
            else:
                return 0.00
        else:
            print('Opção Inválida.\nTente novamente.')

#cria função que pede o número de páginas
def num_pagina():
    while True:
        #try e except para tratar ValueError
        try:
            print()
            p1 = int(input('Número de páginas: '))
            if p1 > 0 and p1 < 10000:
                if p1 > 0 and p1 < 10:
                    return p1
                elif p1 >= 10 and p1 < 100:
                    desconto = p1 * 10 / 100
                    paginas = p1 - desconto
                    return paginas
                elif p1 >= 100 and p1 < 1000:
                    desconto = p1 * 15 / 100
                    paginas = p1 - desconto
                    return paginas
                elif p1 >= 1000 and p1 < 10000:
                    desconto = p1 * 20 / 100
                    paginas = p1 - desconto
                    return paginas
            else:
                print('Não aceitamos este número de páginas.\n'
                      'Por favor, tente novamente.')
        except ValueError:
            print('Digite apenas números')

#cria função que pede o serviço desejado
def escolha_servico():
    while True:
        print('Entre com o serviço desejado:')
        print('DIG - Digitalização - R$ 1,40/p')
        print('ICO - Impressão colorida - R$ 1,00/p')
        print('IBO - Impressão preto e branco - R$ 0,40/p')
        print('FOT - Fotocópia - R$ 0,20/p')
        s1 = input(': ')
        #tratamento de entrada com .lower()
        s1 = s1.lower()
        if s1 == 'dig' or s1 == 'ico' or s1 == 'ibo' or s1 == 'fot':
            if s1 == 'dig':
                return 1.40
            elif s1 == 'ico':
                return 1.00
            elif s1 == 'ibo':
                return 0.40
            else:
                return 0.20
        else:
            print('Serviço Inválido. \nTente novamente.')

            print()

#programa principal
servico = escolha_servico()
paginas = num_pagina()
extra = servico_extra()

preco_final = (paginas * servico) + extra

print(
    'Total: R$ {:.2f}.\nServiço R$ {:.2f} x Páginas {:.0f} + Extra R$ {:.2f}.'
    .format(preco_final, servico, paginas, extra))

