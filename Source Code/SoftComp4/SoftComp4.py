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
source1 = effect1.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source2 = effect2.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source3 = effect3.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source4 = effect4.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source5 = effect5.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source6 = effect6.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source7 = effect7.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source8 = effect8.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source9 = effect9.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)
source10 = effect10.CreateSource(initspeed=3.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=8.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(110, 10, 100), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=24.0)


effect11 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
source11 = effect11.CreateSource(initspeed=10.0, initdirection= 2*math.pi*random.random(), initspeedrandrange=20.0, initdirectionrandrange=2*math.pi,
                             particlelife=1000, colour=(10, 210, 180), drawtype=PyIgnition.DRAWTYPE_BUBBLE, radius=15.0)

effect12 = PyIgnition.ParticleEffect(screen, (25, 25), (1200, 625))
source12 = effect12.CreateSource(initspeed=0.0, initdirection= 0.0, initspeedrandrange=0.0, initdirectionrandrange=0.0,
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
            if ct < 12:
                if ct%12 == 1:
                    source1.CreateKeyframe(source1.curframe + 1, pos=pygame.mouse.get_pos(), initspeed = 3.0, initdirection = 2*math.pi*random.random(), initspeedrandrange = 8.0, initdirectionrandrange = 2*math.pi, particlesperframe=1)
                    source1.CreateKeyframe(source1.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 2:
                    source2.CreateKeyframe(source2.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source2.CreateKeyframe(source2.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 3:
                    source3.CreateKeyframe(source3.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source3.CreateKeyframe(source3.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 4:
                    source4.CreateKeyframe(source4.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source4.CreateKeyframe(source4.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 5:
                    source5.CreateKeyframe(source5.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source5.CreateKeyframe(source5.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 6:
                    source6.CreateKeyframe(source6.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source6.CreateKeyframe(source6.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 7:
                    source7.CreateKeyframe(source7.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source7.CreateKeyframe(source7.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 8:
                    source8.CreateKeyframe(source8.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source8.CreateKeyframe(source8.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 9:
                    source9.CreateKeyframe(source9.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source9.CreateKeyframe(source9.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 10:
                    source10.CreateKeyframe(source10.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=3.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=8.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                    source10.CreateKeyframe(source10.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
                elif ct%12 == 11:
                    source12.CreateKeyframe(source12.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=0.0,initdirection=0.0, initspeedrandrange=0.0,initdirectionrandrange=0.0, particlesperframe=1)
                    source12.CreateKeyframe(source12.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)
            else:
                source11.CreateKeyframe(source11.curframe + 1, pos=pygame.mouse.get_pos(), initspeed=10.0,initdirection=2 * math.pi * random.random(), initspeedrandrange=20.0,initdirectionrandrange=2 * math.pi, particlesperframe=1)
                source11.CreateKeyframe(source11.curframe + 2, pos=pygame.mouse.get_pos(), particlesperframe=0)

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
        effect12.Update()
        effect12.Redraw()
    else:
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
        effect12.Update()
        effect12.Redraw()
        constants.ck = 12
        effect11.Update()
        effect11.Redraw()
    pygame.display.update()
    clock.tick(100)

