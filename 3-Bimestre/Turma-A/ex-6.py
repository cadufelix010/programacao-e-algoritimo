soma = 0
contador = 0

while True:
    nota = float(input('Digite uma nota de 0 a 10. Para terminar, digite outro valor: '))
    if 0 <= nota <= 10:
        soma += nota
        contador += 1
    else:
        break

if contador > 0:
    media = soma / contador
    print(f'A média das {contador} notas é: {media:.2f}')
else:
    print('Nenhuma nota válida foi digitada.')
