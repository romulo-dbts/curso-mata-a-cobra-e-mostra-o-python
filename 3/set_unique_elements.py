# Peça que o usuário informe uma lista de elementos e imprima 
# uma list que contenha apenas uma ocorrencia de cada elemento da lista,
# ou seja, não podem haver repetições de um elemento dessa lista.

num_elements = int(input('Quantos elementos haverão na lista? '))
element_msg = "Digite algo: "
original_list = [input(element_msg) for _ in range(num_elements)]
elements_set = sorted(list(set(original_list)))

print(f'Essa é a lista informada: {original_list}')
print(f'Veja só, sem repetições!: {elements_set}')
