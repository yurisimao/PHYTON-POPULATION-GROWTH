#Boxplot - Diagrama de Caixa

import matplotlib.pyplot as plt
import random

my_list = []

for i in range(10):
	ramdom_number = random.randint(0, 5)
	my_list.append(ramdom_number)


plt.boxplot(my_list)
plt.title("Boxplot")
plt.show()