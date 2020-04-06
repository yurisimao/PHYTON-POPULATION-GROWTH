#Crescimento da população Brasileira 1980-2016
#DataSus
import matplotlib.pyplot as plt

data = open("massa/crescimento_populacional.csv").readlines()
title = "Crescimento da População Brasileira 1980-2016"
xyear = "Ano"
ypopulation = "População x100.000.000"

x = []
y = []

for i in range(len(data)):
	if i != 0:
		line = data[i].split(";")
		x.append(int(line[0]))
		y.append(int(line[1]))

plt.bar(x, y, color = "#e4e4e4")
plt.plot(x, y, color = "k", linestyle = "--")

plt.title(title)
plt.xlabel(xyear)
plt.ylabel(ypopulation)
plt.show()	
#plt.savefig("crescimento_populacao.png", dpi = 300)



