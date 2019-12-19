import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf

df0 = pd.read_csv('exp0_Nagib_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy'],
                 header=0)
df0.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy']
print(df0)

df1 = pd.read_csv('exp1_Random_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy'],
                 header=0)
df1.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy']
print(df1)

df2 = pd.read_csv('exp2_minairtime_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy'],
                 header=0)
df2.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy']
print(df2)

df3 = pd.read_csv('exp4_Equaldistr_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy'],
                 header=0)
df3.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy']
print(df3)

node_numbers = df1['Nodes'].tolist()
der0 = df0['DER'].tolist()
der1 = df1['DER'].tolist()
der2 = df2['DER'].tolist()
der3 = df3['DER'].tolist()


collision0 = df0['Collision'].tolist()
collision1 = df1['Collision'].tolist()
collision2 = df2['Collision'].tolist()
collision3 = df3['Collision'].tolist()

energy0 = df0['OverallEnergy'].tolist()
energy1 = df1['OverallEnergy'].tolist()
energy2 = df2['OverallEnergy'].tolist()
energy3 = df3['OverallEnergy'].tolist()

fig1 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, der0, label='Menor_Canal', linestyle='--', marker='o')
plt.plot(node_numbers, der1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, der2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, der3, label='Distro_Justo', linestyle='--', marker="D")

pdf = matplotlib.backends.backend_pdf.PdfPages('DER-Comparation.pdf')
plt.yticks([ 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize = 12)
plt.xticks(fontsize = 12)
plt.ylabel("DER", fontsize=15)
plt.xlabel("Número de Dispositivos", fontsize=15)
plt.legend(prop=dict(size=12))
plt.ylim((0.3, 1.02))
plt.grid()
plt.show()
pdf.savefig(fig1)
pdf.close()

fig2 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, collision0, label='Menor_Canal', linestyle='--', marker='o')
plt.plot(node_numbers, collision1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, collision2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, collision3, label='Distro_Justo', linestyle='--', marker="D")

pdf = matplotlib.backends.backend_pdf.PdfPages('Collisions-Comparation.pdf')
plt.ylabel("Número de Colisões", fontsize=15)
plt.xlabel("Número de Dispositivos", fontsize=15)
plt.legend(prop=dict(size=12))
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid()
plt.show()
pdf.savefig(fig2)
pdf.close()

fig3 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, energy0, label='Menor_Canal', linestyle='--', marker='o')
plt.plot(node_numbers, energy1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, energy2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, energy3, label='Distro_Justo', linestyle='--', marker="D")

pdf = matplotlib.backends.backend_pdf.PdfPages('Energy-Comparation.pdf')
plt.ylabel("Consumo de Energia da Rede(mJ)", fontsize=15)
plt.xlabel("Número de Dispositivos", fontsize=15)
plt.legend(prop=dict(size=12))
plt.xticks(fontsize = 12)
plt.yticks(fontsize = 12)
plt.grid()
plt.show()
pdf.savefig(fig3)


pdf.close()


