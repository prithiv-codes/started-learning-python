import pygame
import sys
import math
import random
pygame.init()
clock=pygame.time.Clock()
screen=pygame.display.set_mode((800,800))
x=random.randint(100,700)
y=random.randint(100,700)
b_dir=[0,0]
p_hp=100
b_pos=[x,y]
t_pos=[600,400]
p_pos=[0,0]
b_speed=10
p_speed=5
b_alive=False
while True:
        b_rect=pygame.Rect([b_pos[0],b_pos[1],20,20])
        t_rect=pygame.Rect([t_pos[0],t_pos[1],5,10])
        p_rect=pygame.Rect([p_pos[0],p_pos[1],10,10])
        clock.tick(60)
        screen.fill((255,255,255))
        bullet=pygame.draw.rect(screen,(255,255,0),[b_pos[0],b_pos[1],20,20])
        pygame.draw.rect(screen,(0,255,0),[p_pos[0],p_pos[1],10,10])
        keys=pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        if b_pos[0]>799 or b_pos[0]<0 or b_pos[1]>799 or b_pos[1]<0 or p_rect.colliderect(b_rect):
            b_alive=False
            x=random.randint(100,700)
            y=random.randint(100,700)
        if b_alive==False:
            b_pos=[x,y]
            b_dir=[0,0]
            if b_pos[0]>=p_pos[0]:
                b_dir[0]-=b_speed
            if b_pos[0]<p_pos[0]:
                b_dir[0]+=b_speed
            if b_pos[1]>=p_pos[1]:
                b_dir[1]-=b_speed
            if b_pos[1]<p_pos[1]:
                b_dir[1]+=b_speed
            b_alive=True
        if b_alive == True:
                b_pos[0] += b_dir[0]
                b_pos[1] += b_dir[1]
        if keys[pygame.K_LEFT]:
            p_pos[0]-=p_speed
        if keys[pygame.K_RIGHT]:
            p_pos[0]+=p_speed
        if keys[pygame.K_UP]:
            p_pos[1]-=p_speed
        if keys[pygame.K_DOWN]:
            p_pos[1]+=p_speed
        p_pos[0]=min(795,max(0,p_pos[0]))
        p_pos[1]=min(790,max(0,p_pos[1]))
        pygame.display.flip()