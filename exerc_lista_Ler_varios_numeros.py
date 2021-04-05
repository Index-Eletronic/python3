'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
'''
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N]: '))
    if resp in 'Nn':
        break
print('-=' * 30)
print((f'Você digitou {len(valores)}elementos. '))
valores.sort(reverse=True)
print(f'Os valores em ordem descrecente são {valores}:')
if 5 in valores: # Faz busca dentro de coleções, dentro de listas.
    print('O valore 5 faz parte da lista:')
else:
    print('O valore 5 não foi encontrado na lista')
