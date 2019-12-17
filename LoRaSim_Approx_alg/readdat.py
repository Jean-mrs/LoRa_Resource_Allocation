import pandas as pd
import matplotlib.pyplot as plt
from pandas.compat import StringIO

df0 = pd.read_csv('exp0d99BS1Intf_NAGIB.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions'],
                 header=0)
df0.columns = ['Nodes', 'DER', 'Collision']
print(df0)

df1 = pd.read_csv('exp1d99BS1Intf_RANDOM.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions'],
                 header=0)
df1.columns = ['Nodes', 'DER', 'Collision']
print(df1)

df2 = pd.read_csv('exp4d99BS1Intf_APPROX-ALG.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions'],
                 header=0)
df2.columns = ['Nodes', 'DER', 'Collision']
print(df2)

df3 = pd.read_csv('exp4d99BS1Intf_EQUAL-DISTRIBUTION.dat',
                 sep="\s+",
                 names=['Nodes', 'DER0', 'Collisions'],
                 header=0)
df3.columns = ['Nodes', 'DER', 'Collision']
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

fig1 = plt.figure(figsize=(20, 5))
plt.plot(node_numbers, der0)
plt.plot(node_numbers, der1)
plt.plot(node_numbers, der2)
plt.plot(node_numbers, der3)

plt.ylabel("Data Extraction Rate")
plt.xlabel("Number of Nodes")
plt.ylim((0, 1))
plt.show()

fig2 = plt.figure(figsize=(20, 5))
plt.plot(node_numbers, collision0)
plt.plot(node_numbers, collision1)
plt.plot(node_numbers, collision2)
plt.plot(node_numbers, collision3)

plt.ylabel("Number of Collisions")
plt.xlabel("Number of Nodes")
plt.show()