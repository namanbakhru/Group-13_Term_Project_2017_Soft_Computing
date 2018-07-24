### EXESOFT PYIGNITION ###
# Copyright David Barker 2010
#
# Particle and ParticleSource objects


import keyframes, interpolate, random, math, pygame, constants
from constants import *

kc1 = 0.0
tc1 = 0.0
kc2 = 0.0
tc2 = 0.0
kc3 = 0.0
tc3 = 0.0
kc4 = 0.0
tc4 = 0.0
kc5 = 0.0
tc5 = 0.0
kc6 = 0.0
tc6 = 0.0
kc7 = 0.0
tc7 = 0.0
kc8 = 0.0
tc8 = 0.0
kc9 = 0.0
tc9 = 0.0
kc10 = 0.0
tc10 = 0.0
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
        global xpos, ypos, xpos1, ypos1, xpos2, ypos2, xpos3, ypos3, xpos4, ypos4, xpos5, ypos5, xpos6, ypos6, xpos7, ypos7, xpos8, ypos8, xpos9, ypos9, xpos10, ypos10, xpos11, ypos11
        global dist, dixt, dix0, dix1, dix2, dix3, dix4, dix5, dix6, dix7, dix8, dix9, dix10, dix11, dix12, dix13, dix14, dix15, dix16, dix17, dix18, dix19, dix20, dix21, dix22, dix23

        tt = 10*random.random()

        if constants.ck % 12 == 1:
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
        elif constants.ck % 12 == 2:
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
        elif constants.ck % 12 == 3:
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
        elif constants.ck % 12 == 4:
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
        elif constants.ck % 12 == 5:
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
        elif constants.ck % 12 == 6:
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
        elif constants.ck % 12 == 7:
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
            ypos7 = self.pos[1] - tc7
            self.pos = [xpos7, ypos7]
        elif constants.ck % 12 == 8:
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
            ypos8 = self.pos[1] + tc8
            self.pos = [xpos8, ypos8]
        elif constants.ck % 12 == 9:
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
        elif constants.ck % 12 == 10:
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
        elif constants.ck %12 == 11:
            self.pos = [self.pos[0], self.pos[1]]
            xpos11 = self.pos[0]
            ypos11 = self.pos[1]
        elif constants.ck%12 == 0:
            xpos = self.pos[0]
            ypos = self.pos[1]
            x1pos = xpos + 5
            y1pos = ypos
            x2pos = xpos + 5 * math.cos(math.pi / 4)
            y2pos = ypos + 5 * math.sin(math.pi / 4)
            x3pos = xpos + 5 * math.cos(math.pi / 4)
            y3pos = ypos - 5 * math.sin(math.pi / 4)
            x4pos = xpos
            y4pos = ypos + 5
            x5pos = xpos
            y5pos = ypos - 5
            x6pos = xpos - 5
            y6pos = ypos
            x7pos = xpos - 5 * math.cos(math.pi / 4)
            y7pos = ypos + 5 * math.sin(math.pi / 4)
            x8pos = xpos - 5 * math.cos(math.pi / 4)
            y8pos = ypos - 5 * math.sin(math.pi / 4)
            x9pos = xpos + 5 * math.cos(math.pi / 6)
            y9pos = ypos - 5 * math.sin(math.pi / 6)
            x10pos = xpos + 5 * math.cos(math.pi / 12)
            y10pos = ypos - 5 * math.sin(math.pi / 12)
            x11pos = xpos + 5 * math.cos(math.pi / 12)
            y11pos = ypos + 5 * math.sin(math.pi / 12)
            x12pos = xpos + 5 * math.cos(math.pi / 6)
            y12pos = ypos + 5 * math.sin(math.pi / 6)
            x13pos = xpos + 5 * math.cos(math.pi / 3)
            y13pos = ypos + 5 * math.sin(math.pi / 3)
            x14pos = xpos + 5 * math.cos(5 * math.pi / 12)
            y14pos = ypos + 5 * math.sin(5 * math.pi / 12)
            x15pos = xpos - 5 * math.cos(5 * math.pi / 12)
            y15pos = ypos + 5 * math.sin(5 * math.pi / 12)
            x16pos = xpos - 5 * math.cos(math.pi / 3)
            y16pos = ypos + 5 * math.sin(math.pi / 3)
            x17pos = xpos - 5 * math.cos(math.pi / 6)
            y17pos = ypos + 5 * math.sin(math.pi / 6)
            x18pos = xpos - 5 * math.cos(math.pi / 12)
            y18pos = ypos + 5 * math.sin(math.pi / 12)
            x19pos = xpos - 5 * math.cos(math.pi / 12)
            y19pos = ypos - 5 * math.sin(math.pi / 12)
            x20pos = xpos - 5 * math.cos(math.pi / 6)
            y20pos = ypos - 5 * math.sin(math.pi / 6)
            x21pos = xpos - 5 * math.cos(math.pi / 3)
            y21pos = ypos - 5 * math.sin(math.pi / 3)
            x22pos = xpos - 5 * math.cos(5 * math.pi / 12)
            y22pos = ypos - 5 * math.sin(5 * math.pi / 12)
            x23pos = xpos + 5 * math.cos(5 *math.pi / 12)
            y23pos = ypos - 5 * math.sin(5 *math.pi / 12)
            x24pos = xpos + 5 * math.cos(math.pi / 3)
            y24pos = ypos - 5 * math.sin(math.pi / 3)
            dis = math.sqrt((xpos - xpos11) * (xpos - xpos11) + (ypos - ypos11) * (ypos - ypos11))
            dist0 = math.sqrt((x1pos - xpos11) * (x1pos - xpos11) + (y1pos - ypos11) * (y1pos - ypos11))
            dist.append(dist0)
            dist1 = math.sqrt((x2pos - xpos11) * (x2pos - xpos11) + (y2pos - ypos11) * (y2pos - ypos11))
            dist.append(dist1)
            dist2 = math.sqrt((x3pos - xpos11) * (x3pos - xpos11) + (y3pos - ypos11) * (y3pos - ypos11))
            dist.append(dist2)
            dist3 = math.sqrt((x4pos - xpos11) * (x4pos - xpos11) + (y4pos - ypos11) * (y4pos - ypos11))
            dist.append(dist3)
            dist4 = math.sqrt((x5pos - xpos11) * (x5pos - xpos11) + (y5pos - ypos11) * (y5pos - ypos11))
            dist.append(dist4)
            dist5 = math.sqrt((x6pos - xpos11) * (x6pos - xpos11) + (y6pos - ypos11) * (y6pos - ypos11))
            dist.append(dist5)
            dist6 = math.sqrt((x7pos - xpos11) * (x7pos - xpos11) + (y7pos - ypos11) * (y7pos - ypos11))
            dist.append(dist6)
            dist7 = math.sqrt((x8pos - xpos11) * (x8pos - xpos11) + (y8pos - ypos11) * (y8pos - ypos11))
            dist.append(dist7)
            dist8 = math.sqrt((x9pos - xpos11) * (x9pos - xpos11) + (y9pos - ypos11) * (y9pos - ypos11))
            dist.append(dist8)
            dist9 = math.sqrt((x10pos - xpos11) * (x10pos - xpos11) + (y10pos - ypos11) * (y10pos - ypos11))
            dist.append(dist9)
            dist10 = math.sqrt((x11pos - xpos11) * (x11pos - xpos11) + (y11pos - ypos11) * (y11pos - ypos11))
            dist.append(dist10)
            dist11 = math.sqrt((x12pos - xpos11) * (x12pos - xpos11) + (y12pos - ypos11) * (y12pos - ypos11))
            dist.append(dist11)
            dist12 = math.sqrt((x13pos - xpos11) * (x13pos - xpos11) + (y13pos - ypos11) * (y13pos - ypos11))
            dist.append(dist12)
            dist13 = math.sqrt((x14pos - xpos11) * (x14pos - xpos11) + (y14pos - ypos11) * (y14pos - ypos11))
            dist.append(dist13)
            dist14 = math.sqrt((x15pos - xpos11) * (x15pos - xpos11) + (y15pos - ypos11) * (y15pos - ypos11))
            dist.append(dist14)
            dist15 = math.sqrt((x16pos - xpos11) * (x16pos - xpos11) + (y16pos - ypos11) * (y16pos - ypos11))
            dist.append(dist15)
            dist16 = math.sqrt((x17pos - xpos11) * (x17pos - xpos11) + (y17pos - ypos11) * (y17pos - ypos11))
            dist.append(dist16)
            dist17 = math.sqrt((x18pos - xpos11) * (x18pos - xpos11) + (y18pos - ypos11) * (y18pos - ypos11))
            dist.append(dist17)
            dist18 = math.sqrt((x19pos - xpos11) * (x19pos - xpos11) + (y19pos - ypos11) * (y19pos - ypos11))
            dist.append(dist18)
            dist19 = math.sqrt((x20pos - xpos11) * (x20pos - xpos11) + (y20pos - ypos11) * (y20pos - ypos11))
            dist.append(dist19)
            dist20 = math.sqrt((x21pos - xpos11) * (x21pos - xpos11) + (y21pos - ypos11) * (y21pos - ypos11))
            dist.append(dist20)
            dist21 = math.sqrt((x22pos - xpos11) * (x22pos - xpos11) + (y22pos - ypos11) * (y22pos - ypos11))
            dist.append(dist21)
            dist22 = math.sqrt((x23pos - xpos11) * (x23pos - xpos11) + (y23pos - ypos11) * (y23pos - ypos11))
            dist.append(dist22)
            dist23 = math.sqrt((x24pos - xpos11) * (x24pos - xpos11) + (y24pos - ypos11) * (y24pos - ypos11))
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
                            for k in range(10):
                                if dix0[k] < 70:
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
                            for k in range(10):
                                if dix1[k] < 70:
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
                            for k in range(10):
                                if dix2[k] < 70:
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
                            for k in range(10):
                                if dix3[k] < 70:
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
                            for k in range(10):
                                if dix4[k] < 70:
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
                            for k in range(10):
                                if dix5[k] < 70:
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
                            for k in range(10):
                                if dix6[k] < 70:
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
                            for k in range(10):
                                if dix7[k] < 70:
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
                            for k in range(10):
                                if dix8[k] < 70:
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
                            for k in range(10):
                                if dix9[k] < 70:
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
                            for k in range(10):
                                if dix10[k] < 70:
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
                            for k in range(10):
                                if dix11[k] < 70:
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
                            for k in range(10):
                                if dix12[k] < 70:
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
                            for k in range(10):
                                if dix13[k] < 70:
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
                            for k in range(10):
                                if dix14[k] < 70:
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
                            for k in range(10):
                                if dix15[k] < 70:
                                    pttr = 1
                                    break
                            if pttr == 0:
                                self.pos = [x16pos, y16pos]
                                ptr = 1
                                break
                            else:
                                pttr = 0
                        elif j == 16:
                            dst1 = math.sqrt((x17pos - xpos1) * (x17pos - xpos1) + (y18pos - ypos1) * (y19pos - ypos1))
                            dix16.append(dst1)
                            dst2 = math.sqrt((x17pos - xpos2) * (x17pos - xpos2) + (y18pos - ypos2) * (y19pos - ypos2))
                            dix16.append(dst2)
                            dst3 = math.sqrt((x17pos - xpos3) * (x17pos - xpos3) + (y18pos - ypos3) * (y19pos - ypos3))
                            dix16.append(dst3)
                            dst4 = math.sqrt((x17pos - xpos4) * (x17pos - xpos4) + (y18pos - ypos4) * (y19pos - ypos4))
                            dix16.append(dst4)
                            dst5 = math.sqrt((x17pos - xpos5) * (x17pos - xpos5) + (y18pos - ypos5) * (y19pos - ypos5))
                            dix16.append(dst5)
                            dst6 = math.sqrt((x17pos - xpos6) * (x17pos - xpos6) + (y18pos - ypos6) * (y19pos - ypos6))
                            dix16.append(dst6)
                            dst7 = math.sqrt((x17pos - xpos7) * (x17pos - xpos7) + (y18pos - ypos7) * (y19pos - ypos7))
                            dix16.append(dst7)
                            dst8 = math.sqrt((x17pos - xpos8) * (x17pos - xpos8) + (y18pos - ypos8) * (y19pos - ypos8))
                            dix16.append(dst8)
                            dst9 = math.sqrt((x17pos - xpos9) * (x17pos - xpos9) + (y18pos - ypos9) * (y19pos - ypos9))
                            dix16.append(dst9)
                            dst10 = math.sqrt((x17pos - xpos10) * (x17pos - xpos10) + (y18pos - ypos10) * (y19pos - ypos10))
                            dix16.append(dst10)
                            for k in range(10):
                                if dix16[k] < 70:
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
                            for k in range(10):
                                if dix17[k] < 70:
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
                            for k in range(10):
                                if dix18[k] < 70:
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
                            for k in range(10):
                                if dix19[k] < 70:
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
                            for k in range(10):
                                if dix20[k] < 70:
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
                            for k in range(10):
                                if dix21[k] < 70:
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
                            for k in range(10):
                                if dix22[k] < 70:
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
                            for k in range(10):
                                if dix23[k] < 70:
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
