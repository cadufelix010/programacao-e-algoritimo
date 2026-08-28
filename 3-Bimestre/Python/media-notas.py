soma = 0
contador = 0

nota = float(input('Digite uma nota de 0 a 10: '))

while nota >= 0 and nota <= 10:
    soma = soma + nota
    contador = contador + 1
    nota = float(input('Digite outra nota ou um número fora de 0 a 10 para parar: '))

if contador > 0:
    media = soma / contador
    print('Média:', media)
else:
    print('Nenhuma nota válida')
