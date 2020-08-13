#Erick Octavio Nolasco Machuca 17401029
#27
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
tamVentana = 500
nomVentana = "17401029"
xMin,xMax = -10,10
yMin,yMax = -10,10
########################
n = 20
########################
class Triangulo:
    def __init__(self):
        self.vertices = np.array([[-0.5,-0.27],[0.5,-0.27],[0,0.59]],dtype=np.float32)
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    def trasladar(self,tx,ty):
        self.vertices += np.array([tx,ty],dtype=np.float32)
    def rotar(self,degrees):
        for l in self.vertices:
            tpx = l[0]*np.cos(degrees)-l[1]*np.sin(degrees)
            tpy = l[0]*np.sin(degrees)+l[1]*np.cos(degrees)
            l[0],l[1]=tpx,tpy
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
    lista = []
    for i in range(n+1):
        lista.append(Triangulo())
    i = 0
    for theta in np.linspace(0,2*np.pi,n+1):
        lista[i].rotar(3*np.pi/2+theta)
        lista[i].trasladar(7*np.cos(theta),7*np.sin(theta))
        i += 1
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
        for triangulo in lista:
            triangulo.trazar()
        glfw.swap_buffers(window)
    glfw.terminate()
if __name__ == "__main__":
    main()