import pygame
from pygame.locals import *

import player
import sprite

def init(g,r,p):
    s = sprite.Sprite3(g,r,'shoots/%s-draco-shoot'%(p.facing),(0,0,5,5))

    s.rect.centerx = r.centerx
    s.rect.centery = r.centery

    s.groups.add('solid')
    s.groups.add('dracoshoot')
    #s.groups.add('enemy')
    s.hit_groups.add('player')

    s.hit = hit
    g.sprites.append(s)
    s.loop = loop
    s.life = 100
    s.strength = 1
    #if big: s.strength = 3
    
    s.vx = 1
    if p.facing == 'left':
        s.vx = -1
    s.vy = 1
    s.rect.centerx += s.vx*(0+s.rect.width/2)
    s.rect.centery += 6 
    
    return s
    
def loop(g,s):
    s.rect.x += s.vx*2
    s.rect.y += s.vy
    s.life -= 1
    if s.life == 0:
        s.active = False
        #die(g,s)

def hit(g,a,b): 
    player.damage(g,b)
    a.active = False
    #die(g,a)
    #a.act
    

    #b.strength -= a.strength
    #if b.strength <= 0:
        #b.active = False
