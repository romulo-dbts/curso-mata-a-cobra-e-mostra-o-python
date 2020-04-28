# imprimir lista com todos os nomes dos prédios
# predio com maior area. em caso de empate imprima o nome do primeiro predio lido dentro do grupo dos empatados com maior área
# predios com cujo síndico tem um nome palindrômo. Desconsidere maiúsculos e minusculos
# imprimir dados de UM predio em particular
import sys
num_buildings = int(input('Digite o número de prédios que existem no condomínio: '))

if not num_buildings:
	print('O condomínio não possui prédios')
	sys.exit(0)

palindrome = list()
condominium = dict()
biggest_area = 0
biggest_area_building_name = ''

for x in range(num_buildings):
	building_name = input('Digite o nome do prédio: ')
	building_area_size = float(input('Digite o tamanho da área do prédio: '))

	if building_area_size < 0:
		print('A área não pode ser negativa')
		sys.exit(0)

	building_manager = input('Digite o nome do síndico do prédio: ')
	condominium[building_name] = {
		'area': building_area_size,
		'manager': building_manager,
	}

	if building_area_size > biggest_area:
		biggest_area = building_area_size
		biggest_area_building_name = building_name
	if building_manager.upper() == building_manager[::-1].upper():
		palindrome.append((building_name, building_manager))

choosen_building_to_print = input('Digite o nome do prédio que deve ter suas informações impressas: ')


print('O nome do(s) prédio(s) é/são: {}'.format(', '.join(list(condominium.keys()))))
print('O prédio com maior área é o %s que mede %s' % (biggest_area_building_name, biggest_area))
if choosen_building_to_print in condominium:
	building = condominium[choosen_building_to_print]
	print('O prédio %s tem uma área de %s e seu síndico se chama %s' % (choosen_building_to_print, building['area'], building['manager']))
if palindrome:
	msg = 'Predio(s) cujo(s) síndico(s) possuem nomes palíndromo: '	
	msg_variables = ['(Prédio: '+', Síndico: '.join(palind)+')' for palind in palindrome]
	print(msg+', '.join(msg_variables))