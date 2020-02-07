import simpy
import random
from LoraSim.utils.check_colisions import checkcollision


#
# main discrete event loop, runs for each node
# a global list of packet being processed at the gateway
# is maintained
#
def transmit(env, node, packetsAtBS, lostPackets, packetsRecBS, nrNetworks, collidedPackets, recPackets):
    while True:
        # time before sending anything (include prop delay)
        # send up to 2 seconds earlier or later
        yield env.timeout(random.expovariate(1.0 / float(node.period)))

        # time sending and receiving
        # packet arrives -> add to base station

        node.sent = node.sent + 1

        global packetSeq
        packetSeq = packetSeq + 1

        global nrBS
        for bs in range(0, nrBS):
            if node in packetsAtBS[bs]:
                print("ERROR: packet already in")
            else:
                # adding packet if no collision
                if checkcollision(node.packet[bs]) == 1:
                    node.packet[bs].collided = 1
                    global nrCollisions
                    nrCollisions = nrCollisions + 1

                else:
                    node.packet[bs].collided = 0
                packetsAtBS[bs].append(node)
                node.packet[bs].addTime = env.now
                node.packet[bs].seqNr = packetSeq

        # take first packet rectime
        yield env.timeout(node.packet[0].rectime)

        # if packet did not collide, add it in list of received packets
        # unless it is already in
        for bs in range(0, nrBS):
            if node.packet[bs].lost:
                lostPackets.append(node.packet[bs].seqNr)
            else:
                if node.packet[bs].collided == 0:
                    if nrNetworks == 1:
                        packetsRecBS[bs].append(node.packet[bs].seqNr)
                    else:
                        # now need to check for right BS
                        if node.bs.id == bs:
                            packetsRecBS[bs].append(node.packet[bs].seqNr)
                    # recPackets is a global list of received packets
                    # not updated for multiple networks
                    if recPackets:
                        if recPackets[-1] != node.packet[bs].seqNr:
                            recPackets.append(node.packet[bs].seqNr)
                    else:
                        recPackets.append(node.packet[bs].seqNr)
                else:
                    # XXX only for debugging
                    collidedPackets.append(node.packet[bs].seqNr)

        # complete packet has been received by base station
        # can remove it

        for bs in range(0, nrBS):
            if node in packetsAtBS[bs]:
                packetsAtBS[bs].remove(node)
                # reset the packet
                node.packet[bs].collided = 0
                node.packet[bs].processed = 0