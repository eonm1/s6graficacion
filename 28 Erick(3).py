#Erick Octavio Nolasco Machuca

import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np

tamVentana = 500
nomVentana = "17401029"
xMin,xMax = -10,10
yMin,yMax = -10,10

class Figura:
    def __init__(self):
        self.vertices = np.array([[0.0,0.0],
                                  [2.0,0.0],
                                  [2.0,-2.0],
                                  [-2.0,-2.0],
                                  [-2.0,2.0],
                                  [-1.0,2.0],
                                  [-1.0,1.0],
                                  [0.0,1.]],dtype=np.float32)
        self.nVertices = len(self.vertices)
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for v in self.vertices:
            glVertex2fv(v)
        glEnd()
    def trasladar(self,tx,ty):
        for i in range(self.nVertices):
            x,y = self.vertices[i]
            self.vertices[i][0] = x + tx
            self.vertices[i][1] = y + ty
    def rotar(self,theta):
        theta = np.radians(theta)
        for i in range(self.nVertices):
            x,y = self.vertices[i]
            self.vertices[i][0] = x*np.cos(theta) - y*np.sin(theta)
            self.vertices[i][1] = x*np.sin(theta) + y*np.cos(theta)

    def escalar(self,sx,sy):
        for i in range(self.nVertices):
            x,y = self.vertices[i]
            self.vertices[i][0] = x * sx
            self.vertices[i][1] = y * sy

def main():
    if not glfw.init():
        return

    window = glfw.create_window(tamVentana,tamVentana,nomVentana,None,None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glClearColor(1,1,1,0) 
    gluOrtho2D(xMin,xMax,yMin,yMax)

    figura = Figura()
    
    figura.rotar(45)
    figura.escalar(2,2)
    figura.trasladar(1.4,-1.4)
    
    #cruz.escalar(2,2)
    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(0,0,0) 
        glBegin(GL_LINES)
        glVertex2i(xMin,0)
        glVertex2i(xMax,0)
        glVertex2i(0,yMin)
        glVertex2i(0,yMax)
        glEnd()

        glColor(1,0,0)
        figura.trazar()

        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
