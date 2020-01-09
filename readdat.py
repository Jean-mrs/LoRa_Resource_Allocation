import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import matplotlib.ticker as mticker


class MathTextSciFormatter(mticker.Formatter):
    def __init__(self, fmt="%1.2e"):
        self.fmt = fmt

    def __call__(self, x, pos=None):
        s = self.fmt % x
        decimal_point = '.'
        positive_sign = '+'
        tup = s.split('e')
        significand = tup[0].rstrip(decimal_point)
        sign = tup[1][0].replace(positive_sign, '')
        exponent = tup[1][1:].lstrip('0')
        if exponent:
            exponent = '10^{%s%s}' % (sign, exponent)
        if significand and exponent:
            s =  r'%s{\times}%s' % (significand, exponent)
        else:
            s =  r'%s%s' % (significand, exponent)
        return "${}$".format(s)


df0 = pd.read_csv('exp0_Nagib_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay ', 'STD_delay'],
                 header=0)
df0.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay ', 'STD_delay']
print(df0)

df1 = pd.read_csv('exp1_Random_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay ', 'STD_delay'],
                 header=0)
df1.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay ', 'STD_delay']
print(df1)

df2 = pd.read_csv('exp2_minairtime_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay ', 'STD_delay'],
                 header=0)
df2.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay ', 'STD_delay']
print(df2)

df3 = pd.read_csv('exp4_Equaldistr_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay ', 'STD_delay'],
                 header=0)
df3.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay ', 'STD_delay']
print(df3)

df4 = pd.read_csv('exp3_ADR_16min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay ', 'STD_delay'],
                 header=0)
df4.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay ', 'STD_delay']
print(df4)

node_numbers = df1['Nodes'].tolist()
der0 = df0['DER'].tolist()
der1 = df1['DER'].tolist()
der2 = df2['DER'].tolist()
der3 = df3['DER'].tolist()
der4 = df4['DER'].tolist()
index0 = []

for i in range(1, 8):
    somatorio1 = 0
    somatorio2 = 0
    for x in range(0, i):
        somatorio1 += der0[x]
    for x in range(0, i):
        somatorio2 += der0[x] * der0[x]
    index0.append(pow(somatorio1, 2)/(i*somatorio2))
print(index0)
index1 = []
for i in range(1, 8):
    somatorio1 = 0
    somatorio2 = 0
    for x in range(0, i):
        somatorio1 += der1[x]
    for x in range(0, i):
        somatorio2 += der1[x] * der1[x]
    index1.append(pow(somatorio1, 2)/(i*somatorio2))
print(index1)
index2 = []
for i in range(1, 8):
    somatorio1 = 0
    somatorio2 = 0
    for x in range(0, i):
        somatorio1 += der2[x]
    for x in range(0, i):
        somatorio2 += der2[x] * der2[x]
    index2.append(pow(somatorio1, 2)/(i*somatorio2))
print(index2)
index3 = []
for i in range(1, 8):
    somatorio1 = 0
    somatorio2 = 0
    for x in range(0, i):
        somatorio1 += der3[x]
    for x in range(0, i):
        somatorio2 += der3[x] * der3[x]
    index3.append(pow(somatorio1, 2)/(i*somatorio2))
print(index3)
index4 = []
for i in range(1, 8):
    somatorio1 = 0
    somatorio2 = 0
    for x in range(0, i):
        somatorio1 += der4[x]
    for x in range(0, i):
        somatorio2 += der4[x] * der4[x]
    index4.append(pow(somatorio1, 2)/(i*somatorio2))
print(index4)
fig0 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, index0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, index1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, index2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, index3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, index4, label='ADR', linestyle='--', marker="d")

#pdf = matplotlib.backends.backend_pdf.PdfPages('DER-Comparation.pdf')
#plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize = 19)
#plt.xticks([100, 250, 500, 750, 1000, 2000, 3000], fontsize = 19)
plt.ylabel("Indice", fontsize=20)
plt.xlabel("Número de Dispositivos", fontsize=20)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0.,fontsize = 'x-large',markerscale=2,handletextpad=0.05)
plt.xlim(0)
plt.grid()
plt.savefig('INDICES-Comparation.pdf')

collision0 = df0['Collision'].tolist()
collision1 = df1['Collision'].tolist()
collision2 = df2['Collision'].tolist()
collision3 = df3['Collision'].tolist()
collision4 = df4['Collision'].tolist()

energy0 = df0['OverallEnergy'].tolist()
energy1 = df1['OverallEnergy'].tolist()
energy2 = df2['OverallEnergy'].tolist()
energy3 = df3['OverallEnergy'].tolist()
energy4 = df4['OverallEnergy'].tolist()

fig1 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, der0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, der1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, der2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, der3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, der4, label='ADR', linestyle='--', marker="d")

#pdf = matplotlib.backends.backend_pdf.PdfPages('DER-Comparation.pdf')
plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize = 19)
plt.xticks(fontsize = 19)
plt.ylabel("DER", fontsize=20)
plt.xlabel("Número de Dispositivos", fontsize=20)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0.,fontsize = 'x-large',markerscale=2,handletextpad=0.05)
plt.ylim((0.3, 1.02))
plt.xlim(0)
plt.grid()
plt.savefig('DER-Comparation.pdf')

#plt.show()
#pdf.savefig(fig1)
#pdf.close()

fig2 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, collision0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, collision1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, collision2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, collision3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, collision4, label='ADR', linestyle='--', marker="d")

#pdf = matplotlib.backends.backend_pdf.PdfPages('Collisions-Comparation.pdf')
plt.ylabel("Número de Colisões", fontsize=20)
plt.xlabel("Número de Dispositivos", fontsize=20)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0.,fontsize = 'x-large',markerscale=2,handletextpad=0.05)
plt.xticks(fontsize = 18)
plt.gcf().subplots_adjust(left=0.15)
plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
plt.yticks(fontsize = 15)
plt.grid()
plt.xlim(0)
plt.savefig('Collisions-Comparation.pdf')
#plt.show()
#pdf.savefig(fig2)
#pdf.close()

fig3 = plt.figure(figsize=(10, 10))
plt.plot(node_numbers, energy0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, energy1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, energy2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, energy3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, energy4, label='ADR', linestyle='--', marker="d")

pdf = matplotlib.backends.backend_pdf.PdfPages('Energy-Comparation.pdf')
plt.ylabel("Consumo de Energia da Rede(mJ)", fontsize=20)
plt.xlabel("Número de Dispositivos", fontsize=20)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0.,fontsize = 'x-large',markerscale=2,handletextpad=0.05)
plt.xticks(fontsize = 18)
plt.gcf().subplots_adjust(left=0.15)
plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
plt.yticks(fontsize = 15)
plt.xlim(0)
plt.grid()
#plt.show()
pdf.savefig(fig3)


pdf.close()


