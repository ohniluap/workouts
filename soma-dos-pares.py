soma = 0
cont = 0
for c in range(1, 7):
    num = int(input('Digite o {}º valor: '.format(c)))
    if num % 2 == 0:
        soma += c
        cont += 1
print('Você informou {} números PARES e a soma foi de {}.'.format(cont, soma))
