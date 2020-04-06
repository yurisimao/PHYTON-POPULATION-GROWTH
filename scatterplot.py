import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 0]
z = [200, 25, 400, 330, 100]

title = "Scatterplot: Gráfico de dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

plt.title(title)
plt.xlabel(eixox)
plt.ylabel(eixoy)

#Chamada grafico de pontos
plt.scatter(x, y, label = "Meus pontos", color = "k", marker = ".", s=z)

#Chamada grafico de linhas
plt.plot(x, y, color = "k", linestyle = "--")

#Exibe legenda
plt.legend()

plt.show()
#plt.savefig("figura1.png", dpi = 300)