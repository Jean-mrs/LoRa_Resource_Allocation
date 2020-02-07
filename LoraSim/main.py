import simpy
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

from LoraSim.utils.node import myNode
from LoraSim.utils.transmit_packet import transmit
from LoraSim.utils.base_station import myBS
from LoraSim.utils.update_rssi import updateRSSI

# turn on/off graphics
graphics = 0

# do the full collision check
full_collision = True

# CF values
CF1 = 903900000
CF2 = 904100000
CF3 = 904300000
CF4 = 904500000
CF5 = 904700000
CF6 = 904900000
CF7 = 905100000
CF8 = 905300000

nrNodes = 0
avgSendTime = 100000
#experiment = int(sys.argv[3])
simtime = 99999999999999
nrBS = 1
directionality = False
nrNetworks = 1
baseDist = 9999999


# RSSI global values for antenna
dir_30 = 4
dir_90 = 2
dir_150 = -4
dir_180 = -3
#dir_30 = 8
#dir_90 = 4
#dir_150 = -8
#dir_180 = -6

# global stuff
nodes = []
packetsAtBS = []
env = simpy.Environment()

# Import Data
data = pd.read_csv("3000nodes.csv")

# max distance: 300m in city, 3000 m outside (5 km Utz experiment)
# also more unit-disc like according to Utz
nrCollisions = 0
nrReceived = 0
nrProcessed = 0

# global value of packet sequence numbers
packetSeq = 0

# list of received packets
recPackets = []
collidedPackets = []
lostPackets = []

sf7count = 0
sf8count = 0
sf9count = 0
sf10count = 0
sf11count = 0
sf12count = 0

Ptx = 14
gamma = 2.08
d0 = 40.0
var = 0  # variance ignored for now
Lpld0 = 127.41
GL = 2

# this is an array with measured values for sensitivity
# see paper, Table 3
sf7 = np.array(  [7, -125, -124.25, -120.75])
sf8 = np.array(  [8, -128, -126.75, -124.0])
sf9 = np.array(  [9, -131, -128.25, -127.5])
sf10 = np.array([10, -134, -130.25, -128.75])
sf11 = np.array([11, -136, -132.75, -128.75])
sf12 = np.array([12, -137, -132.25, -132.25])
sensi = np.array([sf7, sf8, sf9, sf10, sf11, sf12])

## figure out the minimal sensitivity for the given experiment
minsensi = -200.0
if experiment in [0, 1, 4]:
    minsensi = sensi[5, 2]  # 5th row is SF12, 2nd column is BW125
elif experiment == 2:
    minsensi = -112.0  # no experiments, so value from datasheet
elif experiment == 3 or experiment == 5:
    minsensi = np.amin(sensi)  ## Experiment 3 can use any setting, so take minimum

Lpl = Ptx - minsensi
# print "amin", minsensi, "Lpl", Lpl
maxDist = 0
# print "maxDist:", maxDist

# size of area
xmax = maxDist * (nrBS + 2) + 20
ymax = maxDist * (nrBS + 1) + 20

# maximum number of packets the BS can receive at the same time
maxBSReceives = 8

maxX = maxDist + baseDist * (nrBS)
# print "maxX ", maxX
maxY = 0
# print "maxY", maxY

# prepare graphics and add sink
ax = 0
if graphics == 1:
    plt.ion()
    plt.figure()
    ax = plt.gcf().gca()

# list of base stations
bs = []

# list of packets at each base station, init with 0 packets
packetsAtBS = []
packetsRecBS = []
for i in range(0, nrBS):
    b = myBS(i)
    bs.append(b)
    packetsAtBS.append([])
    packetsRecBS.append([])

for i in range(0, nrNodes):
    # myNode takes period (in ms), base station id packetlen (in Bytes)
    # 1000000 = 16 min
    for j in range(0, nrBS):
        # create nrNodes for each base station
        node = myNode(i * nrBS + j, avgSendTime, 20, data.iat[i, 0], data.iat[i, 1], bs[j], graphics, nrBS, nodes, bs, ax)
        nodes.append(node)

        # when we add directionality, we update the RSSI here
        if (directionality == 1):
            node.updateRSSI()
        env.process(transmit(env, node, packetsAtBS, lostPackets, packetsRecBS, nrNetworks, collidedPackets, recPackets))

# prepare show
if (graphics == 1):
    plt.xlim([0, maxX + 50])
    plt.ylim([0, maxX + 50])
    plt.draw()
    plt.show()

# store nodes and basestation locations
with open('nodes.txt', 'w') as nfile:
    for node in nodes:
        nfile.write('{x} {y} {id}\n'.format(**vars(node)))

with open('basestation.txt', 'w') as bfile:
    for basestation in bs:
        bfile.write('{x} {y} {id}\n'.format(**vars(basestation)))

# start simulation
env.run(until=simtime)

# print stats and save into file
# print "nr received packets (independent of right base station)", len(recPackets)
# print "nr collided packets", len(collidedPackets)
# print "nr lost packets (not correct)", len(lostPackets)

sum = 0
for i in range(0, nrBS):
    # print "packets at BS",i, ":", len(packetsRecBS[i])
    sum = sum + len(packetsRecBS[i])
# print "sent packets: ", packetSeq
# print "overall received at right BS: ", sum

sumSent = 0
sent = []
for i in range(0, nrBS):
    sent.append(0)
for i in range(0, nrNodes * nrBS):
    sumSent = sumSent + nodes[i].sent
    # print "id for node ", nodes[i].id, "BS:", nodes[i].bs.id, " sent: ", nodes[i].sent
    sent[nodes[i].bs.id] = sent[nodes[i].bs.id] + nodes[i].sent
for i in range(0, nrBS):
    print("send to BS[", i, "]:", sent[i])

# print "sumSent: ", sumSent

der = []
# data extraction rate
derALL = len(recPackets) / float(sumSent)
sumder = 0
for i in range(0, nrBS):
    der.append(len(packetsRecBS[i]) / float(sent[i]))
    # print "DER BS[",i,"]:", der[i]
    sumder = sumder + der[i]
avgDER = (sumder) / nrBS
# print "avg DER: ", avgDER

TX = [22, 22, 22, 23,  # RFO/PA0: -2..1
      24, 24, 24, 25, 25, 25, 25, 26, 31, 32, 34, 35, 44,  # PA_BOOST/PA1: 2..14
      82, 85, 90,  # PA_BOOST/PA1: 15..17
      105, 115, 125]  # PA_BOOST/PA1+PA2: 18..20
mA = 44  # current draw for TX = 14 dBm
V = 3.0  # voltage XXX
# sent = sum(n.sent for n in nodes)
energy = 0.0
rectim = 0
time = []
for i in range(0, nrNodes):
    for n in range(0, len(nodes[i].packet)):
        rectim = rectim + nodes[i].packet[n].rectime
    rectim = rectim / len(nodes[i].packet)
    time.append(rectim)
    energy = (energy + rectim * mA * V * nodes[i].sent) / 1000.0
print('time:', len(time))

delay = np.mean(time)
std_delay = np.std(time)

# this can be done to keep graphics visible
# if (graphics == 1):
#     raw_input('Press Enter to continue ...')

# save experiment data into a dat file that can be read by e.g. gnuplot
# name of file would be:  exp0.dat for experiment 0/
# fname = "exp" + str(experiment) + "d99" + "BS" + str(nrBS) + "IntfAAAA.dat"
fname = "exp" + str(experiment) + "_ADR_16min.dat"
print(fname)
if os.path.isfile(fname):
    res = "\n" + str(nrNodes) + " " + str(avgDER) + " " + str(nrCollisions) + " " + str(energy) + " " + str(
        delay) + " " + str(std_delay) + " " + str(sf7count) + " " + str(sf8count) + " " + str(sf9count) + " " + str(
        sf10count) + " " + str(sf11count) + " " + str(sf12count) + " / " + str(collisionsvector[0]) + " " + str(
        collisionsvector[1]) + " " + str(collisionsvector[2]) + " " + str(collisionsvector[3])
else:
    res = "Nodes            DER0                         Collisions  OverallEnergy             Delay         SF7   SF8  SF9  SF10  SF11  SF12    FreqColli    SFColli    PowerColli    TimingColli\n" + str(
        nrNodes) + " " + str(avgDER) + " " + str(nrCollisions) + " " + str(energy) + " " + str(delay) + " " + str(
        sf7count) + " " + str(sf8count) + " " + str(sf9count) + " " + str(sf10count) + " " + str(
        sf11count) + " " + str(sf12count) + "  / " + str(collisionsvector[0]) + " " + str(
        collisionsvector[1]) + " " + str(collisionsvector[2]) + " " + str(collisionsvector[3])
with open(fname, "a") as myfile:
    myfile.write(res)
myfile.close()