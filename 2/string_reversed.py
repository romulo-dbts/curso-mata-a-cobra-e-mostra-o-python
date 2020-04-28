# Escreva um programa em Python que leia uma string informada pelo usuário
# e imprime essa mesma string invertida, ou seja, de trás para frente.
# Além disso verifique se a string invertida é idêntica a string original.
# Caso sejam inguais imprima "Encontramos um palíndromo"

sentence = input('Digite uma palavra ou frase: ')
reversed_sentence = sentence[::-1]

print(f'A sentença invertida é: {reversed_sentence}')
if sentence == reversed_sentence:
    print(f'Encontramos um palíndromo!')
