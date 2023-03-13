# test2_pyganim.py - A pyganim test program.
#
# This test program is the same lightning bolt animation, but provides you with buttons and lots of debug information.
#
# The animation images come from POW Studios, and are available under an Attribution-only license.
# Check them out, they're really nice.
# http://powstudios.com/

import sys
import os
sys.path.append(os.path.abspath('..'))

import pygame
from pygame.locals import *
import time
import pyganim

pygame.init()

# set up the window
WINWIDTH = 640
WINHEIGHT = 480
windowSurface = pygame.display.set_mode((WINWIDTH, WINHEIGHT), 0, 32)
pygame.display.set_caption('Pyganim Control Panel')

# create the animation objects
boltAnim = pyganim.PygAnimation([('testimages/bolt_strike_0001.png', 200),
                                 ('testimages/bolt_strike_0002.png', 200),
                                 ('testimages/bolt_strike_0003.png', 200),
                                 ('testimages/bolt_strike_0004.png', 200),
                                 ('testimages/bolt_strike_0005.png', 200),
                                 ('testimages/bolt_strike_0006.png', 200),
                                 ('testimages/bolt_strike_0007.png', 200),
                                 ('testimages/bolt_strike_0008.png', 200),
                                 ('testimages/bolt_strike_0009.png', 200),
                                 ('testimages/bolt_strike_0010.png', 200)])

boltAnim.play()

BASICFONT = pygame.font.Font('freesansbold.ttf', 16)
WHITE = (255, 255, 255)
BGCOLOR = (100, 50, 50)

buttons = 'Play Pause Stop Toggle Rew. FF Loop Rev Vis PrevF NextF'.split(' ')
buttonDict = {}
leftPoint = 4
for button in buttons:
    buttonDict[button] = [BASICFONT.render(button, True, WHITE)]
    buttonDict[button].append(buttonDict[button][0].get_rect())
    pygame.draw.rect(buttonDict[button][0], WHITE, buttonDict[button][1], 1)
    buttonDict[button][1].bottom = WINHEIGHT - 4
    buttonDict[button][1].left = leftPoint
    leftPoint += buttonDict[button][1].width + 4

while True:
    windowSurface.fill(BGCOLOR)
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            for button in buttons:
                if buttonDict[button][1].collidepoint(event.pos):
                    if button == 'FF':
                        boltAnim.fastForward(100)
                    elif button == 'Loop':
                        boltAnim.loop = not boltAnim.loop
                    elif button == 'NextF':
                        boltAnim.nextFrame()

                    elif button == 'Pause':
                        boltAnim.pause()
                    elif button == 'Play':
                        boltAnim.play()
                    elif button == 'PrevF':
                        boltAnim.prevFrame()
                    elif button == 'Rev':
                        boltAnim.reverse()
                    elif button == 'Rew.':
                        boltAnim.rewind(100)
                    elif button == 'Stop':
                        boltAnim.stop()
                    elif button == 'Toggle':
                        boltAnim.togglePause()
                    elif button == 'Vis':
                        boltAnim.visibility = not boltAnim.visibility
    # draw the animations to the screen
    #boltAnim.currentFrameNum = 3
    #print(boltAnim.currentFrameNum)
    boltAnim.blit(windowSurface, (300, 4))
    for button in buttons:
        windowSurface.blit(buttonDict[button][0], buttonDict[button][1])

    # draw the info text
    stateSurf = BASICFONT.render(f'State: {boltAnim.state}', True, WHITE)
    stateRect = stateSurf.get_rect()
    stateRect.topleft = (4, 130)
    windowSurface.blit(stateSurf, stateRect)

    elapsedSurf = BASICFONT.render(f'Elapsed: {boltAnim.elapsed}', True, WHITE)
    elapsedRect = elapsedSurf.get_rect()
    elapsedRect.topleft = (150, 130)
    windowSurface.blit(elapsedSurf, elapsedRect)

    curFrameSurf = BASICFONT.render(
        f'Cur Frame Num: {boltAnim.currentFrameNum}', True, WHITE
    )
    curFrameRect = curFrameSurf.get_rect()
    curFrameRect.topleft = (380, 130)
    windowSurface.blit(curFrameSurf, curFrameRect)

    loopSurf = BASICFONT.render(f'Looping: {boltAnim.loop}', True, WHITE)
    loopRect = loopSurf.get_rect()
    loopRect.topleft = (4, 150)
    windowSurface.blit(loopSurf, loopRect)

    visSurf = BASICFONT.render(f'Vis: {boltAnim.visibility}', True, WHITE)
    visRect = visSurf.get_rect()
    visRect.topleft = (150, 150)
    windowSurface.blit(visSurf, visRect)

    rightNow = time.time()

    timeSurf = BASICFONT.render(f'Current Time: {rightNow}', True, WHITE)
    timeRect = timeSurf.get_rect()
    timeRect.topleft = (4, 170)
    windowSurface.blit(timeSurf, timeRect)

    playTimeSurf = BASICFONT.render(
        f'Play Start Time: {boltAnim._playingStartTime}', True, WHITE
    )
    playTimeRect = playTimeSurf.get_rect()
    playTimeRect.topleft = (4, 190)
    windowSurface.blit(playTimeSurf, playTimeRect)

    pauseTimeSurf = BASICFONT.render(
        f'Pause Start Time: {boltAnim._pausedStartTime}', True, WHITE
    )
    pauseTimeRect = pauseTimeSurf.get_rect()
    pauseTimeRect.topleft = (4, 210)
    windowSurface.blit(pauseTimeSurf, pauseTimeRect)

    diffTimeSurf = BASICFONT.render(
        f'Play - Pause Time: {boltAnim._playingStartTime - boltAnim._pausedStartTime}',
        True,
        WHITE,
    )
    diffTimeRect = diffTimeSurf.get_rect()
    diffTimeRect.topleft = (4, 230)
    windowSurface.blit(diffTimeSurf, diffTimeRect)

    diff2TimeSurf = BASICFONT.render(
        f'Current - Play Time: {rightNow - boltAnim._playingStartTime}',
        True,
        WHITE,
    )
    diff2TimeRect = diff2TimeSurf.get_rect()
    diff2TimeRect.topleft = (4, 250)
    windowSurface.blit(diff2TimeSurf, diff2TimeRect)

    diff3TimeSurf = BASICFONT.render(
        f'Current - Pause Time: {rightNow - boltAnim._pausedStartTime}',
        True,
        WHITE,
    )
    diff3TimeRect = diff3TimeSurf.get_rect()
    diff3TimeRect.topleft = (4, 270)
    windowSurface.blit(diff3TimeSurf, diff3TimeRect)


    pygame.display.update()

