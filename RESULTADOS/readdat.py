import pandas as pd
import matplotlib.pyplot as plt
from pandas.compat import StringIO

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

fig1 = plt.figure(figsize=(20, 5))
plt.plot(node_numbers, der0, label='NAGIB', linestyle='--', marker='o')
plt.plot(node_numbers, der1, label='Random', linestyle='--', marker='^')
plt.plot(node_numbers, der2, label='Min_airtime', linestyle='--', marker='^')
plt.plot(node_numbers, der3, label='Equal-Distribution', linestyle='--', marker="D")

plt.ylabel("Data Extraction Rate")
plt.xlabel("Number of Nodes")
plt.legend()
plt.ylim((0, 1))
plt.show()
plt.savefig('DER-Comparation.pdf')

fig2 = plt.figure(figsize=(20, 5))
plt.plot(node_numbers, collision0, label='NAGIB', linestyle='--', marker='o')
plt.plot(node_numbers, collision1, label='Random', linestyle='--', marker='^')
plt.plot(node_numbers, collision2, label='Min_airtime', linestyle='--')
plt.plot(node_numbers, collision3, label='Equal-Distribution', linestyle='--', marker="D")

plt.ylabel("Number of Collisions")
plt.xlabel("Number of Nodes")
plt.legend()
plt.show()
plt.savefig('Collisions-Comparation.pdf')

fig3 = plt.figure(figsize=(20, 5))
plt.plot(node_numbers, energy0, label='NAGIB', linestyle='--', marker='o')
plt.plot(node_numbers, energy1, label='Random', linestyle='--', marker='^')
plt.plot(node_numbers, energy2, label='Min_airtime', linestyle='--')
plt.plot(node_numbers, energy3, label='Equal-Distribution', linestyle='--', marker="D")

plt.ylabel("Network Energy Consumption(mJ)")
plt.xlabel("Number of Nodes")
plt.legend()
plt.grid()
plt.show()
plt.savefig('Energy-Comparation.pdf')