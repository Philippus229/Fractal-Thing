import pygame, math, colorsys
from numpy import array

def translate(value, from_min, from_max, to_min, to_max):
    return (value-from_min*(from_min < 0))*((abs(to_min)+to_max)/(abs(from_min)+from_max))+to_min*(to_min < 0)

windowsize = [1024, 1024]
resolution = [1024, 1024]
#angle = 0 #for fractal animation

def get_fractal_pixel_color(c):
    constc = c #mandelbrot set
    gr = (1+math.sqrt(5))/2 #golden ratio
    #constc = [1-gr, 0]           #julia set 1
    #constc = [gr-2, gr-1]        #julia set 2
    #constc = [0.285, 0]          #julia set 3
    #constc = [0.285, 0.01]       #julia set 4
    #constc = [0.45, 0.1428]      #julia set 5
    #constc = [-0.70176, -0.3842] #julia set 6
    #constc = [-0.835, -0.2321]   #julia set 7
    #constc = [-0.8, 0.156]       #julia set 8
    #constc = [-0.7269, 0.1889]   #julia set 9
    #constc = [0, -0.8]           #julia set 10
    #constc = [math.sin(angle), math.cos(angle)] #fractal animation
    z = c
    maxiterations = 255
    for i in range(maxiterations):
        if abs(z[0]+z[1]) > 2:
            break
        z = [z[0]*z[0]-z[1]*z[1]+constc[0], 2*z[0]*z[1]+c[1]]
        i += 1
    i = 0.00000000001 if i == 0 else i
    return tuple((255*array(colorsys.hsv_to_rgb(i/255, 1, 1))).astype(int)) if i < maxiterations else (0, 0, 0) #colored
    #x = 255*math.sqrt(i/maxiterations) #greyscale
    #return (x, x, x) if i < maxiterations else (0, 0, 0) #greyscale

def render_fractal():
    for y in range(resolution[1]):
        for x in range(resolution[0]):
            tmpnum = [translate(x, 0, resolution[0], -2.5, 2.5), translate(y, 0, resolution[1], -2.5, 2.5)]
            color = get_fractal_pixel_color(tmpnum)
            if not windowsize == resolution:
                for px in range(int(windowsize[0]/resolution[0])+1):
                    for py in range(int(windowsize[1]/resolution[1])+1):
                        surface.set_at((int(x*(windowsize[0]/resolution[0])+px), int(y*(windowsize[1]/resolution[1])+py)), color)
            else:
                surface.set_at((x, y), color)

pygame.init()
surface = pygame.display.set_mode(windowsize)
pygame.display.set_caption("Fractal Thing")
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    render_fractal()
    pygame.display.flip()
    #angle += 0.1 #for fractal animation
pygame.quit()
