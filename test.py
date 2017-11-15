from math import *
from graphics import *
from random import *
class projectile:
    #removed 'height' because this program calculates the height the cannon reaches above its initial height,
    # and that is irrelevant to its initial height.
    def __init__(self, angle, velocity, h0):
        self.xpos = 0
        self.ypos = h0
        theta = radians(angle)
        self.xvel = velocity * cos(theta)
        self.yvel = velocity * sin(theta)

    def getX(self):
        return self.xpos

    def getY(self):
        return self.ypos

    #removed the parameter 'time', instead take 0.1 as the default
    def update(self, time):
        self.xpos = self.xpos + time * self.xvel
        yvel1 = self.yvel - time * 9.8
        self.ypos = self.ypos + time * (self.yvel + yvel1) / 2.0
        self.yvel = yvel1

#removed the getInput function.

#fixed the main function, puting angle and velocity as parameters instead of geting from input
#removed the line calculating horizontal distance
#fixed the while loop condition
def main(a, vel, h0, time):
    cannon = projectile(a, vel, h0)
    win = GraphWin('Cannon Ball', 900, 600)
    win.setCoords(-100,-150,1400,650)
    xaxis = Line(Point(-50,0), Point(1350,0))
    xaxis.draw(win)
    yaxis = Line(Point(0,-100), Point(0,600))
    yaxis.draw(win)
    for n in range(1,6):
        Line(Point(-3, n*100), Point(3, n*100)).draw(win)
        Text(Point(-25, n*100), str(n*100)).draw(win)
    for n in range(1,14):
        Line(Point(n*100, -3), Point(n*100, 3)).draw(win)
        Text(Point(n*100, -25), str(n*100)).draw(win)
    Line(Point(1350,0), Point(1340, 10)).draw(win)
    Line(Point(1350, 0), Point(1340, -10)).draw(win)
    Line(Point(0,600), Point(10,590)).draw(win)
    Line(Point(0,600), Point(-10,590)).draw(win)
    Text(Point(-25,-25), '0').draw(win)
    r = random()
    g = random()
    b = random()
    while cannon.ypos >= 0:
        cannon.update(time)
        p = Point(cannon.xpos, cannon.ypos)
        p.draw(win)
        p.setOutline(color_rgb(int((sin(r)+1)*110), int((sin(g)+1)*110), int((sin(b)+1)*110)))
        r += 0.01
        g += 0.02
        b += 0.03
    win.getMouse()
    win.close()

main(45, 100, 200, 0.02)
