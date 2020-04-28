# A partir de um intervalo de numeros inteiros que vão de 1 até n, 
# construa um dicionário onde a chave seja o próprio número e o valor dessa chave seja o quadrado do número. Sendo assim, 
# cada par chave/valor terá a seguinte configuração (x, x*x)
upper_limit = int(input('Digite o limite superior do intervalo: '))
squared_dict = {x: x*x for x in range(1, upper_limit+1)}

print(f'O dicionário de quadrados é {squared_dict}')
