import random
print('\n\n\n') # Espaço de execução para ficar bonitinho no visual code studio
# Programa para medição de temperatura
#temp = random.uniform(15,45)


hora = -1 #meia noite

temp = random.uniform(23,20)
while hora < 5:
    
    temp_neg =random.random()
    temp -= temp_neg
    hora += 1
    print('Hora: ', hora, 'temp = %.2f'%temp)

while hora < 15:

    temp_neg =random.randint(1,3)
    temp += temp_neg
    hora += 1
    print('Hora: ', hora, 'temp = %.2f'%temp)

while hora < 24:
    temp_neg =random.randint(1,3)
    temp -= temp_neg
    hora += 1
    print('Hora: ', hora, 'temp = %.2f'%temp)



print('\n\n\n')# Espaço de execução para ficar bonitinho no visual code studio

