# Escreva um programa em Python para contar o numero de caracteres 
# em uma string. Peça ao usuário para informar essa string antes
# de começar a contar as ocorrencias. Se o usuário informar uma
# string vazia, imprima "Não tente me enganar"

sentence = input('Digite uma sentença: ')

# we can also use defaultdict
occurrences = dict()

if not sentence:
    print('Não tente me enganar! String vazia.')
else:
    for char_sentence in sentence:
        if char_sentence in occurrences:
            occurrences[char_sentence] += 1
        else:
            occurrences[char_sentence] = 1

    print(f'Veja só as ocorrencias das letras {occurrences}')
