import numpy as np


#
#   update RSSI depending on direction
#
def updateRSSI(self, dir_30, dir_90, dir_150, dir_180):
    global bs

    #print "+++++++++uR node", self.id, " and bs ", self.bs.id
    #print "node x,y", self.x, self.y
    #print "main-bs x,y", bs[self.bs.id].x, bs[self.bs.id].y
    for i in range(0,len(self.packet)):
        #print "rssi before", self.packet[i].rssi
        #print "packet bs", self.packet[i].bs
        #print "packet bs x, y:", bs[self.packet[i].bs].x, bs[self.packet[i].bs].y
        if (self.bs.id == self.packet[i].bs):
            #print "packet to main bs, increase rssi "
            self.packet[i].rssi = self.packet[i].rssi + dir_30
        else:
            b1 = np.array([bs[self.bs.id].x, bs[self.bs.id].y])
            p = np.array([self.x, self.y])
            b2 = np.array([bs[self.packet[i].bs].x, bs[self.packet[i].bs].y])

            ba = b1 - p
            bc = b2 - p
            #print ba
            #print bc

            cosine_angle = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc))
            angle = np.degrees(np.arccos(cosine_angle))

            #print "angle: ", angle

            if (angle <= 30):
                #print "rssi increase to other BS: 4"
                self.packet[i].rssi = self.packet[i].rssi + dir_30
            elif angle <= 90:
                #print "rssi increase to other BS: 2"
                self.packet[i].rssi = self.packet[i].rssi + dir_90
            elif angle <= 150:
                #print "rssi increase to other BS: -4"
                self.packet[i].rssi = self.packet[i].rssi + dir_150
            else:
                #print "rssi increase to other BS: -3"
                self.packet[i].rssi = self.packet[i].rssi + dir_180
        #print "packet rssi after", self.packet[i].rssi

