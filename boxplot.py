#Box plot - diagrama de caixa

import matplotlib.pyplot as plt
import random

vetor = []

for i in range(100):
    numero_aleatorio = random.randint(0,15)
    vetor.append(numero_aleatorio)

plt.boxplot(vetor)
plt.title('Meu box plot')
plt.show()
