from StringIO import StringIO

from numpy import sin, arange, pi, concatenate
from numpy.random import random

import matplotlib
matplotlib.use('cairo')
from matplotlib.pyplot import *

import pyglet

#pyglet.clock.set_fps_limit(2)
window = pyglet.window.Window(800,800)

width, height = 640, 480
img = pyglet.image.ImageData(width,height,'RGBA','\x00'*width*height*4,-width*4)


@window.event
def on_draw() :
    window.clear()
    img.blit(window.width/2-img.width/2,window.height/2-img.height/2)
    fps_label = pyglet.text.Label(str(pyglet.clock.get_fps()),x=18,y=18)
    fps_label.draw()
    #print pyglet.clock.get_fps()

plot_i = 0.
f = figure()
sin_x = sin(arange(0,2*pi,1./100))
def plot_image(dt=None) :
    global img, plot_i, f, sin_x
    sin_x_slice = concatenate((sin_x[plot_i:],sin_x[0:plot_i]))
    f.clf()
    f.gca().plot(sin_x_slice)
    width, height = f.canvas.get_width_height()
    s = StringIO()
    f.canvas.print_rgb(s)
    s.seek(0)
    img.set_data('RGBA',-width*4,s.read())
    #img_data = s.read()

    #img = pyglet.image.ImageData(width,height,'RGBA',img_data,-width*4)
    plot_i += 5
    plot_i = plot_i % sin_x.size

def new_number(dt=None) :
    global label

    label = pyglet.text.Label(str(random()),
    font_name='Times New Roman',
    font_size=36,
    x=window.width//2, y=window.height//2,
    anchor_x='center', anchor_y='center')

    label.draw()

plot_image()
new_number()
fps = 60
#pyglet.clock.schedule_interval(new_number,1./fps)
pyglet.clock.schedule_interval(plot_image,1./fps)
pyglet.app.run()
