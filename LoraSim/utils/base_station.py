import matplotlib.pyplot as plt


#
# this function creates a BS
#
class myBS():
    def __init__(self, id, graphics, nrBS, maxDist, maxX, maxY, baseDist, ax):
        self.id = id
        self.x = 0
        self.y = 0

        if (nrBS == 1 and self.id == 0):
            self.x = maxDist
            self.y = maxY

        if (nrBS == 2 and self.id == 0):
            self.x = maxDist
            self.y = maxY

        if (nrBS == 2 and self.id == 1):
            self.x = maxDist + baseDist
            self.y = maxY

        if (nrBS == 3 and self.id == 0):
            self.x = maxDist + baseDist
            self.y = maxY

        if (nrBS == 3 and self.id == 1):
            self.x = maxDist
            self.y = maxY

        if (nrBS == 3 and self.id == 2):
            self.x = maxDist + 2 * baseDist
            self.y = maxY

        if (nrBS == 4 and self.id == 0):
            self.x = maxDist + baseDist
            self.y = maxY

        if (nrBS == 4 and self.id == 1):
            self.x = maxDist
            self.y = maxY

        if (nrBS == 4 and self.id == 2):
            self.x = maxDist + 2 * baseDist
            self.y = maxY

        if (nrBS == 4 and self.id == 3):
            self.x = maxDist + baseDist
            self.y = maxY + baseDist

        if (nrBS == 5 and self.id == 0):
            self.x = maxDist + baseDist
            self.y = maxY + baseDist

        if (nrBS == 5 and self.id == 1):
            self.x = maxDist
            self.y = maxY + baseDist

        if (nrBS == 5 and self.id == 2):
            self.x = maxDist + 2 * baseDist
            self.y = maxY + baseDist

        if (nrBS == 5 and self.id == 3):
            self.x = maxDist + baseDist
            self.y = maxY

        if (nrBS == 5 and self.id == 4):
            self.x = maxDist + baseDist
            self.y = maxY + 2 * baseDist

        if (nrBS == 6):
            if (self.id < 3):
                self.x = (self.id + 1) * maxX / 4.0
                self.y = maxY / 3.0
            else:
                self.x = (self.id + 1 - 3) * maxX / 4.0
                self.y = 2 * maxY / 3.0

        if (nrBS == 8):
            if (self.id < 4):
                self.x = (self.id + 1) * maxX / 5.0
                self.y = maxY / 3.0
            else:
                self.x = (self.id + 1 - 4) * maxX / 5.0
                self.y = 2 * maxY / 3.0

        if (nrBS == 24):
            if (self.id < 8):
                self.x = (self.id + 1) * maxX / 9.0
                self.y = maxY / 4.0
            elif (self.id < 16):
                self.x = (self.id + 1 - 8) * maxX / 9.0
                self.y = 2 * maxY / 4.0
            else:
                self.x = (self.id + 1 - 16) * maxX / 9.0
                self.y = 3 * maxY / 4.0

        if (nrBS == 96):
            if (self.id < 24):
                self.x = (self.id + 1) * maxX / 25.0
                self.y = maxY / 5.0
            elif (self.id < 48):
                self.x = (self.id + 1 - 24) * maxX / 25.0
                self.y = 2 * maxY / 5.0
            elif (self.id < 72):
                self.x = (self.id + 1 - 48) * maxX / 25.0
                self.y = 3 * maxY / 5.0
            else:
                self.x = (self.id + 1 - 72) * maxX / 25.0
                self.y = 4 * maxY / 5.0

        # print "BSx:", self.x, "BSy:", self.y
        if (graphics):
            # XXX should be base station position
            if (self.id == 0):
                ax.add_artist(plt.Circle((self.x, self.y), 4, fill=True, color='blue'))
                ax.add_artist(plt.Circle((self.x, self.y), maxDist, fill=False, color='blue'))
            if (self.id == 1):
                ax.add_artist(plt.Circle((self.x, self.y), 4, fill=True, color='red'))
                ax.add_artist(plt.Circle((self.x, self.y), maxDist, fill=False, color='red'))
            if (self.id == 2):
                ax.add_artist(plt.Circle((self.x, self.y), 4, fill=True, color='green'))
                ax.add_artist(plt.Circle((self.x, self.y), maxDist, fill=False, color='green'))
            if (self.id == 3):
                ax.add_artist(plt.Circle((self.x, self.y), 4, fill=True, color='brown'))
                ax.add_artist(plt.Circle((self.x, self.y), maxDist, fill=False, color='brown'))
            if (self.id == 4):
                ax.add_artist(plt.Circle((self.x, self.y), 4, fill=True, color='orange'))
                ax.add_artist(plt.Circle((self.x, self.y), maxDist, fill=False, color='orange'))
