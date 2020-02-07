import simpy
import random
import numpy as np
import matplotlib.pyplot as plt
from LoraSim.resource_allocation_heuristics.random import myPacket

#
# this function creates a node
#
class myNode():
    def __init__(self, id, period, packetlen, x, y, myBS, graphics, nrBS, nodes, bs, ax, maxX, maxY):
        self.bs = myBS
        self.id = id
        self.period = period

        self.x = 0
        self.y = 0
        self.packet = []
        self.dist = []
        # this is very complex prodecure for placing nodes
        # and ensure minimum distance between each pair of nodes
        found = 0
        rounds = 0
        while (found == 0 and rounds < 100):
            a = random.random()
            b = random.random()
            if b < a:
                a, b = b, a
            posx = x
            posy = y
            if len(nodes) > 0:
                for index, n in enumerate(nodes):
                    dist = np.sqrt(((abs(n.x - posx)) ** 2) + ((abs(n.y - posy)) ** 2))
                    # we set this so nodes can be placed everywhere
                    # otherwise there is a risk that little nodes are placed
                    # between the base stations where it would be more crowded
                    if dist >= 0:
                        found = 1
                        self.x = posx
                        self.y = posy
                    else:
                        rounds = rounds + 1
                        if rounds == 100:
                            # print "could not place new node, giving up"
                            exit(-2)
            else:
                # print "first node"
                self.x = posx
                self.y = posy
                found = 1

        # create "virtual" packet for each BS
        for i in range(0, nrBS):
            d = np.sqrt((self.x - bs[i].x) * (self.x - bs[i].x) + (self.y - bs[i].y) * (self.y - bs[i].y))
            if d == 0:  # Caso o device esteja em cima do Gateway
                d = 0.000000000001
            self.dist.append(d)
            self.packet.append(myPacket(self.id, packetlen, self.dist[i], i))
        # print('node %d' %id, "x", self.x, "y", self.y, "dist: ", self.dist, "my BS:", self.bs.id)

        self.sent = 0

        # graphics for node
        if (graphics == 1):
            if (self.bs.id == 0):
                ax.add_artist(plt.Circle((self.x, self.y), 2, fill=True, color='blue'))
            if (self.bs.id == 1):
                ax.add_artist(plt.Circle((self.x, self.y), 2, fill=True, color='red'))
            if (self.bs.id == 2):
                ax.add_artist(plt.Circle((self.x, self.y), 2, fill=True, color='green'))
            if (self.bs.id == 3):
                ax.add_artist(plt.Circle((self.x, self.y), 2, fill=True, color='brown'))
            if (self.bs.id == 4):
                ax.add_artist(plt.Circle((self.x, self.y), 2, fill=True, color='orange'))

    #
    #   update RSSI depending on direction
    #


    def updateRSSI(self, dir_30, dir_90, dir_150, dir_180):
        global bs

        # print "+++++++++uR node", self.id, " and bs ", self.bs.id
        # print "node x,y", self.x, self.y
        # print "main-bs x,y", bs[self.bs.id].x, bs[self.bs.id].y
        for i in range(0, len(self.packet)):
            # print "rssi before", self.packet[i].rssi
            # print "packet bs", self.packet[i].bs
            # print "packet bs x, y:", bs[self.packet[i].bs].x, bs[self.packet[i].bs].y
            if (self.bs.id == self.packet[i].bs):
                # print "packet to main bs, increase rssi "
                self.packet[i].rssi = self.packet[i].rssi + dir_30
            else:
                b1 = np.array([bs[self.bs.id].x, bs[self.bs.id].y])
                p = np.array([self.x, self.y])
                b2 = np.array([bs[self.packet[i].bs].x, bs[self.packet[i].bs].y])

                ba = b1 - p
                bc = b2 - p
                # print ba
                # print bc

                cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
                angle = np.degrees(np.arccos(cosine_angle))

                # print "angle: ", angle

                if (angle <= 30):
                    # print "rssi increase to other BS: 4"
                    self.packet[i].rssi = self.packet[i].rssi + dir_30
                elif angle <= 90:
                    # print "rssi increase to other BS: 2"
                    self.packet[i].rssi = self.packet[i].rssi + dir_90
                elif angle <= 150:
                    # print "rssi increase to other BS: -4"
                    self.packet[i].rssi = self.packet[i].rssi + dir_150
                else:
                    # print "rssi increase to other BS: -3"
                    self.packet[i].rssi = self.packet[i].rssi + dir_180
            # print "packet rssi after", self.packet[i].rssi

