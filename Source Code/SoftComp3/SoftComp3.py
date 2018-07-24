import PyIgnition, pygame, sys, math, random, constants
from constants import *


screen = pygame.display.set_mode((1250, 675))
pygame.display.set_caption("Simulation!!!")
clock = pygame.time.Clock()

effect1 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect2 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect3 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect4 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect5 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect6 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect7 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect8 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect9 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect10 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect11 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect12 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect13 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect14 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect15 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect16 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect17 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect18 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect19 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect20 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect21 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect22 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect23 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect24 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
effect25 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))

source1 = effect1.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source2 = effect2.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source3 = effect3.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source4 = effect4.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source5 = effect5.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source6 = effect6.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source7 = effect7.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source8 = effect8.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source9 = effect9.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source10 = effect10.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source11 = effect11.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source12 = effect12.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source13 = effect13.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source14 = effect14.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source15 = effect15.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source16 = effect16.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source17 = effect17.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source18 = effect18.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source19 = effect19.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source20 = effect20.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source21 = effect21.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source22 = effect22.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source23 = effect23.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source24 = effect24.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source25 = effect25.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=6.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)


effect26 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
source26 = effect26.CreateSource(initspeed=10.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=20.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(10, 210, 180), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=15.0)

effect27 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
source27 = effect27.CreateSource(initspeed=0.0, initdirection= 0.0, initspeedrandrange=0.0, initdirectionrandrange=0.0,
                             particlelife=1000, colour=(110, 10, 180), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=10.0)

ct = 0
start = 0
gt = 0

pygame.init()
font = pygame.font.SysFont('Arial',80, bold=True)
img1 = font.render('Intelligent', True,
                  pygame.Color(255,165,0),
                  pygame.Color(110,10,100))
img6 = font.render('-', True,
                  pygame.Color(255,165,0),
                  pygame.Color(110,10,100))
img2 = font.render('Path', True,
                  pygame.Color(255,165,0),
                  pygame.Color(110,10,100))
img3 = font.render('Planning', True,
                  pygame.Color(255,165,0),
                  pygame.Color(110,10,100))
img4 = font.render('Start', True,
                  pygame.Color(155,125,50),
                  pygame.Color(0,0,0))
img5 = font.render('Quit', True,
                  pygame.Color(155,125,50),
                  pygame.Color(0,0,0))

while start == 0:
    gt = gt+2
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos=pygame.mouse.get_pos()
            if 236<pos[0]<486 and 451<pos[1]<551:
                start = 1
                break
            elif 761<pos[0]<1011 and 451<pos[1]<551:
                exit()

    screen.fill((10, 0, 50))
    screen.fill((110, 10, 100), rect=(25, 25, 1200, 625))
    screen.fill((0,0,0), rect=(235,450,250,100))
    screen.fill((0,0,0), rect=(760,450,250,100))
    screen.blit(img4, (270,455))
    screen.blit(img5, (795,455))
    screen.blit(img1, (250,120))
    screen.blit(img6, (680, 120))
    screen.blit(img2, (750,120))
    screen.blit(img3, (400,260))
    pygame.display.update()
    clock.tick(60)

while start == 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            ct = ct+1
            if ct < 27:
                if ct%27 == 1:
                    source1.CreateKeyframe(source1.curframe + 1, pos=pygame.mouse.get_pos(), initspeed = 3.0, initdirection = 2*math.pi*random.random(), initspeedrandrange = 8.0, initdirectionrandrange = 2*math.pi, particlesperframe=1)
                    source1.CreateKeyframe(source1.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 2:
                    source2.CreateKeyframe(source2.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source2.CreateKeyframe(source2.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 3:
                    source3.CreateKeyframe(source3.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source3.CreateKeyframe(source3.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 4:
                    source4.CreateKeyframe(source4.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source4.CreateKeyframe(source4.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 5:
                    source5.CreateKeyframe(source5.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source5.CreateKeyframe(source5.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 6:
                    source6.CreateKeyframe(source6.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source6.CreateKeyframe(source6.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 7:
                    source7.CreateKeyframe(source7.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source7.CreateKeyframe(source7.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 8:
                    source8.CreateKeyframe(source8.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source8.CreateKeyframe(source8.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 9:
                    source9.CreateKeyframe(source9.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source9.CreateKeyframe(source9.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 10:
                    source10.CreateKeyframe(source10.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source10.CreateKeyframe(source10.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 11:
                    source11.CreateKeyframe(source11.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source11.CreateKeyframe(source11.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 12:
                    source12.CreateKeyframe(source12.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source12.CreateKeyframe(source12.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 13:
                    source13.CreateKeyframe(source13.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source13.CreateKeyframe(source13.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 14:
                    source14.CreateKeyframe(source14.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source14.CreateKeyframe(source14.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 15:
                    source15.CreateKeyframe(source15.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source15.CreateKeyframe(source15.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 16:
                    source16.CreateKeyframe(source16.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source16.CreateKeyframe(source16.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 17:
                    source17.CreateKeyframe(source17.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source17.CreateKeyframe(source17.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 18:
                    source18.CreateKeyframe(source18.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source18.CreateKeyframe(source18.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 19:
                    source19.CreateKeyframe(source19.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source19.CreateKeyframe(source19.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 20:
                    source20.CreateKeyframe(source20.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source20.CreateKeyframe(source20.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 21:
                    source21.CreateKeyframe(source21.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source21.CreateKeyframe(source21.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 22:
                    source22.CreateKeyframe(source22.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source22.CreateKeyframe(source22.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 23:
                    source23.CreateKeyframe(source23.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source23.CreateKeyframe(source23.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 24:
                    source24.CreateKeyframe(source24.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source24.CreateKeyframe(source24.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 25:
                    source25.CreateKeyframe(source25.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source25.CreateKeyframe(source25.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%27 == 26:
                    source27.CreateKeyframe(source27.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=0.0,initdirection=0.0, initspeedrandrange=0.0,initdirectionrandrange=0.0, particlesperframe=1)
                    source27.CreateKeyframe(source27.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
            else:
                source26.CreateKeyframe(source26.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=10.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=20.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                source26.CreateKeyframe(source26.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)

    screen.fill((10, 0, 50))
    screen.fill((255, 255, 255), rect=(25, 25, 1200, 625))
    if ct == 1:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
    elif ct == 2:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
    elif ct == 3:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
    elif ct == 4:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
    elif ct == 5:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
    elif ct == 6:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
    elif ct == 7:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
    elif ct == 8:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
    elif ct == 9:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
    elif ct == 10:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
    elif ct == 11:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
    elif ct == 12:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
    elif ct == 13:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
    elif ct == 14:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
    elif ct == 15:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
    elif ct == 16:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
    elif ct == 17:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
    elif ct == 18:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
    elif ct == 19:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
    elif ct == 20:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
    elif ct == 21:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
    elif ct == 22:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
        constants.ck = 22
        effect22.Update()
        effect22.Redraw()
    elif ct == 23:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
        constants.ck = 22
        effect22.Update()
        effect22.Redraw()
        constants.ck = 23
        effect23.Update()
        effect23.Redraw()
    elif ct == 24:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
        constants.ck = 22
        effect22.Update()
        effect22.Redraw()
        constants.ck = 23
        effect23.Update()
        effect23.Redraw()
        constants.ck = 24
        effect24.Update()
        effect24.Redraw()
    elif ct == 25:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
        constants.ck = 22
        effect22.Update()
        effect22.Redraw()
        constants.ck = 23
        effect23.Update()
        effect23.Redraw()
        constants.ck = 24
        effect24.Update()
        effect24.Redraw()
        constants.ck = 25
        effect25.Update()
        effect25.Redraw()
    elif ct == 26:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
        constants.ck = 22
        effect22.Update()
        effect22.Redraw()
        constants.ck = 23
        effect23.Update()
        effect23.Redraw()
        constants.ck = 24
        effect24.Update()
        effect24.Redraw()
        constants.ck = 25
        effect25.Update()
        effect25.Redraw()
        constants.ck = 26
        effect27.Update()
        effect27.Redraw()
    elif ct == 27:
        constants.ck = 1
        effect1.Update()
        effect1.Redraw()
        constants.ck = 2
        effect2.Update()
        effect2.Redraw()
        constants.ck = 3
        effect3.Update()
        effect3.Redraw()
        constants.ck = 4
        effect4.Update()
        effect4.Redraw()
        constants.ck = 5
        effect5.Update()
        effect5.Redraw()
        constants.ck = 6
        effect6.Update()
        effect6.Redraw()
        constants.ck = 7
        effect7.Update()
        effect7.Redraw()
        constants.ck = 8
        effect8.Update()
        effect8.Redraw()
        constants.ck = 9
        effect9.Update()
        effect9.Redraw()
        constants.ck = 10
        effect10.Update()
        effect10.Redraw()
        constants.ck = 11
        effect11.Update()
        effect11.Redraw()
        constants.ck = 12
        effect12.Update()
        effect12.Redraw()
        constants.ck = 13
        effect13.Update()
        effect13.Redraw()
        constants.ck = 14
        effect14.Update()
        effect14.Redraw()
        constants.ck = 15
        effect15.Update()
        effect15.Redraw()
        constants.ck = 16
        effect16.Update()
        effect16.Redraw()
        constants.ck = 17
        effect17.Update()
        effect17.Redraw()
        constants.ck = 18
        effect18.Update()
        effect18.Redraw()
        constants.ck = 19
        effect19.Update()
        effect19.Redraw()
        constants.ck = 20
        effect20.Update()
        effect20.Redraw()
        constants.ck = 21
        effect21.Update()
        effect21.Redraw()
        constants.ck = 22
        effect22.Update()
        effect22.Redraw()
        constants.ck = 23
        effect23.Update()
        effect23.Redraw()
        constants.ck = 24
        effect24.Update()
        effect24.Redraw()
        constants.ck = 25
        effect25.Update()
        effect25.Redraw()
        constants.ck = 26
        effect27.Update()
        effect27.Redraw()
        constants.ck = 27
        effect26.Update()
        effect26.Redraw()
    pygame.display.update()
    clock.tick(100)