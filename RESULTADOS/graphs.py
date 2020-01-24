import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

df0 = pd.read_csv('exp0_Nagib_16min.dat')
df1 = pd.read_csv('exp1_Random_16min.dat')
df2 = pd.read_csv('exp2_minairtime_16min.dat')
df3 = pd.read_csv('exp4_Equaldistr_16min.dat')
df4 = pd.read_csv('exp3_ADR_16min.dat')
df5 = pd.read_csv('exp6_Heuristic_16min.dat')
node_numbers = df1['Nodes'].tolist()


# Energy Comparation
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


energy0 = df0['OverallEnergy'].tolist()
energy1 = df1['OverallEnergy'].tolist()
energy2 = df2['OverallEnergy'].tolist()
energy3 = df3['OverallEnergy'].tolist()
energy4 = df4['OverallEnergy'].tolist()
energy5 = df5['OverallEnergy'].tolist()

fig3 = plt.figure(figsize=(17, 10))
plt.plot(node_numbers, energy1, label='Random', linestyle='--', marker='^')
plt.plot(node_numbers, energy2, label='Min_Airtime', linestyle='--', marker='h')
plt.plot(node_numbers, energy3, label='Equal_Distribution', linestyle='--', marker="D")
plt.plot(node_numbers, energy4, label='ADR', linestyle='--', marker="d")
plt.plot(node_numbers, energy5, label='Heuristica', linestyle='--', marker="P")

plt.ylabel("Overall Energy (mJ)", fontsize=26)
plt.xlabel("Number of Devices", fontsize=26)
plt.legend(prop=dict(size=12))
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0., fontsize=25, markerscale=2, handletextpad=0.1)
plt.xticks(fontsize=20)
plt.gcf().subplots_adjust(left=0.15)
plt.gca().yaxis.set_major_formatter(MathTextSciFormatter("%1.2e"))
plt.yticks(fontsize=20)
plt.xlim(0)
plt.grid()
plt.savefig('Energy-Comparation.pdf')


# Fairness Index
def NewMatrixTime(matrix, Tempo=None): # deve retornar um vetor de vetores
    NewMatrix = []
    if Tempo is None:
        Tempo = [56.57600000000001, 102.912, 185.344, 370.688, 741.376, 1318.912]
    for i in range(0, 7):
        NewMatrix.append([matrix.iat[i, 6] * Tempo[0], matrix.iat[i, 7] * Tempo[1], matrix.iat[i, 8] * Tempo[2], matrix.iat[i, 9] * Tempo[3], matrix.iat[i, 10] * Tempo[4], matrix.iat[i, 11] * Tempo[5]])
    return NewMatrix


def jfi(vetor):
    sum0 = 0
    sum1 = 0
    for i in range(0, 5):
        sum0 += vetor[i]
        sum1 += pow(vetor[i], 2)
    return pow(sum0, 2) / (6 * sum1)


rand = NewMatrixTime(df1)
minAir = NewMatrixTime(df2)
equal = NewMatrixTime(df3)
adr = NewMatrixTime(df4)
heuri = NewMatrixTime(df5)

JFI1 = [jfi(justice) for justice in rand]
JFI2 = [jfi(justice) for justice in minAir]
JFI3 = [jfi(justice) for justice in equal]
JFI4 = [jfi(justice) for justice in adr]
JFI5 = [jfi(justice) for justice in heuri]

fig0 = plt.figure(figsize=(17, 10))
plt.plot(node_numbers, JFI1, label='Random', linestyle='--', marker='^')
plt.plot(node_numbers, JFI2, label='Min_Airtime', linestyle='--', marker='h')
plt.plot(node_numbers, JFI3, label='Equal_Distribution', linestyle='--', marker="D")
plt.plot(node_numbers, JFI4, label='ADR', linestyle='--', marker="d")
plt.plot(node_numbers, JFI5, label='Heuristica', linestyle='--', marker="P")
plt.yticks([0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0], fontsize=24)
plt.xticks([100, 500, 1000, 2000, 3000], fontsize=24)
plt.ylabel("Fairness Index", fontsize=26)
plt.xlabel("Number of Devices", fontsize=26)
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
            ncol=6, mode="expand", borderaxespad=0.,fontsize = 25,markerscale=2,handletextpad=0.1)
plt.grid()
plt.savefig('Fairness_Comparation.pdf')

# SF Comparation Bar Graph
num_set = [{'SF7':1410, 'SF8':775, 'SF9':428, 'SF10':212, 'SF11':106, 'SF12':69},  # Heuristica
           {'SF7':400, 'SF8':456, 'SF9':560, 'SF10':586, 'SF11':480, 'SF12':518},  # Random
           {'SF7':3000, 'SF8':0, 'SF9':0, 'SF10':0, 'SF11':0, 'SF12':0},  # Min_Airtime
           {'SF7':500, 'SF8':500, 'SF9':500, 'SF10':500, 'SF11':500, 'SF12':500},  # Equal-Distribution
           {'SF7':3000, 'SF8':0, 'SF9':0, 'SF10':0, 'SF11':0, 'SF12':0}  # ADR
           ]  # Modificado manualmente

lan_guage = [['SF7','SF8','SF9', 'SF10', 'SF11', 'SF12'],
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

fig5 = plt.figure(figsize=(17, 10))
for name, pattern, color in zip(names, patterns, colors2):
    idx = np.where(orders == name)
    value = values[idx]
    left = lefts[idx]
    plt.bar(bottoms, height=value, width=0.8, bottom=left, hatch=pattern, orientation="vertical", label=name,
            facecolor=color, edgecolor='black')

plt.ylim(0, 3000)
plt.yticks([300, 600, 900, 1200, 1500, 1800, 2100, 2400, 2700,3000], ['10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%', '100%'], fontsize = 22)
plt.xticks(bottoms, ['Heuristica', 'Random', 'Min_Airtime', 'Equal_Distribution', 'ADR'], fontsize = 24)
plt.legend(bbox_to_anchor=(0., 1.01, 1., .202), loc=3,
           ncol=6, mode="expand", borderaxespad=0,fontsize = 25,markerscale=3,handletextpad=0.18)
plt.savefig('SF-Bar_Comparation.pdf')