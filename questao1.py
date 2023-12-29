#Questão 1
print('Olá, bem-vindo a loja do Pablo Ramon Galdino Barros')
a = float(input('Qual o valor do produto? '))
b = int(input('Qual a quantidade do produto? '))

if b * a >= 1000 and b * a < 3000:
    desconto = ((b * a) * 3) / 100
    print('O valor SEM desconto: R${}'.format(b * a))
    print('O valor COM desconto: R${}'.format((b * a) - desconto))
elif b * a >= 3000 and b * a < 5000:
    desconto = ((b * a) * 5) / 100
    print('O valor SEM desconto: R${}'.format(b * a))
    print('O valor COM desconto: R${}'.format((b * a) - desconto))
elif b * a >= 5000:
    desconto = ((b * a) * 8) / 100
    print('O valor SEM desconto: R${}'.format(b * a))
    print('O valor COM desconto: R${}'.format((b * a) - desconto))
#Achei conviniente deixar o não desconto no else com uma mensagem dizendo porque o desconto não foi aplicado
else:
    print('O valor SEM desconto: R${}'.format(b * a))
    print('Desconto aplicado para valores acima de R$1000.')

