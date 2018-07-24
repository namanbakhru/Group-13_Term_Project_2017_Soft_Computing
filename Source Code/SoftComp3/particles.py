### EXESOFT PYIGNITION ###
# Copyright David Barker 2010
#
# Particle and ParticleSource objects


import keyframes, interpolate, random, math, pygame, constants
from constants import *

kc1 = 2.0
tc1 = 2.0
kc2 = 2.0
tc2 = 2.0
kc3 = 2.0
tc3 = 2.0
kc4 = 2.0
tc4 = 2.0
kc5 = 2.0
tc5 = 2.0
kc6 = 2.0
tc6 = 2.0
kc7 = 2.0
tc7 = 2.0
kc8 = 2.0
tc8 = 2.0
kc9 = 2.0
tc9 = 2.0
kc10 = 2.0
tc10 = 2.0
kc11 = 2.0
tc11 = 2.0
kc12 = 2.0
tc12 = 2.0
kc13 = 2.0
tc13 = 2.0
kc14 = 2.0
tc14 = 2.0
kc15 = 2.0
tc15 = 2.0
kc16 = 2.0
tc16 = 2.0
kc17 = 2.0
tc17 = 2.0
kc18 = 2.0
tc18 = 2.0
kc19 = 2.0
tc19 = 2.0
kc20 = 2.0
tc20 = 2.0
kc21 = 2.0
tc21 = 2.0
kc22 = 2.0
tc22 = 2.0
kc23 = 2.0
tc23 = 2.0
kc24 = 2.0
tc24 = 2.0
kc25 = 2.0
tc25 = 2.0
xpos = 0
ypos = 0
xpos1 = 0
ypos1 = 0
xpos2 = 0
ypos2 = 0
xpos3 = 0
ypos3 = 0
xpos4 = 0
ypos4 = 0
xpos5 = 0
ypos5 = 0
xpos6 = 0
ypos6 = 0
xpos7 = 0
ypos7 = 0
xpos8 = 0
ypos8 = 0
xpos9 = 0
ypos9 = 0
xpos10 = 0
ypos10 = 0
xpos11 = 0
ypos11 = 0
xpos12 = 0
ypos12 = 0
xpos13 = 0
ypos13 = 0
xpos14 = 0
ypos14 = 0
xpos15 = 0
ypos15 = 0
xpos16 = 0
ypos16 = 0
xpos17 = 0
ypos17 = 0
xpos18 = 0
ypos18 = 0
xpos19 = 0
ypos19 = 0
xpos20 = 0
ypos20 = 0
xpos21 = 0
ypos21 = 0
xpos22 = 0
ypos22 = 0
xpos23 = 0
ypos23 = 0
xpos24 = 0
ypos24 = 0
xpos25 = 0
ypos25 = 0
xpos26 = 0
ypos26 = 0
dist = []
dixt = []
dix0 = []
dix1 = []
dix2 = []
dix3 = []
dix4 = []
dix5 = []
dix6 = []
dix7 = []
dix8 = []
dix9 = []
dix10 = []
dix11 = []
dix12 = []
dix13 = []
dix14 = []
dix15 = []
dix16 = []
dix17 = []
dix18 = []
dix19 = []
dix20 = []
dix21 = []
dix22 = []
dix23 = []
cpr = 0
ptr = 0
pttr = 0
tt = 0


class Particle:
    def __init__(self, parent, initpos, velocity, angle, life, drawtype=DRAWTYPE_POINT, colour=(0, 0, 0), radius=0.0,
                 length=0.0, image=None, keyframes=[]):
        self.parent = parent
        self.pos = initpos
        self.velocity = velocity
        self.life = life
        self.drawtype = drawtype
        self.colour = colour
        self.radius = radius
        self.length = length
        self.image = image
        self.angle = angle
        self.keyframes = []
        self.keyframes.extend(keyframes[:])
        self.curframe = 0

        self.alive = True

    def Update(self):
        global kc1, tc1, kc2, tc2, kc3, tc3, kc4, tc4, kc5, tc5, kc6, tc6, kc7, tc7, kc8, tc8, kc9, tc9, kc10, tc10, kc11, tc11, tt, cpr, ptr, pttr
        global kc12, tc12, kc13, tc13, kc14, tc14, kc15, tc15, kc16, tc16, kc17, tc17, kc18, tc18, kc19, tc19, kc20, tc20, kc21, tc21, kc22, tc22, kc23, tc23, kc24, tc24, kc25, tc25
        global xpos, ypos, xpos1, ypos1, xpos2, ypos2, xpos3, ypos3, xpos4, ypos4, xpos5, ypos5, xpos6, ypos6, xpos7, ypos7, xpos8, ypos8, xpos9, ypos9, xpos10, ypos10, xpos11, ypos11, xpos26, ypos26
        global xpos12, ypos12, xpos13, ypos13, xpos14, ypos14, xpos15, ypos15, xpos16, ypos16, xpos17, ypos17, xpos18, ypos18, xpos19, ypos19, xpos20, ypos20, xpos21, ypos21, xpos22, ypos22, xpos23, ypos23, xpos24, ypos24, xpos25, ypos25
        global dist, dixt, dix0, dix1, dix2, dix3, dix4, dix5, dix6, dix7, dix8, dix9, dix10, dix11, dix12, dix13, dix14, dix15, dix15, dix16, dix17, dix18, dix19, dix20, dix21, dix22, dix23

        tt = 10*random.random()

        if constants.ck % 27 == 1:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc1 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc1 = t
            if self.pos[0] < 25 :
                kc1 = -1 * kc1
            elif self.pos[0] > 1200:
                kc1 = -1 * kc1
            if self.pos[1] < 25:
                tc1 = -1 * tc1
            elif self.pos[1] > 625:
                tc1 = -1 * tc1
            xpos1 = self.pos[0] + kc1
            ypos1 = self.pos[1] + tc1
            self.pos = [xpos1, ypos1]
        elif constants.ck % 27 == 2:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc2 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc2 = t
            if self.pos[0] < 25 :
                kc2 = -1 * kc2
            elif self.pos[0] > 1200:
                kc2 = -1 * kc2
            if self.pos[1] < 25:
                tc2 = -1 * tc2
            elif self.pos[1] > 625:
                tc2 = -1 * tc2
            xpos2 = self.pos[0] - kc2
            ypos2 = self.pos[1] + tc2
            self.pos = [xpos2, ypos2]
        elif constants.ck % 27 == 3:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc3 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc3 = t
            if self.pos[0] < 25 :
                kc3 = -1 * kc3
            elif self.pos[0] > 1200:
                kc3 = -1 * kc3
            if self.pos[1] < 25:
                tc3 = -1 * tc3
            elif self.pos[1] > 625:
                tc3 = -1 * tc3
            xpos3 = self.pos[0] + kc3
            ypos3 = self.pos[1] - tc3
            self.pos = [xpos3, ypos3]
        elif constants.ck % 27 == 4:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc4 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc4 = t
            if self.pos[0] < 25 :
                kc4 = -1 * kc4
            elif self.pos[0] > 1200:
                kc4 = -1 * kc4
            if self.pos[1] < 25:
                tc4 = -1 * tc4
            elif self.pos[1] > 625:
                tc4 = -1 * tc4
            xpos4 = self.pos[0] - kc4
            ypos4 = self.pos[1] - tc4
            self.pos = [xpos4, ypos4]
        elif constants.ck % 27 == 5:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc5 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc5 = t
            if self.pos[0] < 25 :
                kc5 = -1 * kc5
            elif self.pos[0] > 1200:
                kc5 = -1 * kc5
            if self.pos[1] < 25:
                tc5 = -1 * tc5
            elif self.pos[1] > 625:
                tc5 = -1 * tc5
            xpos5 = self.pos[0] + kc5
            ypos5 = self.pos[1] + tc5
            self.pos = [xpos5, ypos5]
        elif constants.ck % 27 == 6:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc6 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc6 = t
            if self.pos[0] < 25 :
                kc6 = -1 * kc6
            elif self.pos[0] > 1200:
                kc6 = -1 * kc6
            if self.pos[1] < 25:
                tc6 = -1 * tc6
            elif self.pos[1] > 625:
                tc6 = -1 * tc6
            xpos6 = self.pos[0] + kc6
            ypos6 = self.pos[1] - tc6
            self.pos = [xpos6, ypos6]
        elif constants.ck % 27 == 7:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc7 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc7 = t
            if self.pos[0] < 25 :
                kc7 = -1 * kc7
            elif self.pos[0] > 1200:
                kc7 = -1 * kc7
            if self.pos[1] < 25:
                tc7 = -1 * tc7
            elif self.pos[1] > 625:
                tc7 = -1 * tc7
            xpos7 = self.pos[0] - kc7
            ypos7 = self.pos[1] + tc7
            self.pos = [xpos7, ypos7]
        elif constants.ck % 27 == 8:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc8 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc8 = t
            if self.pos[0] < 25 :
                kc8 = -1 * kc8
            elif self.pos[0] > 1200:
                kc8 = -1 * kc8
            if self.pos[1] < 25:
                tc8 = -1 * tc8
            elif self.pos[1] > 625:
                tc8 = -1 * tc8
            xpos8 = self.pos[0] - kc8
            ypos8 = self.pos[1] - tc8
            self.pos = [xpos8, ypos8]
        elif constants.ck % 27 == 9:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc9 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc9 = t
            if self.pos[0] < 25 :
                kc9 = -1 * kc9
            elif self.pos[0] > 1200:
                kc9 = -1 * kc9
            if self.pos[1] < 25:
                tc9 = -1 * tc9
            elif self.pos[1] > 625:
                tc9 = -1 * tc9
            xpos9 = self.pos[0] + kc9
            ypos9 = self.pos[1] - tc9
            self.pos = [xpos9, ypos9]
        elif constants.ck % 27 == 10:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc10 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc10 = t
            if self.pos[0] < 25 :
                kc10 = -1 * kc10
            elif self.pos[0] > 1200:
                kc10 = -1 * kc10
            if self.pos[1] < 25:
                tc10 = -1 * tc10
            elif self.pos[1] > 625:
                tc10 = -1 * tc10
            xpos10 = self.pos[0] + kc10
            ypos10 = self.pos[1] + tc10
            self.pos = [xpos10, ypos10]
        elif constants.ck % 27 == 11:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc11 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc11 = t
            if self.pos[0] < 25 :
                kc11 = -1 * kc11
            elif self.pos[0] > 1200:
                kc11 = -1 * kc11
            if self.pos[1] < 25:
                tc11 = -1 * tc11
            elif self.pos[1] > 625:
                tc11 = -1 * tc11
            xpos11 = self.pos[0] - kc11
            ypos11 = self.pos[1] + tc11
            self.pos = [xpos11, ypos11]
        elif constants.ck % 27 == 12:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc12 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc12 = t
            if self.pos[0] < 25 :
                kc12 = -1 * kc12
            elif self.pos[0] > 1200:
                kc12 = -1 * kc12
            if self.pos[1] < 25:
                tc12 = -1 * tc12
            elif self.pos[1] > 625:
                tc12 = -1 * tc12
            xpos12 = self.pos[0] - kc12
            ypos12 = self.pos[1] - tc12
            self.pos = [xpos12, ypos12]
        elif constants.ck % 27 == 13:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc13 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc13 = t
            if self.pos[0] < 25 :
                kc13 = -1 * kc13
            elif self.pos[0] > 1200:
                kc13 = -1 * kc13
            if self.pos[1] < 25:
                tc13 = -1 * tc13
            elif self.pos[1] > 625:
                tc13 = -1 * tc13
            xpos13 = self.pos[0] - kc13
            ypos13 = self.pos[1] + tc13
            self.pos = [xpos13, ypos13]
        elif constants.ck % 27 == 14:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc14 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc14 = t
            if self.pos[0] < 25 :
                kc14 = -1 * kc14
            elif self.pos[0] > 1200:
                kc14 = -1 * kc14
            if self.pos[1] < 25:
                tc14 = -1 * tc14
            elif self.pos[1] > 625:
                tc14 = -1 * tc14
            xpos14 = self.pos[0] + kc14
            ypos14 = self.pos[1] - tc14
            self.pos = [xpos14, ypos14]
        elif constants.ck % 27 == 15:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc15 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc15 = t
            if self.pos[0] < 25 :
                kc15 = -1 * kc15
            elif self.pos[0] > 1200:
                kc15 = -1 * kc15
            if self.pos[1] < 25:
                tc15 = -1 * tc15
            elif self.pos[1] > 625:
                tc15 = -1 * tc15
            xpos15 = self.pos[0] - kc15
            ypos15 = self.pos[1] - tc15
            self.pos = [xpos15, ypos15]
        elif constants.ck % 27 == 16:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc16 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc16 = t
            if self.pos[0] < 25 :
                kc16 = -1 * kc16
            elif self.pos[0] > 1200:
                kc16 = -1 * kc16
            if self.pos[1] < 25:
                tc16 = -1 * tc16
            elif self.pos[1] > 625:
                tc16 = -1 * tc16
            xpos16 = self.pos[0] + kc16
            ypos16 = self.pos[1] + tc16
            self.pos = [xpos16, ypos16]
        elif constants.ck % 27 == 17:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc17 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc17 = t
            if self.pos[0] < 25 :
                kc17 = -1 * kc17
            elif self.pos[0] > 1200:
                kc17 = -1 * kc17
            if self.pos[1] < 25:
                tc17 = -1 * tc17
            elif self.pos[1] > 625:
                tc17 = -1 * tc17
            xpos17 = self.pos[0] - kc17
            ypos17 = self.pos[1] + tc17
            self.pos = [xpos17, ypos17]
        elif constants.ck % 27 == 18:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc18 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc18 = t
            if self.pos[0] < 25 :
                kc18 = -1 * kc18
            elif self.pos[0] > 1200:
                kc18 = -1 * kc18
            if self.pos[1] < 25:
                tc18 = -1 * tc18
            elif self.pos[1] > 625:
                tc18 = -1 * tc18
            xpos18 = self.pos[0] - kc18
            ypos18 = self.pos[1] - tc18
            self.pos = [xpos18, ypos18]
        elif constants.ck % 27 == 19:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc19 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc19 = t
            if self.pos[0] < 25 :
                kc19 = -1 * kc19
            elif self.pos[0] > 1200:
                kc19 = -1 * kc19
            if self.pos[1] < 25:
                tc19 = -1 * tc19
            elif self.pos[1] > 625:
                tc19 = -1 * tc19
            xpos19 = self.pos[0] + kc19
            ypos19 = self.pos[1] + tc19
            self.pos = [xpos19, ypos19]
        elif constants.ck % 27 == 20:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc20 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc20 = t
            if self.pos[0] < 25 :
                kc20 = -1 * kc20
            elif self.pos[0] > 1200:
                kc20 = -1 * kc20
            if self.pos[1] < 25:
                tc20 = -1 * tc20
            elif self.pos[1] > 625:
                tc20 = -1 * tc20
            xpos20 = self.pos[0] + kc20
            ypos20 = self.pos[1] - tc20
            self.pos = [xpos20, ypos20]
        elif constants.ck % 27 == 21:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc21 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc21 = t
            if self.pos[0] < 25 :
                kc21 = -1 * kc21
            elif self.pos[0] > 1200:
                kc21 = -1 * kc21
            if self.pos[1] < 25:
                tc21 = -1 * tc21
            elif self.pos[1] > 625:
                tc21 = -1 * tc21
            xpos21 = self.pos[0] + kc21
            ypos21 = self.pos[1] + tc21
            self.pos = [xpos21, ypos21]
        elif constants.ck % 27 == 22:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc22 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc22 = t
            if self.pos[0] < 25 :
                kc22 = -1 * kc22
            elif self.pos[0] > 1200:
                kc22 = -1 * kc22
            if self.pos[1] < 25:
                tc22 = -1 * tc22
            elif self.pos[1] > 625:
                tc22 = -1 * tc22
            xpos22 = self.pos[0] - kc22
            ypos22 = self.pos[1] - tc22
            self.pos = [xpos22, ypos22]
        elif constants.ck % 27 == 23:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc23 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc23 = t
            if self.pos[0] < 25 :
                kc23 = -1 * kc23
            elif self.pos[0] > 1200:
                kc23 = -1 * kc23
            if self.pos[1] < 25:
                tc23 = -1 * tc23
            elif self.pos[1] > 625:
                tc23 = -1 * tc23
            xpos23 = self.pos[0] - kc23
            ypos23 = self.pos[1] + tc23
            self.pos = [xpos23, ypos23]
        elif constants.ck % 27 == 24:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc24 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc24 = t
            if self.pos[0] < 25 :
                kc24 = -1 * kc24
            elif self.pos[0] > 1200:
                kc24 = -1 * kc24
            if self.pos[1] < 25:
                tc24 = -1 * tc24
            elif self.pos[1] > 625:
                tc24 = -1 * tc24
            xpos24 = self.pos[0] + kc24
            ypos24 = self.pos[1] - tc24
            self.pos = [xpos24, ypos24]
        elif constants.ck % 27 == 25:
            self.angle = random.random() * 2 * math.pi
            if tt > 9.5:
                k = math.sin(self.angle) * self.velocity[0]
                kc25 = k
                t = math.cos(self.angle) * self.velocity[1]
                tc25 = t
            if self.pos[0] < 25 :
                kc25 = -1 * kc25
            elif self.pos[0] > 1200:
                kc25 = -1 * kc25
            if self.pos[1] < 25:
                tc25 = -1 * tc25
            elif self.pos[1] > 625:
                tc25 = -1 * tc25
            xpos25 = self.pos[0] - kc25
            ypos25 = self.pos[1] + tc25
            self.pos = [xpos25, ypos25]
        elif constants.ck % 27 == 26:
            self.pos = [self.pos[0], self.pos[1]]
            xpos26 = self.pos[0]
            ypos26 = self.pos[1]
        elif constants.ck % 27 == 0:
            xpos = self.pos[0]
            ypos = self.pos[1]
            x1pos = xpos + 10
            y1pos = ypos
            x2pos = xpos + 10 * math.cos(math.pi / 4)
            y2pos = ypos + 10 * math.sin(math.pi / 4)
            x3pos = xpos + 10 * math.cos(math.pi / 4)
            y3pos = ypos - 10 * math.sin(math.pi / 4)
            x4pos = xpos
            y4pos = ypos + 10
            x5pos = xpos
            y5pos = ypos - 10
            x6pos = xpos - 10
            y6pos = ypos
            x7pos = xpos - 10 * math.cos(math.pi / 4)
            y7pos = ypos + 10 * math.sin(math.pi / 4)
            x8pos = xpos - 10 * math.cos(math.pi / 4)
            y8pos = ypos - 10 * math.sin(math.pi / 4)
            x9pos = xpos + 10 * math.cos(math.pi / 6)
            y9pos = ypos - 10 * math.sin(math.pi / 6)
            x10pos = xpos + 10 * math.cos(math.pi / 12)
            y10pos = ypos - 10 * math.sin(math.pi / 12)
            x11pos = xpos + 10 * math.cos(math.pi / 12)
            y11pos = ypos + 10 * math.sin(math.pi / 12)
            x12pos = xpos + 10 * math.cos(math.pi / 6)
            y12pos = ypos + 10 * math.sin(math.pi / 6)
            x13pos = xpos + 10 * math.cos(math.pi / 3)
            y13pos = ypos + 10 * math.sin(math.pi / 3)
            x14pos = xpos + 10 * math.cos(5 * math.pi / 12)
            y14pos = ypos + 10 * math.sin(5 * math.pi / 12)
            x15pos = xpos - 10 * math.cos(5 * math.pi / 12)
            y15pos = ypos + 10 * math.sin(5 * math.pi / 12)
            x16pos = xpos - 10 * math.cos(math.pi / 3)
            y16pos = ypos + 10 * math.sin(math.pi / 3)
            x17pos = xpos - 10 * math.cos(math.pi / 6)
            y17pos = ypos + 10 * math.sin(math.pi / 6)
            x18pos = xpos - 10 * math.cos(math.pi / 12)
            y18pos = ypos + 10 * math.sin(math.pi / 12)
            x19pos = xpos - 10 * math.cos(math.pi / 12)
            y19pos = ypos - 10 * math.sin(math.pi / 12)
            x20pos = xpos - 10 * math.cos(math.pi / 6)
            y20pos = ypos - 10 * math.sin(math.pi / 6)
            x21pos = xpos - 10 * math.cos(math.pi / 3)
            y21pos = ypos - 10 * math.sin(math.pi / 3)
            x22pos = xpos - 10 * math.cos(5 * math.pi / 12)
            y22pos = ypos - 10 * math.sin(5 * math.pi / 12)
            x23pos = xpos + 10 * math.cos(5 *math.pi / 12)
            y23pos = ypos - 10 * math.sin(5 *math.pi / 12)
            x24pos = xpos + 10 * math.cos(math.pi / 3)
            y24pos = ypos - 10 * math.sin(math.pi / 3)
            dis = math.sqrt((xpos - xpos26) * (xpos - xpos26) + (ypos - ypos26) * (ypos - ypos26))
            dist0 = math.sqrt((x1pos - xpos26) * (x1pos - xpos26) + (y1pos - ypos26) * (y1pos - ypos26))
            dist.append(dist0)
            dist1 = math.sqrt((x2pos - xpos26) * (x2pos - xpos26) + (y2pos - ypos26) * (y2pos - ypos26))
            dist.append(dist1)
            dist2 = math.sqrt((x3pos - xpos26) * (x3pos - xpos26) + (y3pos - ypos26) * (y3pos - ypos26))
            dist.append(dist2)
            dist3 = math.sqrt((x4pos - xpos26) * (x4pos - xpos26) + (y4pos - ypos26) * (y4pos - ypos26))
            dist.append(dist3)
            dist4 = math.sqrt((x5pos - xpos26) * (x5pos - xpos26) + (y5pos - ypos26) * (y5pos - ypos26))
            dist.append(dist4)
            dist5 = math.sqrt((x6pos - xpos26) * (x6pos - xpos26) + (y6pos - ypos26) * (y6pos - ypos26))
            dist.append(dist5)
            dist6 = math.sqrt((x7pos - xpos26) * (x7pos - xpos26) + (y7pos - ypos26) * (y7pos - ypos26))
            dist.append(dist6)
            dist7 = math.sqrt((x8pos - xpos26) * (x8pos - xpos26) + (y8pos - ypos26) * (y8pos - ypos26))
            dist.append(dist7)
            dist8 = math.sqrt((x9pos - xpos26) * (x9pos - xpos26) + (y9pos - ypos26) * (y9pos - ypos26))
            dist.append(dist8)
            dist9 = math.sqrt((x10pos - xpos26) * (x10pos - xpos26) + (y10pos - ypos26) * (y10pos - ypos26))
            dist.append(dist9)
            dist10 = math.sqrt((x11pos - xpos26) * (x11pos - xpos26) + (y11pos - ypos26) * (y11pos - ypos26))
            dist.append(dist10)
            dist11 = math.sqrt((x12pos - xpos26) * (x12pos - xpos26) + (y12pos - ypos26) * (y12pos - ypos26))
            dist.append(dist11)
            dist12 = math.sqrt((x13pos - xpos26) * (x13pos - xpos26) + (y13pos - ypos26) * (y13pos - ypos26))
            dist.append(dist12)
            dist13 = math.sqrt((x14pos - xpos26) * (x14pos - xpos26) + (y14pos - ypos26) * (y14pos - ypos26))
            dist.append(dist13)
            dist14 = math.sqrt((x15pos - xpos26) * (x15pos - xpos26) + (y15pos - ypos26) * (y15pos - ypos26))
            dist.append(dist14)
            dist15 = math.sqrt((x16pos - xpos26) * (x16pos - xpos26) + (y16pos - ypos26) * (y16pos - ypos26))
            dist.append(dist15)
            dist16 = math.sqrt((x17pos - xpos26) * (x17pos - xpos26) + (y17pos - ypos26) * (y17pos - ypos26))
            dist.append(dist16)
            dist17 = math.sqrt((x18pos - xpos26) * (x18pos - xpos26) + (y18pos - ypos26) * (y18pos - ypos26))
            dist.append(dist17)
            dist18 = math.sqrt((x19pos - xpos26) * (x19pos - xpos26) + (y19pos - ypos26) * (y19pos - ypos26))
            dist.append(dist18)
            dist19 = math.sqrt((x20pos - xpos26) * (x20pos - xpos26) + (y20pos - ypos26) * (y20pos - ypos26))
            dist.append(dist19)
            dist20 = math.sqrt((x21pos - xpos26) * (x21pos - xpos26) + (y21pos - ypos26) * (y21pos - ypos26))
            dist.append(dist20)
            dist21 = math.sqrt((x22pos - xpos26) * (x22pos - xpos26) + (y22pos - ypos26) * (y22pos - ypos26))
            dist.append(dist21)
            dist22 = math.sqrt((x23pos - xpos26) * (x23pos - xpos26) + (y23pos - ypos26) * (y23pos - ypos26))
            dist.append(dist22)
            dist23 = math.sqrt((x24pos - xpos26) * (x24pos - xpos26) + (y24pos - ypos26) * (y24pos - ypos26))
            dist.append(dist23)
            dixt = list(sorted(dist))
            for i in range(24):
                for j in range(24):
                    if dixt[i] == dist[j]:
                        if j == 0:
                            dst1 = math.sqrt((x1pos - xpos1) * (x1pos - xpos1) + (y1pos - ypos1) * (y1pos - ypos1))
                            dix0.append(dst1)
                            dst2 = math.sqrt((x1pos - xpos2) * (x1pos - xpos2) + (y1pos - ypos2) * (y1pos - ypos2))
                            dix0.append(dst2)
                            dst3 = math.sqrt((x1pos - xpos3) * (x1pos - xpos3) + (y1pos - ypos3) * (y1pos - ypos3))
                            dix0.append(dst3)
                            dst4 = math.sqrt((x1pos - xpos4) * (x1pos - xpos4) + (y1pos - ypos4) * (y1pos - ypos4))
                            dix0.append(dst4)
                            dst5 = math.sqrt((x1pos - xpos5) * (x1pos - xpos5) + (y1pos - ypos5) * (y1pos - ypos5))
                            dix0.append(dst5)
                            dst6 = math.sqrt((x1pos - xpos6) * (x1pos - xpos6) + (y1pos - ypos6) * (y1pos - ypos6))
                            dix0.append(dst6)
                            dst7 = math.sqrt((x1pos - xpos7) * (x1pos - xpos7) + (y1pos - ypos7) * (y1pos - ypos7))
                            dix0.append(dst7)
                            dst8 = math.sqrt((x1pos - xpos8) * (x1pos - xpos8) + (y1pos - ypos8) * (y1pos - ypos8))
                            dix0.append(dst8)
                            dst9 = math.sqrt((x1pos - xpos9) * (x1pos - xpos9) + (y1pos - ypos9) * (y1pos - ypos9))
                            dix0.append(dst9)
                            dst10 = math.sqrt((x1pos - xpos10) * (x1pos - xpos10) + (y1pos - ypos10) * (y1pos - ypos10))
                            dix0.append(dst10)
                            dst11 = math.sqrt((x1pos - xpos11) * (x1pos - xpos11) + (y1pos - ypos11) * (y1pos - ypos11))
                            dix0.append(dst11)
                            dst12 = math.sqrt((x1pos - xpos12) * (x1pos - xpos12) + (y1pos - ypos12) * (y1pos - ypos12))
                            dix0.append(dst12)
                            dst13 = math.sqrt((x1pos - xpos13) * (x1pos - xpos13) + (y1pos - ypos13) * (y1pos - ypos13))
                            dix0.append(dst13)
                            dst14 = math.sqrt((x1pos - xpos14) * (x1pos - xpos14) + (y1pos - ypos14) * (y1pos - ypos14))
                            dix0.append(dst14)
                            dst15 = math.sqrt((x1pos - xpos15) * (x1pos - xpos15) + (y1pos - ypos15) * (y1pos - ypos15))
                            dix0.append(dst15)
                            dst16 = math.sqrt((x1pos - xpos16) * (x1pos - xpos16) + (y1pos - ypos16) * (y1pos - ypos16))
                            dix0.append(dst16)
                            dst17 = math.sqrt((x1pos - xpos17) * (x1pos - xpos17) + (y1pos - ypos17) * (y1pos - ypos17))
                            dix0.append(dst17)
                            dst18 = math.sqrt((x1pos - xpos18) * (x1pos - xpos18) + (y1pos - ypos18) * (y1pos - ypos18))
                            dix0.append(dst18)
                            dst19 = math.sqrt((x1pos - xpos19) * (x1pos - xpos19) + (y1pos - ypos19) * (y1pos - ypos19))
                            dix0.append(dst19)
                            dst20 = math.sqrt((x1pos - xpos20) * (x1pos - xpos20) + (y1pos - ypos20) * (y1pos - ypos20))
                            dix0.append(dst20)
                            dst21 = math.sqrt((x1pos - xpos21) * (x1pos - xpos21) + (y1pos - ypos21) * (y1pos - ypos21))
                            dix0.append(dst21)
                            dst22 = math.sqrt((x1pos - xpos22) * (x1pos - xpos22) + (y1pos - ypos22) * (y1pos - ypos22))
                            dix0.append(dst22)
                            dst23 = math.sqrt((x1pos - xpos23) * (x1pos - xpos23) + (y1pos - ypos23) * (y1pos - ypos23))
                            dix0.append(dst23)
                            dst24 = math.sqrt((x1pos - xpos24) * (x1pos - xpos24) + (y1pos - ypos24) * (y1pos - ypos24))
                            dix0.append(dst24)
                            dst25 = math.sqrt((x1pos - xpos25) * (x1pos - xpos25) + (y1pos - ypos25) * (y1pos - ypos25))
                            dix0.append(dst25)

                            for k in range(25):
                                if dix0[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x1pos, y1pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 1:
                            dst1 = math.sqrt((x2pos - xpos1) * (x2pos - xpos1) + (y2pos - ypos1) * (y2pos - ypos1))
                            dix1.append(dst1)
                            dst2 = math.sqrt((x2pos - xpos2) * (x2pos - xpos2) + (y2pos - ypos2) * (y2pos - ypos2))
                            dix1.append(dst2)
                            dst3 = math.sqrt((x2pos - xpos3) * (x2pos - xpos3) + (y2pos - ypos3) * (y2pos - ypos3))
                            dix1.append(dst3)
                            dst4 = math.sqrt((x2pos - xpos4) * (x2pos - xpos4) + (y2pos - ypos4) * (y2pos - ypos4))
                            dix1.append(dst4)
                            dst5 = math.sqrt((x2pos - xpos5) * (x2pos - xpos5) + (y2pos - ypos5) * (y2pos - ypos5))
                            dix1.append(dst5)
                            dst6 = math.sqrt((x2pos - xpos6) * (x2pos - xpos6) + (y2pos - ypos6) * (y2pos - ypos6))
                            dix1.append(dst6)
                            dst7 = math.sqrt((x2pos - xpos7) * (x2pos - xpos7) + (y2pos - ypos7) * (y2pos - ypos7))
                            dix1.append(dst7)
                            dst8 = math.sqrt((x2pos - xpos8) * (x2pos - xpos8) + (y2pos - ypos8) * (y2pos - ypos8))
                            dix1.append(dst8)
                            dst9 = math.sqrt((x2pos - xpos9) * (x2pos - xpos9) + (y2pos - ypos9) * (y2pos - ypos9))
                            dix1.append(dst9)
                            dst10 = math.sqrt((x2pos - xpos10) * (x2pos - xpos10) + (y2pos - ypos10) * (y2pos - ypos10))
                            dix1.append(dst10)
                            dst11 = math.sqrt((x2pos - xpos11) * (x2pos - xpos11) + (y2pos - ypos11) * (y2pos - ypos11))
                            dix1.append(dst11)
                            dst12 = math.sqrt((x2pos - xpos12) * (x2pos - xpos12) + (y2pos - ypos12) * (y2pos - ypos12))
                            dix1.append(dst12)
                            dst13 = math.sqrt((x2pos - xpos13) * (x2pos - xpos13) + (y2pos - ypos13) * (y2pos - ypos13))
                            dix1.append(dst13)
                            dst14 = math.sqrt((x2pos - xpos14) * (x2pos - xpos14) + (y2pos - ypos14) * (y2pos - ypos14))
                            dix1.append(dst14)
                            dst15 = math.sqrt((x2pos - xpos15) * (x2pos - xpos15) + (y2pos - ypos15) * (y2pos - ypos15))
                            dix1.append(dst15)
                            dst16 = math.sqrt((x2pos - xpos16) * (x2pos - xpos16) + (y2pos - ypos16) * (y2pos - ypos16))
                            dix1.append(dst16)
                            dst17 = math.sqrt((x2pos - xpos17) * (x2pos - xpos17) + (y2pos - ypos17) * (y2pos - ypos17))
                            dix1.append(dst17)
                            dst18 = math.sqrt((x2pos - xpos18) * (x2pos - xpos18) + (y2pos - ypos18) * (y2pos - ypos18))
                            dix1.append(dst18)
                            dst19 = math.sqrt((x2pos - xpos19) * (x2pos - xpos19) + (y2pos - ypos19) * (y2pos - ypos19))
                            dix1.append(dst19)
                            dst20 = math.sqrt((x2pos - xpos20) * (x2pos - xpos20) + (y2pos - ypos20) * (y2pos - ypos20))
                            dix1.append(dst20)
                            dst21 = math.sqrt((x2pos - xpos21) * (x2pos - xpos21) + (y2pos - ypos21) * (y2pos - ypos21))
                            dix1.append(dst21)
                            dst22 = math.sqrt((x2pos - xpos22) * (x2pos - xpos22) + (y2pos - ypos22) * (y2pos - ypos22))
                            dix1.append(dst22)
                            dst23 = math.sqrt((x2pos - xpos23) * (x2pos - xpos23) + (y2pos - ypos23) * (y2pos - ypos23))
                            dix1.append(dst23)
                            dst24 = math.sqrt((x2pos - xpos24) * (x2pos - xpos24) + (y2pos - ypos24) * (y2pos - ypos24))
                            dix1.append(dst24)
                            dst25 = math.sqrt((x2pos - xpos25) * (x2pos - xpos25) + (y2pos - ypos25) * (y2pos - ypos25))
                            dix1.append(dst25)
                            for k in range(25):
                                if dix1[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x2pos, y2pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 2:
                            dst1 = math.sqrt((x3pos - xpos1) * (x3pos - xpos1) + (y3pos - ypos1) * (y3pos - ypos1))
                            dix2.append(dst1)
                            dst2 = math.sqrt((x3pos - xpos2) * (x3pos - xpos2) + (y3pos - ypos2) * (y3pos - ypos2))
                            dix2.append(dst2)
                            dst3 = math.sqrt((x3pos - xpos3) * (x3pos - xpos3) + (y3pos - ypos3) * (y3pos - ypos3))
                            dix2.append(dst3)
                            dst4 = math.sqrt((x3pos - xpos4) * (x3pos - xpos4) + (y3pos - ypos4) * (y3pos - ypos4))
                            dix2.append(dst4)
                            dst5 = math.sqrt((x3pos - xpos5) * (x3pos - xpos5) + (y3pos - ypos5) * (y3pos - ypos5))
                            dix2.append(dst5)
                            dst6 = math.sqrt((x3pos - xpos6) * (x3pos - xpos6) + (y3pos - ypos6) * (y3pos - ypos6))
                            dix2.append(dst6)
                            dst7 = math.sqrt((x3pos - xpos7) * (x3pos - xpos7) + (y3pos - ypos7) * (y3pos - ypos7))
                            dix2.append(dst7)
                            dst8 = math.sqrt((x3pos - xpos8) * (x3pos - xpos8) + (y3pos - ypos8) * (y3pos - ypos8))
                            dix2.append(dst8)
                            dst9 = math.sqrt((x3pos - xpos9) * (x3pos - xpos9) + (y3pos - ypos9) * (y3pos - ypos9))
                            dix2.append(dst9)
                            dst10 = math.sqrt((x3pos - xpos10) * (x3pos - xpos10) + (y3pos - ypos10) * (y3pos - ypos10))
                            dix2.append(dst10)
                            dst11 = math.sqrt((x3pos - xpos11) * (x3pos - xpos11) + (y3pos - ypos11) * (y3pos - ypos11))
                            dix2.append(dst11)
                            dst12 = math.sqrt((x3pos - xpos12) * (x3pos - xpos12) + (y3pos - ypos12) * (y3pos - ypos12))
                            dix2.append(dst12)
                            dst13 = math.sqrt((x3pos - xpos13) * (x3pos - xpos13) + (y3pos - ypos13) * (y3pos - ypos13))
                            dix2.append(dst13)
                            dst14 = math.sqrt((x3pos - xpos14) * (x3pos - xpos14) + (y3pos - ypos14) * (y3pos - ypos14))
                            dix2.append(dst14)
                            dst15 = math.sqrt((x3pos - xpos15) * (x3pos - xpos15) + (y3pos - ypos15) * (y3pos - ypos15))
                            dix2.append(dst15)
                            dst16 = math.sqrt((x3pos - xpos16) * (x3pos - xpos16) + (y3pos - ypos16) * (y3pos - ypos16))
                            dix2.append(dst16)
                            dst17 = math.sqrt((x3pos - xpos17) * (x3pos - xpos17) + (y3pos - ypos17) * (y3pos - ypos17))
                            dix2.append(dst17)
                            dst18 = math.sqrt((x3pos - xpos18) * (x3pos - xpos18) + (y3pos - ypos18) * (y3pos - ypos18))
                            dix2.append(dst18)
                            dst19 = math.sqrt((x3pos - xpos19) * (x3pos - xpos19) + (y3pos - ypos19) * (y3pos - ypos19))
                            dix2.append(dst19)
                            dst20 = math.sqrt((x3pos - xpos20) * (x3pos - xpos20) + (y3pos - ypos20) * (y3pos - ypos20))
                            dix2.append(dst20)
                            dst21 = math.sqrt((x3pos - xpos21) * (x3pos - xpos21) + (y3pos - ypos21) * (y3pos - ypos21))
                            dix2.append(dst21)
                            dst22 = math.sqrt((x3pos - xpos22) * (x3pos - xpos22) + (y3pos - ypos22) * (y3pos - ypos22))
                            dix2.append(dst22)
                            dst23 = math.sqrt((x3pos - xpos23) * (x3pos - xpos23) + (y3pos - ypos23) * (y3pos - ypos23))
                            dix2.append(dst23)
                            dst24 = math.sqrt((x3pos - xpos24) * (x3pos - xpos24) + (y3pos - ypos24) * (y3pos - ypos24))
                            dix2.append(dst24)
                            dst25 = math.sqrt((x3pos - xpos25) * (x3pos - xpos25) + (y3pos - ypos25) * (y3pos - ypos25))
                            dix2.append(dst25)
                            for k in range(25):
                                if dix2[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x3pos, y3pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 3:
                            dst1 = math.sqrt((x4pos - xpos1) * (x4pos - xpos1) + (y4pos - ypos1) * (y4pos - ypos1))
                            dix3.append(dst1)
                            dst2 = math.sqrt((x4pos - xpos2) * (x4pos - xpos2) + (y4pos - ypos2) * (y4pos - ypos2))
                            dix3.append(dst2)
                            dst3 = math.sqrt((x4pos - xpos3) * (x4pos - xpos3) + (y4pos - ypos3) * (y4pos - ypos3))
                            dix3.append(dst3)
                            dst4 = math.sqrt((x4pos - xpos4) * (x4pos - xpos4) + (y4pos - ypos4) * (y4pos - ypos4))
                            dix3.append(dst4)
                            dst5 = math.sqrt((x4pos - xpos5) * (x4pos - xpos5) + (y4pos - ypos5) * (y4pos - ypos5))
                            dix3.append(dst5)
                            dst6 = math.sqrt((x4pos - xpos6) * (x4pos - xpos6) + (y4pos - ypos6) * (y4pos - ypos6))
                            dix3.append(dst6)
                            dst7 = math.sqrt((x4pos - xpos7) * (x4pos - xpos7) + (y4pos - ypos7) * (y4pos - ypos7))
                            dix3.append(dst7)
                            dst8 = math.sqrt((x4pos - xpos8) * (x4pos - xpos8) + (y4pos - ypos8) * (y4pos - ypos8))
                            dix3.append(dst8)
                            dst9 = math.sqrt((x4pos - xpos9) * (x4pos - xpos9) + (y4pos - ypos9) * (y4pos - ypos9))
                            dix3.append(dst9)
                            dst10 = math.sqrt((x4pos - xpos10) * (x4pos - xpos10) + (y4pos - ypos10) * (y4pos - ypos10))
                            dix3.append(dst10)
                            dst11 = math.sqrt((x4pos - xpos11) * (x4pos - xpos11) + (y4pos - ypos11) * (y4pos - ypos11))
                            dix3.append(dst11)
                            dst12 = math.sqrt((x4pos - xpos12) * (x4pos - xpos12) + (y4pos - ypos12) * (y4pos - ypos12))
                            dix3.append(dst12)
                            dst13 = math.sqrt((x4pos - xpos13) * (x4pos - xpos13) + (y4pos - ypos13) * (y4pos - ypos13))
                            dix3.append(dst13)
                            dst14 = math.sqrt((x4pos - xpos14) * (x4pos - xpos14) + (y4pos - ypos14) * (y4pos - ypos14))
                            dix3.append(dst14)
                            dst15 = math.sqrt((x4pos - xpos15) * (x4pos - xpos15) + (y4pos - ypos15) * (y4pos - ypos15))
                            dix3.append(dst15)
                            dst16 = math.sqrt((x4pos - xpos16) * (x4pos - xpos16) + (y4pos - ypos16) * (y4pos - ypos16))
                            dix3.append(dst16)
                            dst17 = math.sqrt((x4pos - xpos17) * (x4pos - xpos17) + (y4pos - ypos17) * (y4pos - ypos17))
                            dix3.append(dst17)
                            dst18 = math.sqrt((x4pos - xpos18) * (x4pos - xpos18) + (y4pos - ypos18) * (y4pos - ypos18))
                            dix3.append(dst18)
                            dst19 = math.sqrt((x4pos - xpos19) * (x4pos - xpos19) + (y4pos - ypos19) * (y4pos - ypos19))
                            dix3.append(dst19)
                            dst20 = math.sqrt((x4pos - xpos20) * (x4pos - xpos20) + (y4pos - ypos20) * (y4pos - ypos20))
                            dix3.append(dst20)
                            dst21 = math.sqrt((x4pos - xpos21) * (x4pos - xpos21) + (y4pos - ypos21) * (y4pos - ypos21))
                            dix3.append(dst21)
                            dst22 = math.sqrt((x4pos - xpos22) * (x4pos - xpos22) + (y4pos - ypos22) * (y4pos - ypos22))
                            dix3.append(dst22)
                            dst23 = math.sqrt((x4pos - xpos23) * (x4pos - xpos23) + (y4pos - ypos23) * (y4pos - ypos23))
                            dix3.append(dst23)
                            dst24 = math.sqrt((x4pos - xpos24) * (x4pos - xpos24) + (y4pos - ypos24) * (y4pos - ypos24))
                            dix3.append(dst24)
                            dst25 = math.sqrt((x4pos - xpos25) * (x4pos - xpos25) + (y4pos - ypos25) * (y4pos - ypos25))
                            dix3.append(dst25)
                            for k in range(25):
                                if dix3[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x4pos, y4pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif cpr == 4:
                            dst1 = math.sqrt((x5pos - xpos1) * (x5pos - xpos1) + (y5pos - ypos1) * (y5pos - ypos1))
                            dix4.append(dst1)
                            dst2 = math.sqrt((x5pos - xpos2) * (x5pos - xpos2) + (y5pos - ypos2) * (y5pos - ypos2))
                            dix4.append(dst2)
                            dst3 = math.sqrt((x5pos - xpos3) * (x5pos - xpos3) + (y5pos - ypos3) * (y5pos - ypos3))
                            dix4.append(dst3)
                            dst4 = math.sqrt((x5pos - xpos4) * (x5pos - xpos4) + (y5pos - ypos4) * (y5pos - ypos4))
                            dix4.append(dst4)
                            dst5 = math.sqrt((x5pos - xpos5) * (x5pos - xpos5) + (y5pos - ypos5) * (y5pos - ypos5))
                            dix4.append(dst5)
                            dst6 = math.sqrt((x5pos - xpos6) * (x5pos - xpos6) + (y5pos - ypos6) * (y5pos - ypos6))
                            dix4.append(dst6)
                            dst7 = math.sqrt((x5pos - xpos7) * (x5pos - xpos7) + (y5pos - ypos7) * (y5pos - ypos7))
                            dix4.append(dst7)
                            dst8 = math.sqrt((x5pos - xpos8) * (x5pos - xpos8) + (y5pos - ypos8) * (y5pos - ypos8))
                            dix4.append(dst8)
                            dst9 = math.sqrt((x5pos - xpos9) * (x5pos - xpos9) + (y5pos - ypos9) * (y5pos - ypos9))
                            dix4.append(dst9)
                            dst10 = math.sqrt((x5pos - xpos10) * (x5pos - xpos10) + (y5pos - ypos10) * (y5pos - ypos10))
                            dix4.append(dst10)
                            dst11 = math.sqrt((x5pos - xpos11) * (x5pos - xpos11) + (y5pos - ypos11) * (y5pos - ypos11))
                            dix4.append(dst11)
                            dst12 = math.sqrt((x5pos - xpos12) * (x5pos - xpos12) + (y5pos - ypos12) * (y5pos - ypos12))
                            dix4.append(dst12)
                            dst13 = math.sqrt((x5pos - xpos13) * (x5pos - xpos13) + (y5pos - ypos13) * (y5pos - ypos13))
                            dix4.append(dst13)
                            dst14 = math.sqrt((x5pos - xpos14) * (x5pos - xpos14) + (y5pos - ypos14) * (y5pos - ypos14))
                            dix4.append(dst14)
                            dst15 = math.sqrt((x5pos - xpos15) * (x5pos - xpos15) + (y5pos - ypos15) * (y5pos - ypos15))
                            dix4.append(dst15)
                            dst16 = math.sqrt((x5pos - xpos16) * (x5pos - xpos16) + (y5pos - ypos16) * (y5pos - ypos16))
                            dix4.append(dst16)
                            dst17 = math.sqrt((x5pos - xpos17) * (x5pos - xpos17) + (y5pos - ypos17) * (y5pos - ypos17))
                            dix4.append(dst17)
                            dst18 = math.sqrt((x5pos - xpos18) * (x5pos - xpos18) + (y5pos - ypos18) * (y5pos - ypos18))
                            dix4.append(dst18)
                            dst19 = math.sqrt((x5pos - xpos19) * (x5pos - xpos19) + (y5pos - ypos19) * (y5pos - ypos19))
                            dix4.append(dst19)
                            dst20 = math.sqrt((x5pos - xpos20) * (x5pos - xpos20) + (y5pos - ypos20) * (y5pos - ypos20))
                            dix4.append(dst20)
                            dst21 = math.sqrt((x5pos - xpos21) * (x5pos - xpos21) + (y5pos - ypos21) * (y5pos - ypos21))
                            dix4.append(dst21)
                            dst22 = math.sqrt((x5pos - xpos22) * (x5pos - xpos22) + (y5pos - ypos22) * (y5pos - ypos22))
                            dix4.append(dst22)
                            dst23 = math.sqrt((x5pos - xpos23) * (x5pos - xpos23) + (y5pos - ypos23) * (y5pos - ypos23))
                            dix4.append(dst23)
                            dst24 = math.sqrt((x5pos - xpos24) * (x5pos - xpos24) + (y5pos - ypos24) * (y5pos - ypos24))
                            dix4.append(dst24)
                            dst25 = math.sqrt((x5pos - xpos25) * (x5pos - xpos25) + (y5pos - ypos25) * (y5pos - ypos25))
                            dix4.append(dst25)
                            for k in range(25):
                                if dix4[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x5pos, y5pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 5:
                            dst1 = math.sqrt((x6pos - xpos1) * (x6pos - xpos1) + (y6pos - ypos1) * (y6pos - ypos1))
                            dix5.append(dst1)
                            dst2 = math.sqrt((x6pos - xpos2) * (x6pos - xpos2) + (y6pos - ypos2) * (y6pos - ypos2))
                            dix5.append(dst2)
                            dst3 = math.sqrt((x6pos - xpos3) * (x6pos - xpos3) + (y6pos - ypos3) * (y6pos - ypos3))
                            dix5.append(dst3)
                            dst4 = math.sqrt((x6pos - xpos4) * (x6pos - xpos4) + (y6pos - ypos4) * (y6pos - ypos4))
                            dix5.append(dst4)
                            dst5 = math.sqrt((x6pos - xpos5) * (x6pos - xpos5) + (y6pos - ypos5) * (y6pos - ypos5))
                            dix5.append(dst5)
                            dst6 = math.sqrt((x6pos - xpos6) * (x6pos - xpos6) + (y6pos - ypos6) * (y6pos - ypos6))
                            dix5.append(dst6)
                            dst7 = math.sqrt((x6pos - xpos7) * (x6pos - xpos7) + (y6pos - ypos7) * (y6pos - ypos7))
                            dix5.append(dst7)
                            dst8 = math.sqrt((x6pos - xpos8) * (x6pos - xpos8) + (y6pos - ypos8) * (y6pos - ypos8))
                            dix5.append(dst8)
                            dst9 = math.sqrt((x6pos - xpos9) * (x6pos - xpos9) + (y6pos - ypos9) * (y6pos - ypos9))
                            dix5.append(dst9)
                            dst10 = math.sqrt((x6pos - xpos10) * (x6pos - xpos10) + (y6pos - ypos10) * (y6pos - ypos10))
                            dix5.append(dst10)
                            dst11 = math.sqrt((x6pos - xpos11) * (x6pos - xpos11) + (y6pos - ypos11) * (y6pos - ypos11))
                            dix5.append(dst11)
                            dst12 = math.sqrt((x6pos - xpos12) * (x6pos - xpos12) + (y6pos - ypos12) * (y6pos - ypos12))
                            dix5.append(dst12)
                            dst13 = math.sqrt((x6pos - xpos13) * (x6pos - xpos13) + (y6pos - ypos13) * (y6pos - ypos13))
                            dix5.append(dst13)
                            dst14 = math.sqrt((x6pos - xpos14) * (x6pos - xpos14) + (y6pos - ypos14) * (y6pos - ypos14))
                            dix5.append(dst14)
                            dst15 = math.sqrt((x6pos - xpos15) * (x6pos - xpos15) + (y6pos - ypos15) * (y6pos - ypos15))
                            dix5.append(dst15)
                            dst16 = math.sqrt((x6pos - xpos16) * (x6pos - xpos16) + (y6pos - ypos16) * (y6pos - ypos16))
                            dix5.append(dst16)
                            dst17 = math.sqrt((x6pos - xpos17) * (x6pos - xpos17) + (y6pos - ypos17) * (y6pos - ypos17))
                            dix5.append(dst17)
                            dst18 = math.sqrt((x6pos - xpos18) * (x6pos - xpos18) + (y6pos - ypos18) * (y6pos - ypos18))
                            dix5.append(dst18)
                            dst19 = math.sqrt((x6pos - xpos19) * (x6pos - xpos19) + (y6pos - ypos19) * (y6pos - ypos19))
                            dix5.append(dst19)
                            dst20 = math.sqrt((x6pos - xpos20) * (x6pos - xpos20) + (y6pos - ypos20) * (y6pos - ypos20))
                            dix5.append(dst20)
                            dst21 = math.sqrt((x6pos - xpos21) * (x6pos - xpos21) + (y6pos - ypos21) * (y6pos - ypos21))
                            dix5.append(dst21)
                            dst22 = math.sqrt((x6pos - xpos22) * (x6pos - xpos22) + (y6pos - ypos22) * (y6pos - ypos22))
                            dix5.append(dst22)
                            dst23 = math.sqrt((x6pos - xpos23) * (x6pos - xpos23) + (y6pos - ypos23) * (y6pos - ypos23))
                            dix5.append(dst23)
                            dst24 = math.sqrt((x6pos - xpos24) * (x6pos - xpos24) + (y6pos - ypos24) * (y6pos - ypos24))
                            dix5.append(dst24)
                            dst25 = math.sqrt((x6pos - xpos25) * (x6pos - xpos25) + (y6pos - ypos25) * (y6pos - ypos25))
                            dix5.append(dst25)
                            for k in range(25):
                                if dix5[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x6pos, y6pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 6:
                            dst1 = math.sqrt((x7pos - xpos1) * (x7pos - xpos1) + (y7pos - ypos1) * (y7pos - ypos1))
                            dix6.append(dst1)
                            dst2 = math.sqrt((x7pos - xpos2) * (x7pos - xpos2) + (y7pos - ypos2) * (y7pos - ypos2))
                            dix6.append(dst2)
                            dst3 = math.sqrt((x7pos - xpos3) * (x7pos - xpos3) + (y7pos - ypos3) * (y7pos - ypos3))
                            dix6.append(dst3)
                            dst4 = math.sqrt((x7pos - xpos4) * (x7pos - xpos4) + (y7pos - ypos4) * (y7pos - ypos4))
                            dix6.append(dst4)
                            dst5 = math.sqrt((x7pos - xpos5) * (x7pos - xpos5) + (y7pos - ypos5) * (y7pos - ypos5))
                            dix6.append(dst5)
                            dst6 = math.sqrt((x7pos - xpos6) * (x7pos - xpos6) + (y7pos - ypos6) * (y7pos - ypos6))
                            dix6.append(dst6)
                            dst7 = math.sqrt((x7pos - xpos7) * (x7pos - xpos7) + (y7pos - ypos7) * (y7pos - ypos7))
                            dix6.append(dst7)
                            dst8 = math.sqrt((x7pos - xpos8) * (x7pos - xpos8) + (y7pos - ypos8) * (y7pos - ypos8))
                            dix6.append(dst8)
                            dst9 = math.sqrt((x7pos - xpos9) * (x7pos - xpos9) + (y7pos - ypos9) * (y7pos - ypos9))
                            dix6.append(dst9)
                            dst10 = math.sqrt((x7pos - xpos10) * (x7pos - xpos10) + (y7pos - ypos10) * (y7pos - ypos10))
                            dix6.append(dst10)
                            dst11 = math.sqrt((x7pos - xpos11) * (x7pos - xpos11) + (y7pos - ypos11) * (y7pos - ypos11))
                            dix6.append(dst11)
                            dst12 = math.sqrt((x7pos - xpos12) * (x7pos - xpos12) + (y7pos - ypos12) * (y7pos - ypos12))
                            dix6.append(dst12)
                            dst13 = math.sqrt((x7pos - xpos13) * (x7pos - xpos13) + (y7pos - ypos13) * (y7pos - ypos13))
                            dix6.append(dst13)
                            dst14 = math.sqrt((x7pos - xpos14) * (x7pos - xpos14) + (y7pos - ypos14) * (y7pos - ypos14))
                            dix6.append(dst14)
                            dst15 = math.sqrt((x7pos - xpos15) * (x7pos - xpos15) + (y7pos - ypos15) * (y7pos - ypos15))
                            dix6.append(dst15)
                            dst16 = math.sqrt((x7pos - xpos16) * (x7pos - xpos16) + (y7pos - ypos16) * (y7pos - ypos16))
                            dix6.append(dst16)
                            dst17 = math.sqrt((x7pos - xpos17) * (x7pos - xpos17) + (y7pos - ypos17) * (y7pos - ypos17))
                            dix6.append(dst17)
                            dst18 = math.sqrt((x7pos - xpos18) * (x7pos - xpos18) + (y7pos - ypos18) * (y7pos - ypos18))
                            dix6.append(dst18)
                            dst19 = math.sqrt((x7pos - xpos19) * (x7pos - xpos19) + (y7pos - ypos19) * (y7pos - ypos19))
                            dix6.append(dst19)
                            dst20 = math.sqrt((x7pos - xpos20) * (x7pos - xpos20) + (y7pos - ypos20) * (y7pos - ypos20))
                            dix6.append(dst20)
                            dst21 = math.sqrt((x7pos - xpos21) * (x7pos - xpos21) + (y7pos - ypos21) * (y7pos - ypos21))
                            dix6.append(dst21)
                            dst22 = math.sqrt((x7pos - xpos22) * (x7pos - xpos22) + (y7pos - ypos22) * (y7pos - ypos22))
                            dix6.append(dst22)
                            dst23 = math.sqrt((x7pos - xpos23) * (x7pos - xpos23) + (y7pos - ypos23) * (y7pos - ypos23))
                            dix6.append(dst23)
                            dst24 = math.sqrt((x7pos - xpos24) * (x7pos - xpos24) + (y7pos - ypos24) * (y7pos - ypos24))
                            dix6.append(dst24)
                            dst25 = math.sqrt((x7pos - xpos25) * (x7pos - xpos25) + (y7pos - ypos25) * (y7pos - ypos25))
                            dix6.append(dst25)
                            for k in range(25):
                                if dix6[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x7pos, y7pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 7:
                            dst1 = math.sqrt((x8pos - xpos1) * (x8pos - xpos1) + (y8pos - ypos1) * (y8pos - ypos1))
                            dix7.append(dst1)
                            dst2 = math.sqrt((x8pos - xpos2) * (x8pos - xpos2) + (y8pos - ypos2) * (y8pos - ypos2))
                            dix7.append(dst2)
                            dst3 = math.sqrt((x8pos - xpos3) * (x8pos - xpos3) + (y8pos - ypos3) * (y8pos - ypos3))
                            dix7.append(dst3)
                            dst4 = math.sqrt((x8pos - xpos4) * (x8pos - xpos4) + (y8pos - ypos4) * (y8pos - ypos4))
                            dix7.append(dst4)
                            dst5 = math.sqrt((x8pos - xpos5) * (x8pos - xpos5) + (y8pos - ypos5) * (y8pos - ypos5))
                            dix7.append(dst5)
                            dst6 = math.sqrt((x8pos - xpos6) * (x8pos - xpos6) + (y8pos - ypos6) * (y8pos - ypos6))
                            dix7.append(dst6)
                            dst7 = math.sqrt((x8pos - xpos7) * (x8pos - xpos7) + (y8pos - ypos7) * (y8pos - ypos7))
                            dix7.append(dst7)
                            dst8 = math.sqrt((x8pos - xpos8) * (x8pos - xpos8) + (y8pos - ypos8) * (y8pos - ypos8))
                            dix7.append(dst8)
                            dst9 = math.sqrt((x8pos - xpos9) * (x8pos - xpos9) + (y8pos - ypos9) * (y8pos - ypos9))
                            dix7.append(dst9)
                            dst10 = math.sqrt((x8pos - xpos10) * (x8pos - xpos10) + (y8pos - ypos10) * (y8pos - ypos10))
                            dix7.append(dst10)
                            dst11 = math.sqrt((x8pos - xpos11) * (x8pos - xpos11) + (y8pos - ypos11) * (y8pos - ypos11))
                            dix7.append(dst11)
                            dst12 = math.sqrt((x8pos - xpos12) * (x8pos - xpos12) + (y8pos - ypos12) * (y8pos - ypos12))
                            dix7.append(dst12)
                            dst13 = math.sqrt((x8pos - xpos13) * (x8pos - xpos13) + (y8pos - ypos13) * (y8pos - ypos13))
                            dix7.append(dst13)
                            dst14 = math.sqrt((x8pos - xpos14) * (x8pos - xpos14) + (y8pos - ypos14) * (y8pos - ypos14))
                            dix7.append(dst14)
                            dst15 = math.sqrt((x8pos - xpos15) * (x8pos - xpos15) + (y8pos - ypos15) * (y8pos - ypos15))
                            dix7.append(dst15)
                            dst16 = math.sqrt((x8pos - xpos16) * (x8pos - xpos16) + (y8pos - ypos16) * (y8pos - ypos16))
                            dix7.append(dst16)
                            dst17 = math.sqrt((x8pos - xpos17) * (x8pos - xpos17) + (y8pos - ypos17) * (y8pos - ypos17))
                            dix7.append(dst17)
                            dst18 = math.sqrt((x8pos - xpos18) * (x8pos - xpos18) + (y8pos - ypos18) * (y8pos - ypos18))
                            dix7.append(dst18)
                            dst19 = math.sqrt((x8pos - xpos19) * (x8pos - xpos19) + (y8pos - ypos19) * (y8pos - ypos19))
                            dix7.append(dst19)
                            dst20 = math.sqrt((x8pos - xpos20) * (x8pos - xpos20) + (y8pos - ypos20) * (y8pos - ypos20))
                            dix7.append(dst20)
                            dst21 = math.sqrt((x8pos - xpos21) * (x8pos - xpos21) + (y8pos - ypos21) * (y8pos - ypos21))
                            dix7.append(dst21)
                            dst22 = math.sqrt((x8pos - xpos22) * (x8pos - xpos22) + (y8pos - ypos22) * (y8pos - ypos22))
                            dix7.append(dst22)
                            dst23 = math.sqrt((x8pos - xpos23) * (x8pos - xpos23) + (y1pos - ypos23) * (y8pos - ypos23))
                            dix7.append(dst23)
                            dst24 = math.sqrt((x8pos - xpos24) * (x8pos - xpos24) + (y1pos - ypos24) * (y8pos - ypos24))
                            dix7.append(dst24)
                            dst25 = math.sqrt((x8pos - xpos25) * (x8pos - xpos25) + (y1pos - ypos25) * (y8pos - ypos25))
                            dix7.append(dst25)
                            for k in range(25):
                                if dix7[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x8pos, y8pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 8:
                            dst1 = math.sqrt((x9pos - xpos1) * (x9pos - xpos1) + (y9pos - ypos1) * (y9pos - ypos1))
                            dix8.append(dst1)
                            dst2 = math.sqrt((x9pos - xpos2) * (x9pos - xpos2) + (y9pos - ypos2) * (y9pos - ypos2))
                            dix8.append(dst2)
                            dst3 = math.sqrt((x9pos - xpos3) * (x9pos - xpos3) + (y9pos - ypos3) * (y9pos - ypos3))
                            dix8.append(dst3)
                            dst4 = math.sqrt((x9pos - xpos4) * (x9pos - xpos4) + (y9pos - ypos4) * (y9pos - ypos4))
                            dix8.append(dst4)
                            dst5 = math.sqrt((x9pos - xpos5) * (x9pos - xpos5) + (y9pos - ypos5) * (y9pos - ypos5))
                            dix8.append(dst5)
                            dst6 = math.sqrt((x9pos - xpos6) * (x9pos - xpos6) + (y9pos - ypos6) * (y9pos - ypos6))
                            dix8.append(dst6)
                            dst7 = math.sqrt((x9pos - xpos7) * (x9pos - xpos7) + (y9pos - ypos7) * (y9pos - ypos7))
                            dix8.append(dst7)
                            dst8 = math.sqrt((x9pos - xpos8) * (x9pos - xpos8) + (y9pos - ypos8) * (y9pos - ypos8))
                            dix8.append(dst8)
                            dst9 = math.sqrt((x9pos - xpos9) * (x9pos - xpos9) + (y9pos - ypos9) * (y9pos - ypos9))
                            dix8.append(dst9)
                            dst10 = math.sqrt((x9pos - xpos10) * (x9pos - xpos10) + (y9pos - ypos10) * (y9pos - ypos10))
                            dix8.append(dst10)
                            dst11 = math.sqrt((x9pos - xpos11) * (x9pos - xpos11) + (y9pos - ypos11) * (y9pos - ypos11))
                            dix8.append(dst11)
                            dst12 = math.sqrt((x9pos - xpos12) * (x9pos - xpos12) + (y9pos - ypos12) * (y9pos - ypos12))
                            dix8.append(dst12)
                            dst13 = math.sqrt((x9pos - xpos13) * (x9pos - xpos13) + (y9pos - ypos13) * (y9pos - ypos13))
                            dix8.append(dst13)
                            dst14 = math.sqrt((x9pos - xpos14) * (x9pos - xpos14) + (y9pos - ypos14) * (y9pos - ypos14))
                            dix8.append(dst14)
                            dst15 = math.sqrt((x9pos - xpos15) * (x9pos - xpos15) + (y9pos - ypos15) * (y9pos - ypos15))
                            dix8.append(dst15)
                            dst16 = math.sqrt((x9pos - xpos16) * (x9pos - xpos16) + (y9pos - ypos16) * (y9pos - ypos16))
                            dix8.append(dst16)
                            dst17 = math.sqrt((x9pos - xpos17) * (x9pos - xpos17) + (y9pos - ypos17) * (y9pos - ypos17))
                            dix8.append(dst17)
                            dst18 = math.sqrt((x9pos - xpos18) * (x9pos - xpos18) + (y9pos - ypos18) * (y9pos - ypos18))
                            dix8.append(dst18)
                            dst19 = math.sqrt((x9pos - xpos19) * (x9pos - xpos19) + (y9pos - ypos19) * (y9pos - ypos19))
                            dix8.append(dst19)
                            dst20 = math.sqrt((x9pos - xpos20) * (x9pos - xpos20) + (y9pos - ypos20) * (y9pos - ypos20))
                            dix8.append(dst20)
                            dst21 = math.sqrt((x9pos - xpos21) * (x9pos - xpos21) + (y9pos - ypos21) * (y9pos - ypos21))
                            dix8.append(dst21)
                            dst22 = math.sqrt((x9pos - xpos22) * (x9pos - xpos22) + (y9pos - ypos22) * (y9pos - ypos22))
                            dix8.append(dst22)
                            dst23 = math.sqrt((x9pos - xpos23) * (x9pos - xpos23) + (y9pos - ypos23) * (y9pos - ypos23))
                            dix8.append(dst23)
                            dst24 = math.sqrt((x9pos - xpos24) * (x9pos - xpos24) + (y9pos - ypos24) * (y9pos - ypos24))
                            dix8.append(dst24)
                            dst25 = math.sqrt((x9pos - xpos25) * (x9pos - xpos25) + (y9pos - ypos25) * (y9pos - ypos25))
                            dix8.append(dst25)
                            for k in range(25):
                                if dix8[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x9pos, y9pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 9:
                            dst1 = math.sqrt((x10pos - xpos1) * (x10pos - xpos1) + (y10pos - ypos1) * (y10pos - ypos1))
                            dix9.append(dst1)
                            dst2 = math.sqrt((x10pos - xpos2) * (x10pos - xpos2) + (y10pos - ypos2) * (y10pos - ypos2))
                            dix9.append(dst2)
                            dst3 = math.sqrt((x10pos - xpos3) * (x10pos - xpos3) + (y10pos - ypos3) * (y10pos - ypos3))
                            dix9.append(dst3)
                            dst4 = math.sqrt((x10pos - xpos4) * (x10pos - xpos4) + (y10pos - ypos4) * (y10pos - ypos4))
                            dix9.append(dst4)
                            dst5 = math.sqrt((x10pos - xpos5) * (x10pos - xpos5) + (y10pos - ypos5) * (y10pos - ypos5))
                            dix9.append(dst5)
                            dst6 = math.sqrt((x10pos - xpos6) * (x10pos - xpos6) + (y10pos - ypos6) * (y10pos - ypos6))
                            dix9.append(dst6)
                            dst7 = math.sqrt((x10pos - xpos7) * (x10pos - xpos7) + (y10pos - ypos7) * (y10pos - ypos7))
                            dix9.append(dst7)
                            dst8 = math.sqrt((x10pos - xpos8) * (x10pos - xpos8) + (y10pos - ypos8) * (y10pos - ypos8))
                            dix9.append(dst8)
                            dst9 = math.sqrt((x10pos - xpos9) * (x10pos - xpos9) + (y10pos - ypos9) * (y10pos - ypos9))
                            dix9.append(dst9)
                            dst10 = math.sqrt((x10pos - xpos10) * (x10pos - xpos10) + (y10pos - ypos10) * (y10pos - ypos10))
                            dix9.append(dst10)
                            dst11 = math.sqrt((x10pos - xpos11) * (x10pos - xpos11) + (y10pos - ypos11) * (y10pos - ypos11))
                            dix9.append(dst11)
                            dst12 = math.sqrt((x10pos - xpos12) * (x10pos - xpos12) + (y10pos - ypos12) * (y10pos - ypos12))
                            dix9.append(dst12)
                            dst13 = math.sqrt((x10pos - xpos13) * (x10pos - xpos13) + (y10pos - ypos13) * (y10pos - ypos13))
                            dix9.append(dst13)
                            dst14 = math.sqrt((x10pos - xpos14) * (x10pos - xpos14) + (y10pos - ypos14) * (y10pos - ypos14))
                            dix9.append(dst14)
                            dst15 = math.sqrt((x10pos - xpos15) * (x10pos - xpos15) + (y10pos - ypos15) * (y10pos - ypos15))
                            dix9.append(dst15)
                            dst16 = math.sqrt((x10pos - xpos16) * (x10pos - xpos16) + (y10pos - ypos16) * (y10pos - ypos16))
                            dix9.append(dst16)
                            dst17 = math.sqrt((x10pos - xpos17) * (x10pos - xpos17) + (y10pos - ypos17) * (y10pos - ypos17))
                            dix9.append(dst17)
                            dst18 = math.sqrt((x10pos - xpos18) * (x10pos - xpos18) + (y10pos - ypos18) * (y10pos - ypos18))
                            dix9.append(dst18)
                            dst19 = math.sqrt((x10pos - xpos19) * (x10pos - xpos19) + (y10pos - ypos19) * (y10pos - ypos19))
                            dix9.append(dst19)
                            dst20 = math.sqrt((x10pos - xpos20) * (x10pos - xpos20) + (y10pos - ypos20) * (y10pos - ypos20))
                            dix9.append(dst20)
                            dst21 = math.sqrt((x10pos - xpos21) * (x10pos - xpos21) + (y10pos - ypos21) * (y10pos - ypos21))
                            dix9.append(dst21)
                            dst22 = math.sqrt((x10pos - xpos22) * (x10pos - xpos22) + (y10pos - ypos22) * (y10pos - ypos22))
                            dix9.append(dst22)
                            dst23 = math.sqrt((x10pos - xpos23) * (x10pos - xpos23) + (y10pos - ypos23) * (y10pos - ypos23))
                            dix9.append(dst23)
                            dst24 = math.sqrt((x10pos - xpos24) * (x10pos - xpos24) + (y10pos - ypos24) * (y10pos - ypos24))
                            dix9.append(dst24)
                            dst25 = math.sqrt((x10pos - xpos25) * (x10pos - xpos25) + (y10pos - ypos25) * (y10pos - ypos25))
                            dix9.append(dst25)
                            for k in range(25):
                                if dix9[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x10pos, y10pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 10:
                            dst1 = math.sqrt((x11pos - xpos1) * (x11pos - xpos1) + (y11pos - ypos1) * (y11pos - ypos1))
                            dix10.append(dst1)
                            dst2 = math.sqrt((x11pos - xpos2) * (x11pos - xpos2) + (y11pos - ypos2) * (y11pos - ypos2))
                            dix10.append(dst2)
                            dst3 = math.sqrt((x11pos - xpos3) * (x11pos - xpos3) + (y11pos - ypos3) * (y11pos - ypos3))
                            dix10.append(dst3)
                            dst4 = math.sqrt((x11pos - xpos4) * (x11pos - xpos4) + (y11pos - ypos4) * (y11pos - ypos4))
                            dix10.append(dst4)
                            dst5 = math.sqrt((x11pos - xpos5) * (x11pos - xpos5) + (y11pos - ypos5) * (y11pos - ypos5))
                            dix10.append(dst5)
                            dst6 = math.sqrt((x11pos - xpos6) * (x11pos - xpos6) + (y11pos - ypos6) * (y11pos - ypos6))
                            dix10.append(dst6)
                            dst7 = math.sqrt((x11pos - xpos7) * (x11pos - xpos7) + (y11pos - ypos7) * (y11pos - ypos7))
                            dix10.append(dst7)
                            dst8 = math.sqrt((x11pos - xpos8) * (x11pos - xpos8) + (y11pos - ypos8) * (y11pos - ypos8))
                            dix10.append(dst8)
                            dst9 = math.sqrt((x11pos - xpos9) * (x11pos - xpos9) + (y11pos - ypos9) * (y11pos - ypos9))
                            dix10.append(dst9)
                            dst10 = math.sqrt((x11pos - xpos10) * (x11pos - xpos10) + (y11pos - ypos10) * (y11pos - ypos10))
                            dix10.append(dst10)
                            dst11 = math.sqrt((x11pos - xpos11) * (x11pos - xpos11) + (y11pos - ypos11) * (y11pos - ypos11))
                            dix10.append(dst11)
                            dst12 = math.sqrt((x11pos - xpos12) * (x11pos - xpos12) + (y11pos - ypos12) * (y11pos - ypos12))
                            dix10.append(dst12)
                            dst13 = math.sqrt((x11pos - xpos13) * (x11pos - xpos13) + (y11pos - ypos13) * (y11pos - ypos13))
                            dix10.append(dst13)
                            dst14 = math.sqrt((x11pos - xpos14) * (x11pos - xpos14) + (y11pos - ypos14) * (y11pos - ypos14))
                            dix10.append(dst14)
                            dst15 = math.sqrt((x11pos - xpos15) * (x11pos - xpos15) + (y11pos - ypos15) * (y11pos - ypos15))
                            dix10.append(dst15)
                            dst16 = math.sqrt((x11pos - xpos16) * (x11pos - xpos16) + (y11pos - ypos16) * (y11pos - ypos16))
                            dix10.append(dst16)
                            dst17 = math.sqrt((x11pos - xpos17) * (x11pos - xpos17) + (y11pos - ypos17) * (y11pos - ypos17))
                            dix10.append(dst17)
                            dst18 = math.sqrt((x11pos - xpos18) * (x11pos - xpos18) + (y11pos - ypos18) * (y11pos - ypos18))
                            dix10.append(dst18)
                            dst19 = math.sqrt((x11pos - xpos19) * (x11pos - xpos19) + (y11pos - ypos19) * (y11pos - ypos19))
                            dix10.append(dst19)
                            dst20 = math.sqrt((x11pos - xpos20) * (x11pos - xpos20) + (y11pos - ypos20) * (y11pos - ypos20))
                            dix10.append(dst20)
                            dst21 = math.sqrt((x11pos - xpos21) * (x11pos - xpos21) + (y11pos - ypos21) * (y11pos - ypos21))
                            dix10.append(dst21)
                            dst22 = math.sqrt((x11pos - xpos22) * (x11pos - xpos22) + (y11pos - ypos22) * (y11pos - ypos22))
                            dix10.append(dst22)
                            dst23 = math.sqrt((x11pos - xpos23) * (x11pos - xpos23) + (y11pos - ypos23) * (y11pos - ypos23))
                            dix10.append(dst23)
                            dst24 = math.sqrt((x11pos - xpos24) * (x11pos - xpos24) + (y11pos - ypos24) * (y11pos - ypos24))
                            dix10.append(dst24)
                            dst25 = math.sqrt((x11pos - xpos25) * (x11pos - xpos25) + (y11pos - ypos25) * (y11pos - ypos25))
                            dix10.append(dst25)
                            for k in range(25):
                                if dix10[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x11pos, y11pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 11:
                            dst1 = math.sqrt((x12pos - xpos1) * (x12pos - xpos1) + (y12pos - ypos1) * (y12pos - ypos1))
                            dix11.append(dst1)
                            dst2 = math.sqrt((x12pos - xpos2) * (x12pos - xpos2) + (y12pos - ypos2) * (y12pos - ypos2))
                            dix11.append(dst2)
                            dst3 = math.sqrt((x12pos - xpos3) * (x12pos - xpos3) + (y12pos - ypos3) * (y12pos - ypos3))
                            dix11.append(dst3)
                            dst4 = math.sqrt((x12pos - xpos4) * (x12pos - xpos4) + (y12pos - ypos4) * (y12pos - ypos4))
                            dix11.append(dst4)
                            dst5 = math.sqrt((x12pos - xpos5) * (x12pos - xpos5) + (y12pos - ypos5) * (y12pos - ypos5))
                            dix11.append(dst5)
                            dst6 = math.sqrt((x12pos - xpos6) * (x12pos - xpos6) + (y12pos - ypos6) * (y12pos - ypos6))
                            dix11.append(dst6)
                            dst7 = math.sqrt((x12pos - xpos7) * (x12pos - xpos7) + (y12pos - ypos7) * (y12pos - ypos7))
                            dix11.append(dst7)
                            dst8 = math.sqrt((x12pos - xpos8) * (x12pos - xpos8) + (y12pos - ypos8) * (y12pos - ypos8))
                            dix11.append(dst8)
                            dst9 = math.sqrt((x12pos - xpos9) * (x12pos - xpos9) + (y12pos - ypos9) * (y12pos - ypos9))
                            dix11.append(dst9)
                            dst10 = math.sqrt((x12pos - xpos10) * (x12pos - xpos10) + (y12pos - ypos10) * (y12pos - ypos10))
                            dix11.append(dst10)
                            dst11 = math.sqrt((x12pos - xpos11) * (x12pos - xpos11) + (y12pos - ypos11) * (y12pos - ypos11))
                            dix11.append(dst11)
                            dst12 = math.sqrt((x12pos - xpos12) * (x12pos - xpos12) + (y12pos - ypos12) * (y12pos - ypos12))
                            dix11.append(dst12)
                            dst13 = math.sqrt((x12pos - xpos13) * (x12pos - xpos13) + (y12pos - ypos13) * (y12pos - ypos13))
                            dix11.append(dst13)
                            dst14 = math.sqrt((x12pos - xpos14) * (x12pos - xpos14) + (y12pos - ypos14) * (y12pos - ypos14))
                            dix11.append(dst14)
                            dst15 = math.sqrt((x12pos - xpos15) * (x12pos - xpos15) + (y12pos - ypos15) * (y12pos - ypos15))
                            dix11.append(dst15)
                            dst16 = math.sqrt((x12pos - xpos16) * (x12pos - xpos16) + (y12pos - ypos16) * (y12pos - ypos16))
                            dix11.append(dst16)
                            dst17 = math.sqrt((x12pos - xpos17) * (x12pos - xpos17) + (y12pos - ypos17) * (y12pos - ypos17))
                            dix11.append(dst17)
                            dst18 = math.sqrt((x12pos - xpos18) * (x12pos - xpos18) + (y12pos - ypos18) * (y12pos - ypos18))
                            dix11.append(dst18)
                            dst19 = math.sqrt((x12pos - xpos19) * (x12pos - xpos19) + (y12pos - ypos19) * (y12pos - ypos19))
                            dix11.append(dst19)
                            dst20 = math.sqrt((x12pos - xpos20) * (x12pos - xpos20) + (y12pos - ypos20) * (y12pos - ypos20))
                            dix11.append(dst20)
                            dst21 = math.sqrt((x12pos - xpos21) * (x12pos - xpos21) + (y12pos - ypos21) * (y12pos - ypos21))
                            dix11.append(dst21)
                            dst22 = math.sqrt((x12pos - xpos22) * (x12pos - xpos22) + (y12pos - ypos22) * (y12pos - ypos22))
                            dix11.append(dst22)
                            dst23 = math.sqrt((x12pos - xpos23) * (x12pos - xpos23) + (y12pos - ypos23) * (y12pos - ypos23))
                            dix11.append(dst23)
                            dst24 = math.sqrt((x12pos - xpos24) * (x12pos - xpos24) + (y12pos - ypos24) * (y12pos - ypos24))
                            dix11.append(dst24)
                            dst25 = math.sqrt((x12pos - xpos25) * (x12pos - xpos25) + (y12pos - ypos25) * (y12pos - ypos25))
                            dix11.append(dst25)
                            for k in range(25):
                                if dix11[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x12pos, y12pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 12:
                            dst1 = math.sqrt((x13pos - xpos1) * (x13pos - xpos1) + (y13pos - ypos1) * (y13pos - ypos1))
                            dix12.append(dst1)
                            dst2 = math.sqrt((x13pos - xpos2) * (x13pos - xpos2) + (y13pos - ypos2) * (y13pos - ypos2))
                            dix12.append(dst2)
                            dst3 = math.sqrt((x13pos - xpos3) * (x13pos - xpos3) + (y13pos - ypos3) * (y13pos - ypos3))
                            dix12.append(dst3)
                            dst4 = math.sqrt((x13pos - xpos4) * (x13pos - xpos4) + (y13pos - ypos4) * (y13pos - ypos4))
                            dix12.append(dst4)
                            dst5 = math.sqrt((x13pos - xpos5) * (x13pos - xpos5) + (y13pos - ypos5) * (y13pos - ypos5))
                            dix12.append(dst5)
                            dst6 = math.sqrt((x13pos - xpos6) * (x13pos - xpos6) + (y13pos - ypos6) * (y13pos - ypos6))
                            dix12.append(dst6)
                            dst7 = math.sqrt((x13pos - xpos7) * (x13pos - xpos7) + (y13pos - ypos7) * (y13pos - ypos7))
                            dix12.append(dst7)
                            dst8 = math.sqrt((x13pos - xpos8) * (x13pos - xpos8) + (y13pos - ypos8) * (y13pos - ypos8))
                            dix12.append(dst8)
                            dst9 = math.sqrt((x13pos - xpos9) * (x13pos - xpos9) + (y13pos - ypos9) * (y13pos - ypos9))
                            dix12.append(dst9)
                            dst10 = math.sqrt((x13pos - xpos10) * (x13pos - xpos10) + (y13pos - ypos10) * (y13pos - ypos10))
                            dix12.append(dst10)
                            dst11 = math.sqrt((x13pos - xpos11) * (x13pos - xpos11) + (y13pos - ypos11) * (y13pos - ypos11))
                            dix12.append(dst11)
                            dst12 = math.sqrt((x13pos - xpos12) * (x13pos - xpos12) + (y13pos - ypos12) * (y13pos - ypos12))
                            dix12.append(dst12)
                            dst13 = math.sqrt((x13pos - xpos13) * (x13pos - xpos13) + (y13pos - ypos13) * (y13pos - ypos13))
                            dix12.append(dst13)
                            dst14 = math.sqrt((x13pos - xpos14) * (x13pos - xpos14) + (y13pos - ypos14) * (y13pos - ypos14))
                            dix12.append(dst14)
                            dst15 = math.sqrt((x13pos - xpos15) * (x13pos - xpos15) + (y13pos - ypos15) * (y13pos - ypos15))
                            dix12.append(dst15)
                            dst16 = math.sqrt((x13pos - xpos16) * (x13pos - xpos16) + (y13pos - ypos16) * (y13pos - ypos16))
                            dix12.append(dst16)
                            dst17 = math.sqrt((x13pos - xpos17) * (x13pos - xpos17) + (y13pos - ypos17) * (y13pos - ypos17))
                            dix12.append(dst17)
                            dst18 = math.sqrt((x13pos - xpos18) * (x13pos - xpos18) + (y13pos - ypos18) * (y13pos - ypos18))
                            dix12.append(dst18)
                            dst19 = math.sqrt((x13pos - xpos19) * (x13pos - xpos19) + (y13pos - ypos19) * (y13pos - ypos19))
                            dix12.append(dst19)
                            dst20 = math.sqrt((x13pos - xpos20) * (x13pos - xpos20) + (y13pos - ypos20) * (y13pos - ypos20))
                            dix12.append(dst20)
                            dst21 = math.sqrt((x13pos - xpos21) * (x13pos - xpos21) + (y13pos - ypos21) * (y13pos - ypos21))
                            dix12.append(dst21)
                            dst22 = math.sqrt((x13pos - xpos22) * (x13pos - xpos22) + (y13pos - ypos22) * (y13pos - ypos22))
                            dix12.append(dst22)
                            dst23 = math.sqrt((x13pos - xpos23) * (x13pos - xpos23) + (y13pos - ypos23) * (y13pos - ypos23))
                            dix12.append(dst23)
                            dst24 = math.sqrt((x13pos - xpos24) * (x13pos - xpos24) + (y13pos - ypos24) * (y13pos - ypos24))
                            dix12.append(dst24)
                            dst25 = math.sqrt((x13pos - xpos25) * (x13pos - xpos25) + (y13pos - ypos25) * (y13pos - ypos25))
                            dix12.append(dst25)
                            for k in range(25):
                                if dix12[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x13pos, y13pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 13:
                            dst1 = math.sqrt((x14pos - xpos1) * (x14pos - xpos1) + (y14pos - ypos1) * (y14pos - ypos1))
                            dix13.append(dst1)
                            dst2 = math.sqrt((x14pos - xpos2) * (x14pos - xpos2) + (y14pos - ypos2) * (y14pos - ypos2))
                            dix13.append(dst2)
                            dst3 = math.sqrt((x14pos - xpos3) * (x14pos - xpos3) + (y14pos - ypos3) * (y14pos - ypos3))
                            dix13.append(dst3)
                            dst4 = math.sqrt((x14pos - xpos4) * (x14pos - xpos4) + (y14pos - ypos4) * (y14pos - ypos4))
                            dix13.append(dst4)
                            dst5 = math.sqrt((x14pos - xpos5) * (x14pos - xpos5) + (y14pos - ypos5) * (y14pos - ypos5))
                            dix13.append(dst5)
                            dst6 = math.sqrt((x14pos - xpos6) * (x14pos - xpos6) + (y14pos - ypos6) * (y14pos - ypos6))
                            dix13.append(dst6)
                            dst7 = math.sqrt((x14pos - xpos7) * (x14pos - xpos7) + (y14pos - ypos7) * (y14pos - ypos7))
                            dix13.append(dst7)
                            dst8 = math.sqrt((x14pos - xpos8) * (x14pos - xpos8) + (y14pos - ypos8) * (y14pos - ypos8))
                            dix13.append(dst8)
                            dst9 = math.sqrt((x14pos - xpos9) * (x14pos - xpos9) + (y14pos - ypos9) * (y14pos - ypos9))
                            dix13.append(dst9)
                            dst10 = math.sqrt((x14pos - xpos10) * (x14pos - xpos10) + (y14pos - ypos10) * (y14pos - ypos10))
                            dix13.append(dst10)
                            dst11 = math.sqrt((x14pos - xpos11) * (x14pos - xpos11) + (y14pos - ypos11) * (y14pos - ypos11))
                            dix13.append(dst11)
                            dst12 = math.sqrt((x14pos - xpos12) * (x14pos - xpos12) + (y14pos - ypos12) * (y14pos - ypos12))
                            dix13.append(dst12)
                            dst13 = math.sqrt((x14pos - xpos13) * (x14pos - xpos13) + (y14pos - ypos13) * (y14pos - ypos13))
                            dix13.append(dst13)
                            dst14 = math.sqrt((x14pos - xpos14) * (x14pos - xpos14) + (y14pos - ypos14) * (y14pos - ypos14))
                            dix13.append(dst14)
                            dst15 = math.sqrt((x14pos - xpos15) * (x14pos - xpos15) + (y14pos - ypos15) * (y14pos - ypos15))
                            dix13.append(dst15)
                            dst16 = math.sqrt((x14pos - xpos16) * (x14pos - xpos16) + (y14pos - ypos16) * (y14pos - ypos16))
                            dix13.append(dst16)
                            dst17 = math.sqrt((x14pos - xpos17) * (x14pos - xpos17) + (y14pos - ypos17) * (y14pos - ypos17))
                            dix13.append(dst17)
                            dst18 = math.sqrt((x14pos - xpos18) * (x14pos - xpos18) + (y14pos - ypos18) * (y14pos - ypos18))
                            dix13.append(dst18)
                            dst19 = math.sqrt((x14pos - xpos19) * (x14pos - xpos19) + (y14pos - ypos19) * (y14pos - ypos19))
                            dix13.append(dst19)
                            dst20 = math.sqrt((x14pos - xpos20) * (x14pos - xpos20) + (y14pos - ypos20) * (y14pos - ypos20))
                            dix13.append(dst20)
                            dst21 = math.sqrt((x14pos - xpos21) * (x14pos - xpos21) + (y14pos - ypos21) * (y14pos - ypos21))
                            dix13.append(dst21)
                            dst22 = math.sqrt((x14pos - xpos22) * (x14pos - xpos22) + (y14pos - ypos22) * (y14pos - ypos22))
                            dix13.append(dst22)
                            dst23 = math.sqrt((x14pos - xpos23) * (x14pos - xpos23) + (y14pos - ypos23) * (y14pos - ypos23))
                            dix13.append(dst23)
                            dst24 = math.sqrt((x14pos - xpos24) * (x14pos - xpos24) + (y14pos - ypos24) * (y14pos - ypos24))
                            dix13.append(dst24)
                            dst25 = math.sqrt((x14pos - xpos25) * (x14pos - xpos25) + (y14pos - ypos25) * (y14pos - ypos25))
                            dix13.append(dst25)
                            for k in range(25):
                                if dix13[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x14pos, y14pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 14:
                            dst1 = math.sqrt((x15pos - xpos1) * (x15pos - xpos1) + (y15pos - ypos1) * (y15pos - ypos1))
                            dix14.append(dst1)
                            dst2 = math.sqrt((x15pos - xpos2) * (x15pos - xpos2) + (y15pos - ypos2) * (y15pos - ypos2))
                            dix14.append(dst2)
                            dst3 = math.sqrt((x15pos - xpos3) * (x15pos - xpos3) + (y15pos - ypos3) * (y15pos - ypos3))
                            dix14.append(dst3)
                            dst4 = math.sqrt((x15pos - xpos4) * (x15pos - xpos4) + (y15pos - ypos4) * (y15pos - ypos4))
                            dix14.append(dst4)
                            dst5 = math.sqrt((x15pos - xpos5) * (x15pos - xpos5) + (y15pos - ypos5) * (y15pos - ypos5))
                            dix14.append(dst5)
                            dst6 = math.sqrt((x15pos - xpos6) * (x15pos - xpos6) + (y15pos - ypos6) * (y15pos - ypos6))
                            dix14.append(dst6)
                            dst7 = math.sqrt((x15pos - xpos7) * (x15pos - xpos7) + (y15pos - ypos7) * (y15pos - ypos7))
                            dix14.append(dst7)
                            dst8 = math.sqrt((x15pos - xpos8) * (x15pos - xpos8) + (y15pos - ypos8) * (y15pos - ypos8))
                            dix14.append(dst8)
                            dst9 = math.sqrt((x15pos - xpos9) * (x15pos - xpos9) + (y15pos - ypos9) * (y15pos - ypos9))
                            dix14.append(dst9)
                            dst10 = math.sqrt((x15pos - xpos10) * (x15pos - xpos10) + (y15pos - ypos10) * (y15pos - ypos10))
                            dix14.append(dst10)
                            dst11 = math.sqrt((x15pos - xpos11) * (x15pos - xpos11) + (y15pos - ypos11) * (y15pos - ypos11))
                            dix14.append(dst11)
                            dst12 = math.sqrt((x15pos - xpos12) * (x15pos - xpos12) + (y15pos - ypos12) * (y15pos - ypos12))
                            dix14.append(dst12)
                            dst13 = math.sqrt((x15pos - xpos13) * (x15pos - xpos13) + (y15pos - ypos13) * (y15pos - ypos13))
                            dix14.append(dst13)
                            dst14 = math.sqrt((x15pos - xpos14) * (x15pos - xpos14) + (y15pos - ypos14) * (y15pos - ypos14))
                            dix14.append(dst14)
                            dst15 = math.sqrt((x15pos - xpos15) * (x15pos - xpos15) + (y15pos - ypos15) * (y15pos - ypos15))
                            dix14.append(dst15)
                            dst16 = math.sqrt((x15pos - xpos16) * (x15pos - xpos16) + (y15pos - ypos16) * (y15pos - ypos16))
                            dix14.append(dst16)
                            dst17 = math.sqrt((x15pos - xpos17) * (x15pos - xpos17) + (y15pos - ypos17) * (y15pos - ypos17))
                            dix14.append(dst17)
                            dst18 = math.sqrt((x15pos - xpos18) * (x15pos - xpos18) + (y15pos - ypos18) * (y15pos - ypos18))
                            dix14.append(dst18)
                            dst19 = math.sqrt((x15pos - xpos19) * (x15pos - xpos19) + (y15pos - ypos19) * (y15pos - ypos19))
                            dix14.append(dst19)
                            dst20 = math.sqrt((x15pos - xpos20) * (x15pos - xpos20) + (y15pos - ypos20) * (y15pos - ypos20))
                            dix14.append(dst20)
                            dst21 = math.sqrt((x15pos - xpos21) * (x15pos - xpos21) + (y15pos - ypos21) * (y15pos - ypos21))
                            dix14.append(dst21)
                            dst22 = math.sqrt((x15pos - xpos22) * (x15pos - xpos22) + (y15pos - ypos22) * (y15pos - ypos22))
                            dix14.append(dst22)
                            dst23 = math.sqrt((x15pos - xpos23) * (x15pos - xpos23) + (y15pos - ypos23) * (y15pos - ypos23))
                            dix14.append(dst23)
                            dst24 = math.sqrt((x15pos - xpos24) * (x15pos - xpos24) + (y15pos - ypos24) * (y15pos - ypos24))
                            dix14.append(dst24)
                            dst25 = math.sqrt((x15pos - xpos25) * (x15pos - xpos25) + (y15pos - ypos25) * (y15pos - ypos25))
                            dix14.append(dst25)
                            for k in range(25):
                                if dix14[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x15pos, y15pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 15:
                            dst1 = math.sqrt((x16pos - xpos1) * (x16pos - xpos1) + (y16pos - ypos1) * (y16pos - ypos1))
                            dix15.append(dst1)
                            dst2 = math.sqrt((x16pos - xpos2) * (x16pos - xpos2) + (y16pos - ypos2) * (y16pos - ypos2))
                            dix15.append(dst2)
                            dst3 = math.sqrt((x16pos - xpos3) * (x16pos - xpos3) + (y16pos - ypos3) * (y16pos - ypos3))
                            dix15.append(dst3)
                            dst4 = math.sqrt((x16pos - xpos4) * (x16pos - xpos4) + (y16pos - ypos4) * (y16pos - ypos4))
                            dix15.append(dst4)
                            dst5 = math.sqrt((x16pos - xpos5) * (x16pos - xpos5) + (y16pos - ypos5) * (y16pos - ypos5))
                            dix15.append(dst5)
                            dst6 = math.sqrt((x16pos - xpos6) * (x16pos - xpos6) + (y16pos - ypos6) * (y16pos - ypos6))
                            dix15.append(dst6)
                            dst7 = math.sqrt((x16pos - xpos7) * (x16pos - xpos7) + (y16pos - ypos7) * (y16pos - ypos7))
                            dix15.append(dst7)
                            dst8 = math.sqrt((x16pos - xpos8) * (x16pos - xpos8) + (y16pos - ypos8) * (y16pos - ypos8))
                            dix15.append(dst8)
                            dst9 = math.sqrt((x16pos - xpos9) * (x16pos - xpos9) + (y16pos - ypos9) * (y16pos - ypos9))
                            dix15.append(dst9)
                            dst10 = math.sqrt((x16pos - xpos10) * (x16pos - xpos10) + (y16pos - ypos10) * (y16pos - ypos10))
                            dix15.append(dst10)
                            dst11 = math.sqrt((x16pos - xpos11) * (x16pos - xpos11) + (y16pos - ypos11) * (y16pos - ypos11))
                            dix15.append(dst11)
                            dst12 = math.sqrt((x16pos - xpos12) * (x16pos - xpos12) + (y16pos - ypos12) * (y16pos - ypos12))
                            dix15.append(dst12)
                            dst13 = math.sqrt((x16pos - xpos13) * (x16pos - xpos13) + (y16pos - ypos13) * (y16pos - ypos13))
                            dix15.append(dst13)
                            dst14 = math.sqrt((x16pos - xpos14) * (x16pos - xpos14) + (y16pos - ypos14) * (y16pos - ypos14))
                            dix15.append(dst14)
                            dst15 = math.sqrt((x16pos - xpos15) * (x16pos - xpos15) + (y16pos - ypos15) * (y16pos - ypos15))
                            dix15.append(dst15)
                            dst16 = math.sqrt((x16pos - xpos16) * (x16pos - xpos16) + (y16pos - ypos16) * (y16pos - ypos16))
                            dix15.append(dst16)
                            dst17 = math.sqrt((x16pos - xpos17) * (x16pos - xpos17) + (y16pos - ypos17) * (y16pos - ypos17))
                            dix15.append(dst17)
                            dst18 = math.sqrt((x16pos - xpos18) * (x16pos - xpos18) + (y16pos - ypos18) * (y16pos - ypos18))
                            dix15.append(dst18)
                            dst19 = math.sqrt((x16pos - xpos19) * (x16pos - xpos19) + (y16pos - ypos19) * (y16pos - ypos19))
                            dix15.append(dst19)
                            dst20 = math.sqrt((x16pos - xpos20) * (x16pos - xpos20) + (y16pos - ypos20) * (y16pos - ypos20))
                            dix15.append(dst20)
                            dst21 = math.sqrt((x16pos - xpos21) * (x16pos - xpos21) + (y16pos - ypos21) * (y16pos - ypos21))
                            dix15.append(dst21)
                            dst22 = math.sqrt((x16pos - xpos22) * (x16pos - xpos22) + (y16pos - ypos22) * (y16pos - ypos22))
                            dix15.append(dst22)
                            dst23 = math.sqrt((x16pos - xpos23) * (x16pos - xpos23) + (y16pos - ypos23) * (y16pos - ypos23))
                            dix15.append(dst23)
                            dst24 = math.sqrt((x16pos - xpos24) * (x16pos - xpos24) + (y16pos - ypos24) * (y16pos - ypos24))
                            dix15.append(dst24)
                            dst25 = math.sqrt((x16pos - xpos25) * (x16pos - xpos25) + (y16pos - ypos25) * (y16pos - ypos25))
                            dix15.append(dst25)
                            for k in range(25):
                                if dix15[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x16pos, y16pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 16:
                            dst1 = math.sqrt((x17pos - xpos1) * (x17pos - xpos1) + (y17pos - ypos1) * (y17pos - ypos1))
                            dix16.append(dst1)
                            dst2 = math.sqrt((x17pos - xpos2) * (x17pos - xpos2) + (y17pos - ypos2) * (y17pos - ypos2))
                            dix16.append(dst2)
                            dst3 = math.sqrt((x17pos - xpos3) * (x17pos - xpos3) + (y17pos - ypos3) * (y17pos - ypos3))
                            dix16.append(dst3)
                            dst4 = math.sqrt((x17pos - xpos4) * (x17pos - xpos4) + (y17pos - ypos4) * (y17pos - ypos4))
                            dix16.append(dst4)
                            dst5 = math.sqrt((x17pos - xpos5) * (x17pos - xpos5) + (y17pos - ypos5) * (y17pos - ypos5))
                            dix16.append(dst5)
                            dst6 = math.sqrt((x17pos - xpos6) * (x17pos - xpos6) + (y17pos - ypos6) * (y17pos - ypos6))
                            dix16.append(dst6)
                            dst7 = math.sqrt((x17pos - xpos7) * (x17pos - xpos7) + (y17pos - ypos7) * (y17pos - ypos7))
                            dix16.append(dst7)
                            dst8 = math.sqrt((x17pos - xpos8) * (x17pos - xpos8) + (y17pos - ypos8) * (y17pos - ypos8))
                            dix16.append(dst8)
                            dst9 = math.sqrt((x17pos - xpos9) * (x17pos - xpos9) + (y17pos - ypos9) * (y17pos - ypos9))
                            dix16.append(dst9)
                            dst10 = math.sqrt((x17pos - xpos10) * (x17pos - xpos10) + (y17pos - ypos10) * (y17pos - ypos10))
                            dix16.append(dst10)
                            dst11 = math.sqrt((x17pos - xpos11) * (x17pos - xpos11) + (y17pos - ypos11) * (y17pos - ypos11))
                            dix16.append(dst11)
                            dst12 = math.sqrt((x17pos - xpos12) * (x17pos - xpos12) + (y17pos - ypos12) * (y17pos - ypos12))
                            dix16.append(dst12)
                            dst13 = math.sqrt((x17pos - xpos13) * (x17pos - xpos13) + (y17pos - ypos13) * (y17pos - ypos13))
                            dix16.append(dst13)
                            dst14 = math.sqrt((x17pos - xpos14) * (x17pos - xpos14) + (y17pos - ypos14) * (y17pos - ypos14))
                            dix16.append(dst14)
                            dst15 = math.sqrt((x17pos - xpos15) * (x17pos - xpos15) + (y17pos - ypos15) * (y17pos - ypos15))
                            dix16.append(dst15)
                            dst16 = math.sqrt((x17pos - xpos16) * (x17pos - xpos16) + (y17pos - ypos16) * (y17pos - ypos16))
                            dix16.append(dst16)
                            dst17 = math.sqrt((x17pos - xpos17) * (x17pos - xpos17) + (y17pos - ypos17) * (y17pos - ypos17))
                            dix16.append(dst17)
                            dst18 = math.sqrt((x17pos - xpos18) * (x17pos - xpos18) + (y17pos - ypos18) * (y17pos - ypos18))
                            dix16.append(dst18)
                            dst19 = math.sqrt((x17pos - xpos19) * (x17pos - xpos19) + (y17pos - ypos19) * (y17pos - ypos19))
                            dix16.append(dst19)
                            dst20 = math.sqrt((x17pos - xpos20) * (x17pos - xpos20) + (y17pos - ypos20) * (y17pos - ypos20))
                            dix16.append(dst20)
                            dst21 = math.sqrt((x17pos - xpos21) * (x17pos - xpos21) + (y17pos - ypos21) * (y17pos - ypos21))
                            dix16.append(dst21)
                            dst22 = math.sqrt((x17pos - xpos22) * (x17pos - xpos22) + (y17pos - ypos22) * (y17pos - ypos22))
                            dix16.append(dst22)
                            dst23 = math.sqrt((x17pos - xpos23) * (x17pos - xpos23) + (y17pos - ypos23) * (y17pos - ypos23))
                            dix16.append(dst23)
                            dst24 = math.sqrt((x17pos - xpos24) * (x17pos - xpos24) + (y17pos - ypos24) * (y17pos - ypos24))
                            dix16.append(dst24)
                            dst25 = math.sqrt((x17pos - xpos25) * (x17pos - xpos25) + (y17pos - ypos25) * (y17pos - ypos25))
                            dix16.append(dst25)
                            for k in range(25):
                                if dix16[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x17pos, y17pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 17:
                            dst1 = math.sqrt((x18pos - xpos1) * (x18pos - xpos1) + (y18pos - ypos1) * (y18pos - ypos1))
                            dix17.append(dst1)
                            dst2 = math.sqrt((x18pos - xpos2) * (x18pos - xpos2) + (y18pos - ypos2) * (y18pos - ypos2))
                            dix17.append(dst2)
                            dst3 = math.sqrt((x18pos - xpos3) * (x18pos - xpos3) + (y18pos - ypos3) * (y18pos - ypos3))
                            dix17.append(dst3)
                            dst4 = math.sqrt((x18pos - xpos4) * (x18pos - xpos4) + (y18pos - ypos4) * (y18pos - ypos4))
                            dix17.append(dst4)
                            dst5 = math.sqrt((x18pos - xpos5) * (x18pos - xpos5) + (y18pos - ypos5) * (y18pos - ypos5))
                            dix17.append(dst5)
                            dst6 = math.sqrt((x18pos - xpos6) * (x18pos - xpos6) + (y18pos - ypos6) * (y18pos - ypos6))
                            dix17.append(dst6)
                            dst7 = math.sqrt((x18pos - xpos7) * (x18pos - xpos7) + (y18pos - ypos7) * (y18pos - ypos7))
                            dix17.append(dst7)
                            dst8 = math.sqrt((x18pos - xpos8) * (x18pos - xpos8) + (y18pos - ypos8) * (y18pos - ypos8))
                            dix17.append(dst8)
                            dst9 = math.sqrt((x18pos - xpos9) * (x18pos - xpos9) + (y18pos - ypos9) * (y18pos - ypos9))
                            dix17.append(dst9)
                            dst10 = math.sqrt((x18pos - xpos10) * (x18pos - xpos10) + (y18pos - ypos10) * (y18pos - ypos10))
                            dix17.append(dst10)
                            dst11 = math.sqrt((x18pos - xpos11) * (x18pos - xpos11) + (y18pos - ypos11) * (y18pos - ypos11))
                            dix17.append(dst11)
                            dst12 = math.sqrt((x18pos - xpos12) * (x18pos - xpos12) + (y18pos - ypos12) * (y18pos - ypos12))
                            dix17.append(dst12)
                            dst13 = math.sqrt((x18pos - xpos13) * (x18pos - xpos13) + (y18pos - ypos13) * (y18pos - ypos13))
                            dix17.append(dst13)
                            dst14 = math.sqrt((x18pos - xpos14) * (x18pos - xpos14) + (y18pos - ypos14) * (y18pos - ypos14))
                            dix17.append(dst14)
                            dst15 = math.sqrt((x18pos - xpos15) * (x18pos - xpos15) + (y18pos - ypos15) * (y18pos - ypos15))
                            dix17.append(dst15)
                            dst16 = math.sqrt((x18pos - xpos16) * (x18pos - xpos16) + (y18pos - ypos16) * (y18pos - ypos16))
                            dix17.append(dst16)
                            dst17 = math.sqrt((x18pos - xpos17) * (x18pos - xpos17) + (y18pos - ypos17) * (y18pos - ypos17))
                            dix17.append(dst17)
                            dst18 = math.sqrt((x18pos - xpos18) * (x18pos - xpos18) + (y18pos - ypos18) * (y18pos - ypos18))
                            dix17.append(dst18)
                            dst19 = math.sqrt((x18pos - xpos19) * (x18pos - xpos19) + (y18pos - ypos19) * (y18pos - ypos19))
                            dix17.append(dst19)
                            dst20 = math.sqrt((x18pos - xpos20) * (x18pos - xpos20) + (y18pos - ypos20) * (y18pos - ypos20))
                            dix17.append(dst20)
                            dst21 = math.sqrt((x18pos - xpos21) * (x18pos - xpos21) + (y18pos - ypos21) * (y18pos - ypos21))
                            dix17.append(dst21)
                            dst22 = math.sqrt((x18pos - xpos22) * (x18pos - xpos22) + (y18pos - ypos22) * (y18pos - ypos22))
                            dix17.append(dst22)
                            dst23 = math.sqrt((x18pos - xpos23) * (x18pos - xpos23) + (y18pos - ypos23) * (y18pos - ypos23))
                            dix17.append(dst23)
                            dst24 = math.sqrt((x18pos - xpos24) * (x18pos - xpos24) + (y18pos - ypos24) * (y18pos - ypos24))
                            dix17.append(dst24)
                            dst25 = math.sqrt((x18pos - xpos25) * (x18pos - xpos25) + (y18pos - ypos25) * (y18pos - ypos25))
                            dix17.append(dst25)
                            for k in range(25):
                                if dix17[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x18pos, y18pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 18:
                            dst1 = math.sqrt((x19pos - xpos1) * (x19pos - xpos1) + (y19pos - ypos1) * (y19pos - ypos1))
                            dix18.append(dst1)
                            dst2 = math.sqrt((x19pos - xpos2) * (x19pos - xpos2) + (y19pos - ypos2) * (y19pos - ypos2))
                            dix18.append(dst2)
                            dst3 = math.sqrt((x19pos - xpos3) * (x19pos - xpos3) + (y19pos - ypos3) * (y19pos - ypos3))
                            dix18.append(dst3)
                            dst4 = math.sqrt((x19pos - xpos4) * (x19pos - xpos4) + (y19pos - ypos4) * (y19pos - ypos4))
                            dix18.append(dst4)
                            dst5 = math.sqrt((x19pos - xpos5) * (x19pos - xpos5) + (y19pos - ypos5) * (y19pos - ypos5))
                            dix18.append(dst5)
                            dst6 = math.sqrt((x19pos - xpos6) * (x19pos - xpos6) + (y19pos - ypos6) * (y19pos - ypos6))
                            dix18.append(dst6)
                            dst7 = math.sqrt((x19pos - xpos7) * (x19pos - xpos7) + (y19pos - ypos7) * (y19pos - ypos7))
                            dix18.append(dst7)
                            dst8 = math.sqrt((x19pos - xpos8) * (x19pos - xpos8) + (y19pos - ypos8) * (y19pos - ypos8))
                            dix18.append(dst8)
                            dst9 = math.sqrt((x19pos - xpos9) * (x19pos - xpos9) + (y19pos - ypos9) * (y19pos - ypos9))
                            dix18.append(dst9)
                            dst10 = math.sqrt((x19pos - xpos10) * (x19pos - xpos10) + (y19pos - ypos10) * (y19pos - ypos10))
                            dix18.append(dst10)
                            dst11 = math.sqrt((x19pos - xpos11) * (x19pos - xpos11) + (y19pos - ypos11) * (y19pos - ypos11))
                            dix18.append(dst11)
                            dst12 = math.sqrt((x19pos - xpos12) * (x19pos - xpos12) + (y19pos - ypos12) * (y19pos - ypos12))
                            dix18.append(dst12)
                            dst13 = math.sqrt((x19pos - xpos13) * (x19pos - xpos13) + (y19pos - ypos13) * (y19pos - ypos13))
                            dix18.append(dst13)
                            dst14 = math.sqrt((x19pos - xpos14) * (x19pos - xpos14) + (y19pos - ypos14) * (y19pos - ypos14))
                            dix18.append(dst14)
                            dst15 = math.sqrt((x19pos - xpos15) * (x19pos - xpos15) + (y19pos - ypos15) * (y19pos - ypos15))
                            dix18.append(dst15)
                            dst16 = math.sqrt((x19pos - xpos16) * (x19pos - xpos16) + (y19pos - ypos16) * (y19pos - ypos16))
                            dix18.append(dst16)
                            dst17 = math.sqrt((x19pos - xpos17) * (x19pos - xpos17) + (y19pos - ypos17) * (y19pos - ypos17))
                            dix18.append(dst17)
                            dst18 = math.sqrt((x19pos - xpos18) * (x19pos - xpos18) + (y19pos - ypos18) * (y19pos - ypos18))
                            dix18.append(dst18)
                            dst19 = math.sqrt((x19pos - xpos19) * (x19pos - xpos19) + (y19pos - ypos19) * (y19pos - ypos19))
                            dix18.append(dst19)
                            dst20 = math.sqrt((x19pos - xpos20) * (x19pos - xpos20) + (y19pos - ypos20) * (y19pos - ypos20))
                            dix18.append(dst20)
                            dst21 = math.sqrt((x19pos - xpos21) * (x19pos - xpos21) + (y19pos - ypos21) * (y19pos - ypos21))
                            dix18.append(dst21)
                            dst22 = math.sqrt((x19pos - xpos22) * (x19pos - xpos22) + (y19pos - ypos22) * (y19pos - ypos22))
                            dix18.append(dst22)
                            dst23 = math.sqrt((x19pos - xpos23) * (x19pos - xpos23) + (y19pos - ypos23) * (y19pos - ypos23))
                            dix18.append(dst23)
                            dst24 = math.sqrt((x19pos - xpos24) * (x19pos - xpos24) + (y19pos - ypos24) * (y19pos - ypos24))
                            dix18.append(dst24)
                            dst25 = math.sqrt((x19pos - xpos25) * (x19pos - xpos25) + (y19pos - ypos25) * (y19pos - ypos25))
                            dix18.append(dst25)
                            for k in range(25):
                                if dix18[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x19pos, y19pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 19:
                            dst1 = math.sqrt((x20pos - xpos1) * (x20pos - xpos1) + (y20pos - ypos1) * (y20pos - ypos1))
                            dix19.append(dst1)
                            dst2 = math.sqrt((x20pos - xpos2) * (x20pos - xpos2) + (y20pos - ypos2) * (y20pos - ypos2))
                            dix19.append(dst2)
                            dst3 = math.sqrt((x20pos - xpos3) * (x20pos - xpos3) + (y20pos - ypos3) * (y20pos - ypos3))
                            dix19.append(dst3)
                            dst4 = math.sqrt((x20pos - xpos4) * (x20pos - xpos4) + (y20pos - ypos4) * (y20pos - ypos4))
                            dix19.append(dst4)
                            dst5 = math.sqrt((x20pos - xpos5) * (x20pos - xpos5) + (y20pos - ypos5) * (y20pos - ypos5))
                            dix19.append(dst5)
                            dst6 = math.sqrt((x20pos - xpos6) * (x20pos - xpos6) + (y20pos - ypos6) * (y20pos - ypos6))
                            dix19.append(dst6)
                            dst7 = math.sqrt((x20pos - xpos7) * (x20pos - xpos7) + (y20pos - ypos7) * (y20pos - ypos7))
                            dix19.append(dst7)
                            dst8 = math.sqrt((x20pos - xpos8) * (x20pos - xpos8) + (y20pos - ypos8) * (y20pos - ypos8))
                            dix19.append(dst8)
                            dst9 = math.sqrt((x20pos - xpos9) * (x20pos - xpos9) + (y20pos - ypos9) * (y20pos - ypos9))
                            dix19.append(dst9)
                            dst10 = math.sqrt((x20pos - xpos10) * (x20pos - xpos10) + (y20pos - ypos10) * (y20pos - ypos10))
                            dix19.append(dst10)
                            dst11 = math.sqrt((x20pos - xpos11) * (x20pos - xpos11) + (y20pos - ypos11) * (y20pos - ypos11))
                            dix19.append(dst11)
                            dst12 = math.sqrt((x20pos - xpos12) * (x20pos - xpos12) + (y20pos - ypos12) * (y20pos - ypos12))
                            dix19.append(dst12)
                            dst13 = math.sqrt((x20pos - xpos13) * (x20pos - xpos13) + (y20pos - ypos13) * (y20pos - ypos13))
                            dix19.append(dst13)
                            dst14 = math.sqrt((x20pos - xpos14) * (x20pos - xpos14) + (y20pos - ypos14) * (y20pos - ypos14))
                            dix19.append(dst14)
                            dst15 = math.sqrt((x20pos - xpos15) * (x20pos - xpos15) + (y20pos - ypos15) * (y20pos - ypos15))
                            dix19.append(dst15)
                            dst16 = math.sqrt((x20pos - xpos16) * (x20pos - xpos16) + (y20pos - ypos16) * (y20pos - ypos16))
                            dix19.append(dst16)
                            dst17 = math.sqrt((x20pos - xpos17) * (x20pos - xpos17) + (y20pos - ypos17) * (y20pos - ypos17))
                            dix19.append(dst17)
                            dst18 = math.sqrt((x20pos - xpos18) * (x20pos - xpos18) + (y20pos - ypos18) * (y20pos - ypos18))
                            dix19.append(dst18)
                            dst19 = math.sqrt((x20pos - xpos19) * (x20pos - xpos19) + (y20pos - ypos19) * (y20pos - ypos19))
                            dix19.append(dst19)
                            dst20 = math.sqrt((x20pos - xpos20) * (x20pos - xpos20) + (y20pos - ypos20) * (y20pos - ypos20))
                            dix19.append(dst20)
                            dst21 = math.sqrt((x20pos - xpos21) * (x20pos - xpos21) + (y20pos - ypos21) * (y20pos - ypos21))
                            dix19.append(dst21)
                            dst22 = math.sqrt((x20pos - xpos22) * (x20pos - xpos22) + (y20pos - ypos22) * (y20pos - ypos22))
                            dix19.append(dst22)
                            dst23 = math.sqrt((x20pos - xpos23) * (x20pos - xpos23) + (y20pos - ypos23) * (y20pos - ypos23))
                            dix19.append(dst23)
                            dst24 = math.sqrt((x20pos - xpos24) * (x20pos - xpos24) + (y20pos - ypos24) * (y20pos - ypos24))
                            dix19.append(dst24)
                            dst25 = math.sqrt((x20pos - xpos25) * (x20pos - xpos25) + (y20pos - ypos25) * (y20pos - ypos25))
                            dix19.append(dst25)
                            for k in range(25):
                                if dix19[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x20pos, y20pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 20:
                            dst1 = math.sqrt((x21pos - xpos1) * (x21pos - xpos1) + (y21pos - ypos1) * (y21pos - ypos1))
                            dix20.append(dst1)
                            dst2 = math.sqrt((x21pos - xpos2) * (x21pos - xpos2) + (y21pos - ypos2) * (y21pos - ypos2))
                            dix20.append(dst2)
                            dst3 = math.sqrt((x21pos - xpos3) * (x21pos - xpos3) + (y21pos - ypos3) * (y21pos - ypos3))
                            dix20.append(dst3)
                            dst4 = math.sqrt((x21pos - xpos4) * (x21pos - xpos4) + (y21pos - ypos4) * (y21pos - ypos4))
                            dix20.append(dst4)
                            dst5 = math.sqrt((x21pos - xpos5) * (x21pos - xpos5) + (y21pos - ypos5) * (y21pos - ypos5))
                            dix20.append(dst5)
                            dst6 = math.sqrt((x21pos - xpos6) * (x21pos - xpos6) + (y21pos - ypos6) * (y21pos - ypos6))
                            dix20.append(dst6)
                            dst7 = math.sqrt((x21pos - xpos7) * (x21pos - xpos7) + (y21pos - ypos7) * (y21pos - ypos7))
                            dix20.append(dst7)
                            dst8 = math.sqrt((x21pos - xpos8) * (x21pos - xpos8) + (y21pos - ypos8) * (y21pos - ypos8))
                            dix20.append(dst8)
                            dst9 = math.sqrt((x21pos - xpos9) * (x21pos - xpos9) + (y21pos - ypos9) * (y21pos - ypos9))
                            dix20.append(dst9)
                            dst10 = math.sqrt((x21pos - xpos10) * (x21pos - xpos10) + (y21pos - ypos10) * (y21pos - ypos10))
                            dix20.append(dst10)
                            dst11 = math.sqrt((x21pos - xpos11) * (x21pos - xpos11) + (y21pos - ypos11) * (y21pos - ypos11))
                            dix20.append(dst11)
                            dst12 = math.sqrt((x21pos - xpos12) * (x21pos - xpos12) + (y21pos - ypos12) * (y21pos - ypos12))
                            dix20.append(dst12)
                            dst13 = math.sqrt((x21pos - xpos13) * (x21pos - xpos13) + (y21pos - ypos13) * (y21pos - ypos13))
                            dix20.append(dst13)
                            dst14 = math.sqrt((x21pos - xpos14) * (x21pos - xpos14) + (y21pos - ypos14) * (y21pos - ypos14))
                            dix20.append(dst14)
                            dst15 = math.sqrt((x21pos - xpos15) * (x21pos - xpos15) + (y21pos - ypos15) * (y21pos - ypos15))
                            dix20.append(dst15)
                            dst16 = math.sqrt((x21pos - xpos16) * (x21pos - xpos16) + (y21pos - ypos16) * (y21pos - ypos16))
                            dix20.append(dst16)
                            dst17 = math.sqrt((x21pos - xpos17) * (x21pos - xpos17) + (y21pos - ypos17) * (y21pos - ypos17))
                            dix20.append(dst17)
                            dst18 = math.sqrt((x21pos - xpos18) * (x21pos - xpos18) + (y21pos - ypos18) * (y21pos - ypos18))
                            dix20.append(dst18)
                            dst19 = math.sqrt((x21pos - xpos19) * (x21pos - xpos19) + (y21pos - ypos19) * (y21pos - ypos19))
                            dix20.append(dst19)
                            dst20 = math.sqrt((x21pos - xpos20) * (x21pos - xpos20) + (y21pos - ypos20) * (y21pos - ypos20))
                            dix20.append(dst20)
                            dst21 = math.sqrt((x21pos - xpos21) * (x21pos - xpos21) + (y21pos - ypos21) * (y21pos - ypos21))
                            dix20.append(dst21)
                            dst22 = math.sqrt((x21pos - xpos22) * (x21pos - xpos22) + (y21pos - ypos22) * (y21pos - ypos22))
                            dix20.append(dst22)
                            dst23 = math.sqrt((x21pos - xpos23) * (x21pos - xpos23) + (y21pos - ypos23) * (y21pos - ypos23))
                            dix20.append(dst23)
                            dst24 = math.sqrt((x21pos - xpos24) * (x21pos - xpos24) + (y21pos - ypos24) * (y21pos - ypos24))
                            dix20.append(dst24)
                            dst25 = math.sqrt((x21pos - xpos25) * (x21pos - xpos25) + (y21pos - ypos25) * (y21pos - ypos25))
                            dix20.append(dst25)
                            for k in range(25):
                                if dix20[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x21pos, y21pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 21:
                            dst1 = math.sqrt((x22pos - xpos1) * (x22pos - xpos1) + (y22pos - ypos1) * (y22pos - ypos1))
                            dix21.append(dst1)
                            dst2 = math.sqrt((x22pos - xpos2) * (x22pos - xpos2) + (y22pos - ypos2) * (y22pos - ypos2))
                            dix21.append(dst2)
                            dst3 = math.sqrt((x22pos - xpos3) * (x22pos - xpos3) + (y22pos - ypos3) * (y22pos - ypos3))
                            dix21.append(dst3)
                            dst4 = math.sqrt((x22pos - xpos4) * (x22pos - xpos4) + (y22pos - ypos4) * (y22pos - ypos4))
                            dix21.append(dst4)
                            dst5 = math.sqrt((x22pos - xpos5) * (x22pos - xpos5) + (y22pos - ypos5) * (y22pos - ypos5))
                            dix21.append(dst5)
                            dst6 = math.sqrt((x22pos - xpos6) * (x22pos - xpos6) + (y22pos - ypos6) * (y22pos - ypos6))
                            dix21.append(dst6)
                            dst7 = math.sqrt((x22pos - xpos7) * (x22pos - xpos7) + (y22pos - ypos7) * (y22pos - ypos7))
                            dix21.append(dst7)
                            dst8 = math.sqrt((x22pos - xpos8) * (x22pos - xpos8) + (y22pos - ypos8) * (y22pos - ypos8))
                            dix21.append(dst8)
                            dst9 = math.sqrt((x22pos - xpos9) * (x22pos - xpos9) + (y22pos - ypos9) * (y22pos - ypos9))
                            dix21.append(dst9)
                            dst10 = math.sqrt((x22pos - xpos10) * (x22pos - xpos10) + (y22pos - ypos10) * (y22pos - ypos10))
                            dix21.append(dst10)
                            dst11 = math.sqrt((x22pos - xpos11) * (x22pos - xpos11) + (y22pos - ypos11) * (y22pos - ypos11))
                            dix21.append(dst11)
                            dst12 = math.sqrt((x22pos - xpos12) * (x22pos - xpos12) + (y22pos - ypos12) * (y22pos - ypos12))
                            dix21.append(dst12)
                            dst13 = math.sqrt((x22pos - xpos13) * (x22pos - xpos13) + (y22pos - ypos13) * (y22pos - ypos13))
                            dix21.append(dst13)
                            dst14 = math.sqrt((x22pos - xpos14) * (x22pos - xpos14) + (y22pos - ypos14) * (y22pos - ypos14))
                            dix21.append(dst14)
                            dst15 = math.sqrt((x22pos - xpos15) * (x22pos - xpos15) + (y22pos - ypos15) * (y22pos - ypos15))
                            dix21.append(dst15)
                            dst16 = math.sqrt((x22pos - xpos16) * (x22pos - xpos16) + (y22pos - ypos16) * (y22pos - ypos16))
                            dix21.append(dst16)
                            dst17 = math.sqrt((x22pos - xpos17) * (x22pos - xpos17) + (y22pos - ypos17) * (y22pos - ypos17))
                            dix21.append(dst17)
                            dst18 = math.sqrt((x22pos - xpos18) * (x22pos - xpos18) + (y22pos - ypos18) * (y22pos - ypos18))
                            dix21.append(dst18)
                            dst19 = math.sqrt((x22pos - xpos19) * (x22pos - xpos19) + (y22pos - ypos19) * (y22pos - ypos19))
                            dix21.append(dst19)
                            dst20 = math.sqrt((x22pos - xpos20) * (x22pos - xpos20) + (y22pos - ypos20) * (y22pos - ypos20))
                            dix21.append(dst20)
                            dst21 = math.sqrt((x22pos - xpos21) * (x22pos - xpos21) + (y22pos - ypos21) * (y22pos - ypos21))
                            dix21.append(dst21)
                            dst22 = math.sqrt((x22pos - xpos22) * (x22pos - xpos22) + (y22pos - ypos22) * (y22pos - ypos22))
                            dix21.append(dst22)
                            dst23 = math.sqrt((x22pos - xpos23) * (x22pos - xpos23) + (y22pos - ypos23) * (y22pos - ypos23))
                            dix21.append(dst23)
                            dst24 = math.sqrt((x22pos - xpos24) * (x22pos - xpos24) + (y22pos - ypos24) * (y22pos - ypos24))
                            dix21.append(dst24)
                            dst25 = math.sqrt((x22pos - xpos25) * (x22pos - xpos25) + (y22pos - ypos25) * (y22pos - ypos25))
                            dix21.append(dst25)
                            for k in range(25):
                                if dix21[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x22pos, y22pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 22:
                            dst1 = math.sqrt((x23pos - xpos1) * (x23pos - xpos1) + (y23pos - ypos1) * (y23pos - ypos1))
                            dix22.append(dst1)
                            dst2 = math.sqrt((x23pos - xpos2) * (x23pos - xpos2) + (y23pos - ypos2) * (y23pos - ypos2))
                            dix22.append(dst2)
                            dst3 = math.sqrt((x23pos - xpos3) * (x23pos - xpos3) + (y23pos - ypos3) * (y23pos - ypos3))
                            dix22.append(dst3)
                            dst4 = math.sqrt((x23pos - xpos4) * (x23pos - xpos4) + (y23pos - ypos4) * (y23pos - ypos4))
                            dix22.append(dst4)
                            dst5 = math.sqrt((x23pos - xpos5) * (x23pos - xpos5) + (y23pos - ypos5) * (y23pos - ypos5))
                            dix22.append(dst5)
                            dst6 = math.sqrt((x23pos - xpos6) * (x23pos - xpos6) + (y23pos - ypos6) * (y23pos - ypos6))
                            dix22.append(dst6)
                            dst7 = math.sqrt((x23pos - xpos7) * (x23pos - xpos7) + (y23pos - ypos7) * (y23pos - ypos7))
                            dix22.append(dst7)
                            dst8 = math.sqrt((x23pos - xpos8) * (x23pos - xpos8) + (y23pos - ypos8) * (y23pos - ypos8))
                            dix22.append(dst8)
                            dst9 = math.sqrt((x23pos - xpos9) * (x23pos - xpos9) + (y23pos - ypos9) * (y23pos - ypos9))
                            dix22.append(dst9)
                            dst10 = math.sqrt((x23pos - xpos10) * (x23pos - xpos10) + (y23pos - ypos10) * (y23pos - ypos10))
                            dix22.append(dst10)
                            dst11 = math.sqrt((x23pos - xpos11) * (x23pos - xpos11) + (y23pos - ypos11) * (y23pos - ypos11))
                            dix22.append(dst11)
                            dst12 = math.sqrt((x23pos - xpos12) * (x23pos - xpos12) + (y23pos - ypos12) * (y23pos - ypos12))
                            dix22.append(dst12)
                            dst13 = math.sqrt((x23pos - xpos13) * (x23pos - xpos13) + (y23pos - ypos13) * (y23pos - ypos13))
                            dix22.append(dst13)
                            dst14 = math.sqrt((x23pos - xpos14) * (x23pos - xpos14) + (y23pos - ypos14) * (y23pos - ypos14))
                            dix22.append(dst14)
                            dst15 = math.sqrt((x23pos - xpos15) * (x23pos - xpos15) + (y23pos - ypos15) * (y23pos - ypos15))
                            dix22.append(dst15)
                            dst16 = math.sqrt((x23pos - xpos16) * (x23pos - xpos16) + (y23pos - ypos16) * (y23pos - ypos16))
                            dix22.append(dst16)
                            dst17 = math.sqrt((x23pos - xpos17) * (x23pos - xpos17) + (y23pos - ypos17) * (y23pos - ypos17))
                            dix22.append(dst17)
                            dst18 = math.sqrt((x23pos - xpos18) * (x23pos - xpos18) + (y23pos - ypos18) * (y23pos - ypos18))
                            dix22.append(dst18)
                            dst19 = math.sqrt((x23pos - xpos19) * (x23pos - xpos19) + (y23pos - ypos19) * (y23pos - ypos19))
                            dix22.append(dst19)
                            dst20 = math.sqrt((x23pos - xpos20) * (x23pos - xpos20) + (y23pos - ypos20) * (y23pos - ypos20))
                            dix22.append(dst20)
                            dst21 = math.sqrt((x23pos - xpos21) * (x23pos - xpos21) + (y23pos - ypos21) * (y23pos - ypos21))
                            dix22.append(dst21)
                            dst22 = math.sqrt((x23pos - xpos22) * (x23pos - xpos22) + (y23pos - ypos22) * (y23pos - ypos22))
                            dix22.append(dst22)
                            dst23 = math.sqrt((x23pos - xpos23) * (x23pos - xpos23) + (y23pos - ypos23) * (y23pos - ypos23))
                            dix22.append(dst23)
                            dst24 = math.sqrt((x23pos - xpos24) * (x23pos - xpos24) + (y23pos - ypos24) * (y23pos - ypos24))
                            dix22.append(dst24)
                            dst25 = math.sqrt((x23pos - xpos25) * (x23pos - xpos25) + (y23pos - ypos25) * (y23pos - ypos25))
                            dix22.append(dst25)
                            for k in range(25):
                                if dix22[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x23pos, y23pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 23:
                            dst1 = math.sqrt((x24pos - xpos1) * (x24pos - xpos1) + (y24pos - ypos1) * (y24pos - ypos1))
                            dix23.append(dst1)
                            dst2 = math.sqrt((x24pos - xpos2) * (x24pos - xpos2) + (y24pos - ypos2) * (y24pos - ypos2))
                            dix23.append(dst2)
                            dst3 = math.sqrt((x24pos - xpos3) * (x24pos - xpos3) + (y24pos - ypos3) * (y24pos - ypos3))
                            dix23.append(dst3)
                            dst4 = math.sqrt((x24pos - xpos4) * (x24pos - xpos4) + (y24pos - ypos4) * (y24pos - ypos4))
                            dix23.append(dst4)
                            dst5 = math.sqrt((x24pos - xpos5) * (x24pos - xpos5) + (y24pos - ypos5) * (y24pos - ypos5))
                            dix23.append(dst5)
                            dst6 = math.sqrt((x24pos - xpos6) * (x24pos - xpos6) + (y24pos - ypos6) * (y24pos - ypos6))
                            dix23.append(dst6)
                            dst7 = math.sqrt((x24pos - xpos7) * (x24pos - xpos7) + (y24pos - ypos7) * (y24pos - ypos7))
                            dix23.append(dst7)
                            dst8 = math.sqrt((x24pos - xpos8) * (x24pos - xpos8) + (y24pos - ypos8) * (y24pos - ypos8))
                            dix23.append(dst8)
                            dst9 = math.sqrt((x24pos - xpos9) * (x24pos - xpos9) + (y24pos - ypos9) * (y24pos - ypos9))
                            dix23.append(dst9)
                            dst10 = math.sqrt((x24pos - xpos10) * (x24pos - xpos10) + (y24pos - ypos10) * (y24pos - ypos10))
                            dix23.append(dst10)
                            dst11 = math.sqrt((x24pos - xpos11) * (x24pos - xpos11) + (y24pos - ypos11) * (y24pos - ypos11))
                            dix23.append(dst11)
                            dst12 = math.sqrt((x24pos - xpos12) * (x24pos - xpos12) + (y24pos - ypos12) * (y24pos - ypos12))
                            dix23.append(dst12)
                            dst13 = math.sqrt((x24pos - xpos13) * (x24pos - xpos13) + (y24pos - ypos13) * (y24pos - ypos13))
                            dix23.append(dst13)
                            dst14 = math.sqrt((x24pos - xpos14) * (x24pos - xpos14) + (y24pos - ypos14) * (y24pos - ypos14))
                            dix23.append(dst14)
                            dst15 = math.sqrt((x24pos - xpos15) * (x24pos - xpos15) + (y24pos - ypos15) * (y24pos - ypos15))
                            dix23.append(dst15)
                            dst16 = math.sqrt((x24pos - xpos16) * (x24pos - xpos16) + (y24pos - ypos16) * (y24pos - ypos16))
                            dix23.append(dst16)
                            dst17 = math.sqrt((x24pos - xpos17) * (x24pos - xpos17) + (y24pos - ypos17) * (y24pos - ypos17))
                            dix23.append(dst17)
                            dst18 = math.sqrt((x24pos - xpos18) * (x24pos - xpos18) + (y24pos - ypos18) * (y24pos - ypos18))
                            dix23.append(dst18)
                            dst19 = math.sqrt((x24pos - xpos19) * (x24pos - xpos19) + (y24pos - ypos19) * (y24pos - ypos19))
                            dix23.append(dst19)
                            dst20 = math.sqrt((x24pos - xpos20) * (x24pos - xpos20) + (y24pos - ypos20) * (y24pos - ypos20))
                            dix23.append(dst20)
                            dst21 = math.sqrt((x24pos - xpos21) * (x24pos - xpos21) + (y24pos - ypos21) * (y24pos - ypos21))
                            dix23.append(dst21)
                            dst22 = math.sqrt((x24pos - xpos22) * (x24pos - xpos22) + (y24pos - ypos22) * (y24pos - ypos22))
                            dix23.append(dst22)
                            dst23 = math.sqrt((x24pos - xpos23) * (x24pos - xpos23) + (y24pos - ypos23) * (y24pos - ypos23))
                            dix23.append(dst23)
                            dst24 = math.sqrt((x24pos - xpos24) * (x24pos - xpos24) + (y24pos - ypos24) * (y24pos - ypos24))
                            dix23.append(dst24)
                            dst25 = math.sqrt((x24pos - xpos25) * (x24pos - xpos25) + (y24pos - ypos25) * (y24pos - ypos25))
                            dix23.append(dst25)
                            for k in range(25):
                                if dix23[k] < 50:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x24pos, y24pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0

                if ptr == 1:
                    break

            ptr = 0
            del dist[:]
            del dixt[:]
            del dix0[:]
            del dix1[:]
            del dix2[:]
            del dix3[:]
            del dix4[:]
            del dix5[:]
            del dix6[:]
            del dix7[:]
            del dix8[:]
            del dix9[:]
            del dix10[:]
            del dix11[:]
            del dix12[:]
            del dix13[:]
            del dix14[:]
            del dix15[:]
            del dix16[:]
            del dix17[:]
            del dix18[:]
            del dix19[:]
            del dix20[:]
            del dix21[:]
            del dix22[:]
            del dix23[:]

            '''
            dis1 = math.sqrt((xpos - xpos1)*(xpos - xpos1) + (ypos - ypos1)*(ypos - ypos1))
            dis2 = math.sqrt((xpos - xpos2)*(xpos - xpos2) + (ypos - ypos2)*(ypos - ypos2))
            dis3 = math.sqrt((xpos - xpos3)*(xpos - xpos3) + (ypos - ypos3)*(ypos - ypos3))
            dis4 = math.sqrt((xpos - xpos4)*(xpos - xpos4) + (ypos - ypos4)*(ypos - ypos4))
            dis5 = math.sqrt((xpos - xpos5)*(xpos - xpos5) + (ypos - ypos5)*(ypos - ypos5))
            dis6 = math.sqrt((xpos - xpos6)*(xpos - xpos6) + (ypos - ypos6)*(ypos - ypos6))
            dis7 = math.sqrt((xpos - xpos7)*(xpos - xpos7) + (ypos - ypos7)*(ypos - ypos7))
            dis8 = math.sqrt((xpos - xpos8)*(xpos - xpos8) + (ypos - ypos8)*(ypos - ypos8))
            dis9 = math.sqrt((xpos - xpos9)*(xpos - xpos9) + (ypos - ypos9)*(ypos - ypos9))
            dis10 = math.sqrt((xpos - xpos10)*(xpos - xpos10) + (ypos - ypos10)*(ypos - ypos10))
            '''





        if self.pos[0] > 1200 and self.pos[0] < 25 and self.pos[1] > 625 and self.pos[1] < 25:
            self.alive = False

        if self.life != -1 and self.curframe > self.life:
            self.alive = False
        else:
            if self.life == -1 and self.curframe >= len(
                    self.parent.particlecache):  # If the particle has infinite life and has passed the last cached frame
                self.colour = (self.parent.particlecache[len(self.parent.particlecache) - 1]['colour_r'],
                               self.parent.particlecache[len(self.parent.particlecache) - 1]['colour_g'],
                               self.parent.particlecache[len(self.parent.particlecache) - 1]['colour_b'])
                self.radius = self.parent.particlecache[len(self.parent.particlecache) - 1]['radius']
                self.length = self.parent.particlecache[len(self.parent.particlecache) - 1]['length']
            else:  # Otherwise, get the values for the current frame
                self.colour = (self.parent.particlecache[self.curframe]['colour_r'],
                               self.parent.particlecache[self.curframe]['colour_g'],
                               self.parent.particlecache[self.curframe]['colour_b'])
                self.radius = self.parent.particlecache[self.curframe]['radius']
                self.length = self.parent.particlecache[self.curframe]['length']

            self.curframe = self.curframe + 1

    def Draw(self, display):
        offset = self.parent.parenteffect.pos

        if (self.pos[0] > 10000) or (self.pos[1] > 10000) or (self.pos[0] < -10000) or (self.pos[1] < -10000):
            return

        if self.drawtype == DRAWTYPE_POINT:  # Point
            pygame.draw.circle(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])), 0)

        elif self.drawtype == DRAWTYPE_CIRCLE:  # Circle
            pygame.draw.circle(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])),
                               int(self.radius))

        elif self.drawtype == DRAWTYPE_LINE:
            if self.length == 0.0:
                pygame.draw.circle(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])),
                                   0)

            else:
                # Vector = (velocity / mag(velocity)) * length (a line of magnitude 'length' in
                # direction of velocity); this is calculated as velocity / (mag(velocity) / length)
                # so that parts consistent for both components in the final calculation are only calculated once
                velocitymagoverlength = math.sqrt(self.velocity[0] ** 2 + self.velocity[1] ** 2) / self.length

                if velocitymagoverlength > 0.0:  # Avoid division-by-zero errors by handling lines with zero velocity separately
                    linevec = [(self.velocity[0] / velocitymagoverlength), (self.velocity[1] / velocitymagoverlength)]
                else:
                    linevec = [self.length, 0.0]  # Draw a line pointing to the right

                endpoint = [offset[0] + int(self.pos[0] + linevec[0]), offset[1] + int(self.pos[1] + linevec[1])]
                pygame.draw.aaline(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])),
                                   endpoint)

        elif self.drawtype == DRAWTYPE_SCALELINE:  # Scaling line (scales with velocity)
            endpoint = [offset[0] + int(self.pos[0] + self.velocity[0]),
                        offset[1] + int(self.pos[1] + self.velocity[1])]
            pygame.draw.aaline(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])),
                               endpoint)

        elif self.drawtype == DRAWTYPE_BUBBLE:  # Bubble
            if self.radius >= 1.0:
                pygame.draw.circle(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])),
                                   int(self.radius), 0)
            else:  # Pygame won't draw circles with thickness < radius, so if radius is smaller than one don't bother trying to set thickness
                pygame.draw.circle(display, self.colour, (offset[0] + int(self.pos[0]), offset[1] + int(self.pos[1])),
                                   int(self.radius))

        elif self.drawtype == DRAWTYPE_IMAGE:  # Image
            size = self.image.get_size()
            display.blit(self.image, (offset[0] + int(self.pos[0] - size[1]), offset[1] + int(self.pos[1] - size[1])))

    def CreateKeyframe(self, frame, colour=(None, None, None), radius=None, length=None):
        keyframes.CreateKeyframe(self.keyframes, frame,
                                 {'colour_r': colour[0], 'colour_g': colour[1], 'colour_b': colour[2], 'radius': radius,
                                  'length': length})


class ParticleSource:
    def __init__(self, parenteffect, pos, initspeed, initdirection, initspeedrandrange, initdirectionrandrange,
                 particlesperframe, particlelife, genspacing, drawtype=0, colour=(0, 0, 0), radius=0.0, length=0.0,
                 imagepath=None):
        self.parenteffect = parenteffect
        self.pos = pos
        self.initspeed = initspeed
        self.initdirection = initdirection
        self.initspeedrandrange = initspeedrandrange
        self.initdirectionrandrange = initdirectionrandrange
        self.particlesperframe = particlesperframe
        self.particlelife = particlelife
        self.genspacing = genspacing
        self.colour = colour
        self.drawtype = drawtype
        self.radius = radius
        self.length = length
        self.imagepath = imagepath
        if self.imagepath == None:
            self.image = None
        else:
            self.image = pygame.image.load(self.imagepath).convert_alpha()
        self.drawtype = drawtype

        self.keyframes = []
        self.CreateKeyframe(0, self.pos, self.initspeed, self.initdirection, self.initspeedrandrange,
                            self.initdirectionrandrange, self.particlesperframe, self.genspacing)
        self.particlekeyframes = []
        self.particlecache = []
        self.CreateParticleKeyframe(0, colour=self.colour, radius=self.radius, length=self.length)
        self.curframe = 0

    def Update(self):
        newvars = interpolate.InterpolateKeyframes(self.curframe, {'pos_x': self.pos[0], 'pos_y': self.pos[1],
                                                                   'initspeed': self.initspeed,
                                                                   'initdirection': self.initdirection,
                                                                   'initspeedrandrange': self.initspeedrandrange,
                                                                   'initdirectionrandrange': self.initdirectionrandrange,
                                                                   'particlesperframe': self.particlesperframe,
                                                                   'genspacing': self.genspacing}, self.keyframes)
        self.pos = (newvars['pos_x'], newvars['pos_y'])
        self.initspeed = newvars['initspeed']
        self.initdirection = newvars['initdirection']
        self.initspeedrandrange = newvars['initspeedrandrange']
        self.initdirectionrandrange = newvars['initdirectionrandrange']
        self.particlesperframe = newvars['particlesperframe']
        self.genspacing = newvars['genspacing']

        particlesperframe = self.particlesperframe

        if (self.genspacing == 0) or ((self.curframe % self.genspacing) == 0):
            for i in range(0, int(particlesperframe)):
                self.CreateParticle()

        self.curframe = self.curframe + 1

    def CreateParticle(self):
        if self.initspeedrandrange != 0.0:
            speed = self.initspeed + (float(
                random.randrange(int(-self.initspeedrandrange * 100.0), int(self.initspeedrandrange * 100.0))) / 100.0)
        else:
            speed = self.initspeed
        if self.initdirectionrandrange != 0.0:
            direction = self.initdirection + (float(random.randrange(int(-self.initdirectionrandrange * 100.0),
                                                                     int(self.initdirectionrandrange * 100.0))) / 100.0)
        else:
            direction = self.initdirection
        velocity = [speed * math.sin(direction), -speed * math.cos(direction)]
        newparticle = Particle(self, initpos=self.pos, velocity=velocity, angle=0.0, life=self.particlelife,
                               drawtype=self.drawtype, colour=self.colour, radius=self.radius, length=self.length,
                               image=self.image, keyframes=self.particlekeyframes)
        self.parenteffect.AddParticle(newparticle)

    def CreateKeyframe(self, frame, pos=(None, None), initspeed=None, initdirection=None, initspeedrandrange=None,
                       initdirectionrandrange=None, particlesperframe=None, genspacing=None,
                       interpolationtype=INTERPOLATIONTYPE_LINEAR):
        return keyframes.CreateKeyframe(self.keyframes, frame,
                                        {'pos_x': pos[0], 'pos_y': pos[1], 'initspeed': initspeed,
                                         'initdirection': initdirection, 'initspeedrandrange': initspeedrandrange,
                                         'initdirectionrandrange': initdirectionrandrange,
                                         'particlesperframe': particlesperframe, 'genspacing': genspacing,
                                         'interpolationtype': interpolationtype})

    def CreateParticleKeyframe(self, frame, colour=(None, None, None), radius=None, length=None,
                               interpolationtype=INTERPOLATIONTYPE_LINEAR):
        newframe = keyframes.CreateKeyframe(self.particlekeyframes, frame,
                                            {'colour_r': colour[0], 'colour_g': colour[1], 'colour_b': colour[2],
                                             'radius': radius, 'length': length,
                                             'interpolationtype': interpolationtype})
        self.PreCalculateParticles()
        return newframe

    def GetKeyframeValue(self, keyframe):
        return keyframe.frame

    def PreCalculateParticles(self):
        self.particlecache = []  # Clear the cache

        # If the particle has infinite life, interpolate for each frame up until its last keyframe
        if self.particlelife == -1:
            particlelife = max(self.particlekeyframes, key=self.GetKeyframeValue).frame
        else:  # Otherwise, interpolate the particle variables for each frame of its life
            particlelife = self.particlelife

        for i in range(0, particlelife + 1):
            vars = interpolate.InterpolateKeyframes(i, {'colour_r': 0, 'colour_g': 0, 'colour_b': 0, 'radius': 0,
                                                        'length': 0}, self.particlekeyframes)
            self.particlecache.append(vars)

    def ConsolidateKeyframes(self):
        keyframes.ConsolidateKeyframes(self.keyframes, self.curframe,
                                       {'pos_x': self.pos[0], 'pos_y': self.pos[1], 'initspeed': self.initspeed,
                                        'initdirection': self.initdirection,
                                        'initspeedrandrange': self.initspeedrandrange,
                                        'initdirectionrandrange': self.initdirectionrandrange,
                                        'particlesperframe': self.particlesperframe, 'genspacing': self.genspacing})

    def SetPos(self, newpos):
        self.CreateKeyframe(self.curframe, pos=newpos)

    def SetInitSpeed(self, newinitspeed):
        self.CreateKeyframe(self.curframe, initspeed=newinitspeed)

    def SetInitDirection(self, newinitdirection):
        self.CreateKeyframe(self.curframe, initdirection=newinitdirection)

    def SetInitSpeedRandRange(self, newinitspeedrandrange):
        self.CreateKeyframe(self.curframe, initspeedrandrange=newinitspeedrandrange)

    def SetInitDirectionRandRange(self, newinitdirectionrandrange):
        self.CreateKeyframe(self.curframe, initdirectionrandrange=newinitdirectionrandrange)

    def SetParticlesPerFrame(self, newparticlesperframe):
        self.CreateKeyframe(self.curframe, particlesperframe=newparticlesperframe)

    def SetGenSpacing(self, newgenspacing):
        self.CreateKeyframe(self.curframe, genspacing=newgenspacing)
