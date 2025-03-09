print('Soma de números pares')

soma = 0
count = 0

for i in range(1,7):
    num = int(input(f'Digite o {i}º número: '))
    
    if num % 2 == 0:
        soma += num 
        count += 1
    
print(f'Nós temos {count} números pares e a soma deles é: {soma}')