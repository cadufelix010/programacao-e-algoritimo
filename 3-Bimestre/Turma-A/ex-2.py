num1 = int(input('Escolha um número: '))
num2 = int(input('Escolha outro número: '))
if num1 > num2:
    print(f'O {num1} é maior que o {num2}')
elif num1 < num2:
    print(f'O {num2} é maior que o {num1}')
else:
    print(f'Os números {num1} e {num2} são iguais')
