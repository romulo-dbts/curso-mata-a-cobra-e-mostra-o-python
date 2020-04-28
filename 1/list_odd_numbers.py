#Escreva um programa em Python que a partir da entrada do usuário
#construa uma lista de números inteiros e, caso hajam números ímpares,
#imprima uma lista contendo-os. Caso não haja nenhum número ímpar 
#na lista fornecida pelo usuário imprima a lista original.


num_elements = int(input("Quantos numeros haverão na lista? "))
element_msg = 'Digite um número: '
elements = [int(input(element_msg)) for x in range(num_elements)]

odd_numbers = [odd for odd in elements if odd % 2 != 0]

if odd_numbers:
    print(f'Os números ímpares são: {odd_numbers}')
else:
    print(f'A lista não contém números ímpares, veja: {elements}')
