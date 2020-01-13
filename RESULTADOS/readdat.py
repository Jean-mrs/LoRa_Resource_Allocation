import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import matplotlib.ticker as mticker
import numpy as np

#
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


df0 = pd.read_csv('exp0_Nagib_5min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12'],
                 header=0)
df0.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12']
print(df0)

df1 = pd.read_csv('exp1_Random_5min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12'],
                 header=0)
df1.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12']
print(df1)

df2 = pd.read_csv('exp2_minairtime_5min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12'],
                 header=0)
df2.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12']
print(df2)

df3 = pd.read_csv('exp4_Equaldistr_5min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12'],
                 header=0)
df3.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12']
print(df3)

df4 = pd.read_csv('exp3_ADR_5min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12'],
                 header=0)
df4.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12']
print(df4)
df5 = pd.read_csv('exp6_Heuristic_5min.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12'],
                 header=0)
df5.columns = ['Nodes', 'DER', 'Collision', 'OverallEnergy', 'Delay','STD_delay', 'SF7',   'SF8',  'SF9',  'SF10',  'SF11',  'SF12']
print(df5)

node_numbers = df1['Nodes'].tolist()
der0 = df0['DER'].tolist()
der1 = df1['DER'].tolist()
der2 = df2['DER'].tolist()
der3 = df3['DER'].tolist()
der4 = df4['DER'].tolist()
der5 = df5['DER'].tolist()
import scipy.stats
from pylab import *

def NewVetorTime(Vetor, Tempo):
    NewVector = [Vetor["SF7"].max() * Tempo[0], Vetor["SF8"].max() * Tempo[1], Vetor["SF9"].max() * Tempo[2], Vetor["SF10"].max() * Tempo[3], Vetor["SF11"].max() * Tempo[4], Vetor["SF12"].max() * Tempo[5]]
    return NewVector


def jfi(vetor):
    sum0 = 0
    sum1 = 0
    for i in range(0, 5):
        sum0 += vetor[i]
        sum1 += pow(vetor[i], 2)
    return pow(sum0, 2) / (6 * sum1)


AirTime = [56.57600000000001, 102.912, 185.344, 370.688, 741.376, 1318.912]

nagib = NewVetorTime(df1, AirTime)
rand = NewVetorTime(df2, AirTime)
minAir = NewVetorTime(df3, AirTime)
adr = NewVetorTime(df4, AirTime)
igual = NewVetorTime(df5, AirTime)

JFI = [0, 0, 0, 0, 0]
JFI[0] = jfi(nagib)
JFI[1] = jfi(rand)
JFI[2] = jfi(minAir)
JFI[3] = jfi(adr)
JFI[4] = jfi(igual)
print(JFI)

# fig0 = plt.figure(figsize=(17, 10))
# plt.plot(node_numbers, index0, label='MARCO', linestyle='--', marker='o')
# plt.plot(node_numbers, index1, label='Aleatório', linestyle='--', marker='^')
# plt.plot(node_numbers, index2, label='Menor_Tempo', linestyle='--', marker='h')
# plt.plot(node_numbers, index3, label='Distro_Justo', linestyle='--', marker="D")
# plt.plot(node_numbers, index4, label='ADR', linestyle='--', marker="d")
#
# #pdf = matplotlib.backends.backend_pdf.PdfPages('DER-Comparation.pdf')
# #plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize = 19)
# #plt.xticks([100, 250, 500, 750, 1000, 2000, 3000], fontsize = 19)
# plt.ylabel("Indice", fontsize=26)
# plt.xlabel("Número de Dispositivos", fontsize=26)
# #plt.legend(prop=dict(size=12))
# plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
#            ncol=6, mode="expand", borderaxespad=0.,fontsize = 25,markerscale=2,handletextpad=0.1)
# plt.xlim(0)
# plt.grid()
# plt.savefig('INDICES-Comparation.pdf')

collision0 = df0['Collision'].tolist()
collision1 = df1['Collision'].tolist()
collision2 = df2['Collision'].tolist()
collision3 = df3['Collision'].tolist()
collision4 = df4['Collision'].tolist()
collision5 = df5['Collision'].tolist()

energy0 = df0['OverallEnergy'].tolist()
energy1 = df1['OverallEnergy'].tolist()
energy2 = df2['OverallEnergy'].tolist()
energy3 = df3['OverallEnergy'].tolist()
energy4 = df4['OverallEnergy'].tolist()
energy5 = df5['OverallEnergy'].tolist()

fig1 = plt.figure(figsize=(17, 10))
plt.plot(node_numbers, der0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, der1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, der2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, der3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, der4, label='ADR', linestyle='--', marker="d")
plt.plot(node_numbers, der5, label='Heuristica', linestyle='--', marker="P", color='yellow')

#pdf = matplotlib.backends.backend_pdf.PdfPages('DER-Comparation.pdf')
plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize = 24)
plt.xticks(fontsize = 24)
plt.ylabel("DER", fontsize=26)
plt.xlabel("Número de Dispositivos", fontsize=26)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0., fontsize=25, markerscale=2, handletextpad=0.1)
plt.ylim((0.3, 1.02))
plt.xlim(0)
plt.grid()
plt.savefig('DER-Comparation')

#plt.show()
#pdf.savefig(fig1)
#pdf.close()

fig2 = plt.figure(figsize=(17, 10))
plt.plot(node_numbers, collision0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, collision1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, collision2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, collision3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, collision4, label='ADR', linestyle='--', marker="d")
plt.plot(node_numbers, collision5, label='Heuristica', linestyle='--', marker="P", color='yellow')

#pdf = matplotlib.backends.backend_pdf.PdfPages('Collisions-Comparation.pdf')
plt.ylabel("Número de Colisões", fontsize=24)
plt.xlabel("Número de Dispositivos", fontsize=24)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0.,fontsize = 25,markerscale=2,handletextpad=0.1)
plt.xticks(fontsize = 24)
plt.gcf().subplots_adjust(left=0.15)
plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
plt.yticks(fontsize = 24)
plt.grid()
plt.xlim(0)
plt.savefig('Collisions-Comparation')
#plt.show()
#pdf.savefig(fig2)
#pdf.close()

fig3 = plt.figure(figsize=(17, 10))
plt.plot(node_numbers, energy0, label='MARCO', linestyle='--', marker='o')
plt.plot(node_numbers, energy1, label='Aleatório', linestyle='--', marker='^')
plt.plot(node_numbers, energy2, label='Menor_Tempo', linestyle='--', marker='h')
plt.plot(node_numbers, energy3, label='Distro_Justo', linestyle='--', marker="D")
plt.plot(node_numbers, energy4, label='ADR', linestyle='--', marker="d")
plt.plot(node_numbers, energy5, label='Heuristica', linestyle='--', marker="P", color='yellow')

#pdf = matplotlib.backends.backend_pdf.PdfPages('Energy-Comparation.pdf')
plt.ylabel("Consumo de Energia da Rede(mJ)", fontsize=26)
plt.xlabel("Número de Dispositivos", fontsize=26)
plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0., fontsize=25, markerscale=2, handletextpad=0.1)
plt.xticks(fontsize = 20)
plt.gcf().subplots_adjust(left=0.15)
plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
plt.yticks(fontsize = 20)
plt.xlim(0)
plt.grid()
#plt.show()
plt.savefig('Energy-Comparation')

delay0 = df0['Delay'].tolist()
delay1 = df1['Delay'].tolist()
delay2 = df2['Delay'].tolist()
delay3 = df3['Delay'].tolist()
delay4 = df4['Delay'].tolist()
delay5 = df5['Delay'].tolist()
stddelay0 = df0['STD_delay'].tolist()
stddelay1 = df1['STD_delay'].tolist()
stddelay2 = df2['STD_delay'].tolist()
stddelay3 = df3['STD_delay'].tolist()
stddelay4 = df4['STD_delay'].tolist()

fig4 = plt.figure(figsize=(17, 10))
#fig4 = plt.figure(figsize=(15, 10))
plt.plot(node_numbers, delay0, label='MARCO', linestyle='--', marker='o')
#plt.errorbar(node_numbers, delay0, stddelay0, linestyle='None', color='blue')
plt.plot(node_numbers, delay1, label='Aleatório', linestyle='--', marker='^')
#plt.errorbar(node_numbers, delay1, stddelay1, linestyle='None', color='green')
plt.plot(node_numbers, delay2, label='Menor_Tempo', linestyle='--', marker='h')
#plt.errorbar(node_numbers, delay2, stddelay2, linestyle='None', color='red')
plt.plot(node_numbers, delay3, label='Distro_Justo', linestyle='--', marker="D")
#plt.errorbar(node_numbers, delay3, stddelay3, linestyle='None', color='purple')
plt.plot(node_numbers, delay4, label='ADR', linestyle='--', marker="d")
#plt.errorbar(node_numbers, delay4, stddelay4, linestyle='None', color='brown')
plt.plot(node_numbers, delay5, label='Heuristica', linestyle='--', marker="P", color='yellow')

#plt.yticks([0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize = 19)
#plt.xticks([100, 250, 500, 750, 1000, 2000, 3000], fontsize = 19)
plt.yticks(fontsize = 22)
plt.xticks(fontsize = 22)
plt.ylabel("ToA(s)", fontsize=24)
plt.xlabel("Número de Dispositivos", fontsize=26)
#plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0.,fontsize=25,markerscale=2,handletextpad=0.1)
plt.xlim(0)
plt.grid()
plt.savefig('ToA-Comparation')




# initialise data of lists.
# data = {'Modelo': ['MARCO', 'Aleatório', 'Menor_Tempo', 'Distro_Justo', 'ADR'],
#         'SF7': [1410, 522, 3000, 500, 3000],
#         'SF8': [774, 495, 0, 500, 0],
#         'SF9': [429, 488, 0, 500, 0],
#         'SF10': [213, 515, 0, 500, 0],
#         'SF11': [106, 477, 0, 500, 0],
#         'SF12': [68, 503, 0, 500, 0]}
# # Creates pandas DataFrame.
# df = pd.DataFrame(data)

num_set = [{'SF7':1410, 'SF8':774, 'SF9':429, 'SF10':213, 'SF11':106, 'SF12':68},
           {'SF7':400, 'SF8':456, 'SF9':560, 'SF10':586, 'SF11':480, 'SF12':518},
           {'SF7':3000, 'SF8':0, 'SF9':0, 'SF10':0, 'SF11':0, 'SF12':0},
           {'SF7':500, 'SF8':500, 'SF9':500, 'SF10':500, 'SF11':500, 'SF12':500},
           {'SF7':3000, 'SF8':0, 'SF9':0, 'SF10':0, 'SF11':0, 'SF12':0}
           ]

lan_guage    = [['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'],
               ['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'],
               ['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'],
                ['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'],
                ['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12']]

patterns = [ "\\" , "|" , "/" , "+" , "-", "x"]
colors2 = ["#dfe6e9",  "#b2bec3","#636e72", "#2d3436", "#262936", "#24252C"]
colors = ["#2f3640", "#2d3436", "#636e72", "#b2bec3", "#dfe6e9", '#6785b7']
names = ['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12']


values = np.array([[data[name] for name in order] for data,order in zip(num_set, lan_guage)])
lefts = np.insert(np.cumsum(values, axis=1),0,0, axis=1)[:, :-1]
orders = np.array(lan_guage)
bottoms = np.arange(5)
print(values)
print(bottoms)
print(lefts)

#fig5 = plt.figure(figsize=(13, 10))
fig5 = plt.figure(figsize=(17, 10))
cont = 0
for name, pattern, color in zip(names, patterns, colors2):
    idx = np.where(orders == name)
    value = values[idx]
    left = lefts[idx]
    #plt.bar(x=bottoms, height=0.8, width=value, bottom=bottoms, hatch=pattern, orientation="horizontal", label=name, color='white', edgecolor='black')
    plt.bar(bottoms, height=value, width=0.8, bottom=left, hatch=pattern, orientation="vertical", label=name,
            facecolor=color, edgecolor='black')
    cont +=1

plt.ylim(0, 3000)
plt.yticks([300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700,3000], ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'], fontsize = 22)
plt.xticks(bottoms, ['MARCO', 'Aleatório', 'Menor_Tempo', 'Distro_Justo', 'ADR'], fontsize = 24)
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0,fontsize = 25,markerscale=3,handletextpad=0.18)
#plt.subplots_adjust(right=0.75)
# Turn on the grid
#plt.minorticks_on()
#plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
#plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.savefig('SF-Comparation.pdf')

