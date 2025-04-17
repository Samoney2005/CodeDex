from turtle import *
import colorsys 

speed(0)
bgcolor("black")
h = 0
for i in range(16):
    for j in range(18):
        c = colorsys.hsv_to_rgb(h, s:1, v:1)
        color(c)
        h += 0.005
        rt(90)
        circle(150 - j * 6, extent:90)
        lt(90)
        circle(150 - j * 6, extent:90)
        rt(180)
    circle(radius:40, extent:24)
done ()
