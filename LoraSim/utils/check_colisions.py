import numpy as np
import simpy

collisionsvector = np.zeros((4,), dtype=int)


#
# check for collisions at base station
# Note: called before a packet (or rather node) is inserted into the list
def checkcollision(packet, full_collision, packetsAtBS):
    col = 0  # flag needed since there might be several collisions for packet
    # lost packets don't collide
    if packet.lost:
        return 0
    if packetsAtBS[packet.bs]:
        for other in packetsAtBS[packet.bs]:
            if other.id != packet.nodeid:
                # simple collision
                if frequencyCollision(packet, other.packet[packet.bs]) and sfCollision(packet, other.packet[packet.bs]):
                    if full_collision:
                        if timingCollision(packet, other.packet[packet.bs]):
                            # check who collides in the power domain
                            c = powerCollision(packet, other.packet[packet.bs])
                            # mark all the collided packets
                            # either this one, the other one, or both
                            for p in c:
                                p.collided = 1
                                if p == packet:
                                    col = 1
                        else:
                            # no timing collision, all fine
                            pass
                    else:
                        packet.collided = 1
                        other.packet[packet.bs].collided = 1  # other also got lost, if it wasn't lost already
                        col = 1
        return col
    return 0


#
# frequencyCollision, conditions
#
#        |f1-f2| <= 120 kHz if f1 or f2 has bw 500
#        |f1-f2| <= 60 kHz if f1 or f2 has bw 250
#        |f1-f2| <= 30 kHz if f1 or f2 has bw 125
def frequencyCollision(p1, p2):
    if abs(p1.freq - p2.freq) <= 120 and (p1.bw == 500 or p2.bw == 500):
        collisionsvector[0] += 1
        return True
    elif abs(p1.freq - p2.freq) <= 60 and (p1.bw == 250 or p2.bw == 250):
        collisionsvector[0] += 1
        return True
    else:
        if abs(p1.freq - p2.freq) <= 30:
            collisionsvector[0] += 1
            return True
    return False


def sfCollision(p1, p2):
    if p1.sf == p2.sf:
        # p2 may have been lost too, will be marked by other checks
        collisionsvector[1] += 1
        return True
    return False


def powerCollision(p1, p2):
    powerThreshold = 6  # dB
    if abs(p1.rssi - p2.rssi) < powerThreshold:
        # packets are too close to each other, both collide
        # return both packets as casualties
        collisionsvector[2] += 1
        return (p1, p2)
    elif p1.rssi - p2.rssi < powerThreshold:
        # p2 overpowered p1, return p1 as casualty
        collisionsvector[2] += 1
        return (p1,)
    # p2 was the weaker packet, return it as a casualty
    return (p2,)


def timingCollision(p1, p2):
    # assuming p1 is the freshly arrived packet and this is the last check
    # we've already determined that p1 is a weak packet, so the only
    # way we can win is by being late enough (only the first n - 5 preamble symbols overlap)

    # assuming 8 preamble symbols
    Npream = 8

    # we can lose at most (Npream - 5) * Tsym of our preamble
    Tpreamb = 2 ** p1.sf / (1.0 * p1.bw) * (Npream - 5)

    # check whether p2 ends in p1's critical section
    p2_end = p2.addTime + p2.rectime
    p1_cs = env.now + Tpreamb
    if p1_cs < p2_end:
        # p1 collided with p2 and lost
        collisionsvector[3] += 1
        return True
    return False

