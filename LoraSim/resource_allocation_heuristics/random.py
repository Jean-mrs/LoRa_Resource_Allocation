import math
import random
from LoraSim.utils.airtime import airtime

#
# this function creates a packet (associated with a node)
# it also sets all parameters, currently random
#
class RandomPacket():
    def __init__(self, nodeid, plen, distance, bs, bsHeight, deviceHeight, Ptx, GL, minsensi, sf7count, sf8count, sf9count, sf10count, sf11count, sf12count):

        # new: base station ID
        self.bs = bs
        self.nodeid = nodeid

        # for certain experiments override these
        # RANDOM
        self.sf = random.randint(7, 12)
        self.cr = 1
        self.bw = 125
        self.freq = random.choice(
            [903900000, 904100000, 904300000, 904500000, 904700000, 904900000, 905100000, 905300000])

        Prx = Ptx  ## zero path loss by default
        # log-shadow
        # Lpl = Lpld0 + 10*gamma*math.log10(distance/d0)
        Lpl = 69.55 + 26.16 * math.log10(self.freq / 1000000) - 13.82 * math.log10(bsHeight) - (
                3.2 * math.pow(math.log10(11.75 * deviceHeight), 2) - 4.97) + (
                      44.9 - 6.55 * math.log10(bsHeight)) * math.log10(distance * 0.001)

        # print Lpl
        Prx = Ptx + GL - Lpl

        # transmission range, needs update XXX
        self.transRange = 150
        self.pl = plen
        self.symTime = (2.0 ** self.sf) / self.bw
        self.arriveTime = 0
        self.rssi = Prx

        self.rectime = airtime(self.sf, self.cr, self.pl, self.bw)
        # denote if packet is collided
        self.collided = 0
        self.processed = 0
        # mark the packet as lost when it's rssi is below the sensitivity
        # don't do this for experiment 3, as it requires a bit more work
        # global minsensi
        self.lost = self.rssi < minsensi
        # print "node {} bs {} lost {}".format(self.nodeid, self.bs, self.lost)

        if self.sf == 7:
            sf7count += 1
        if self.sf == 8:
            sf8count += 1
        if self.sf == 9:
            sf9count += 1
        if self.sf == 10:
            sf10count += 1
        if self.sf == 11:
            sf11count += 1
        if self.sf == 12:
            sf12count += 1

#
# main discrete event loop, runs for each node
# a global list of packet being processed at the gateway
# is maintained
#