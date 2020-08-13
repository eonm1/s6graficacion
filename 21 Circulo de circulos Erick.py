#Erick Octavio Nolasco Machuca 17401029 C16
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
xMin,xMax = -10,10
yMin,yMax = -10,10

class Circunferencia:
    def __init__(self,r):
        self.vertices = np.array(
            [[r*np.cos(i),r*np.sin(i)] for i in np.linspace(0,2*np.pi)])
        
    def trazar(self):
        glBegin(GL_LINE_LOOP)
        for vertice in self.vertices:
            glVertex2fv(vertice)
        glEnd()
    def trasladar (self,x,y):
        self.vertices += np.array([x,y],dtype=np.float32)

def main():
    #-----------------------------------------------
    n=15 #cambiar el numero de circunferencias
    #-----------------------------------------------
    
    if not glfw.init():
        return
    window = glfw.create_window(500,500,"Circulo de cirulos 21",None,None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glClearColor(1,1,1,0) 
    gluOrtho2D(xMin,xMax,yMin,yMax)
    
    arregloCir = []
    puntos = 0
    
    for i in range(n):
        arregloCir.append(Circunferencia(.5))
    len(arregloCir)
    for i in arregloCir:
        rad = np.radians(puntos)
        x = 6*np.sin(rad) #Cambiar el tamaño de el circulo mayor
        y = 6*np.cos(rad) #Aqui tambien
        i.trasladar(x,y)
        puntos += 360/n
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

        glColor(0,0,1)
        
        for i in arregloCir:
            i.trazar()

        glColor(1,0,0)
                        
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()
