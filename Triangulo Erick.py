#Erick Octavio Nolasco Machuca 17401029 Grupo: C16
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import math

def rectaADD(xi,yi,xf,yf):
    dx = xf-xi
    dy = yf-yi

    if abs(dx) >= abs(dy):
        pasos = abs(dx)
    else:
        pasos = abs(dy)
    
    incx = dx/pasos
    incy = dy/pasos
    x = xi
    y = yi
    i = 0
    glColor(0,0,1) #RGB
    glBegin(GL_POINTS)
    while i <= pasos:
        glVertex2i(round(x),round(y))
        x += incx
        y += incy
        i += 1
    glEnd()

class Triangulo:
    def __init__(self,lado):
        self.lado = lado
    
    def trazar(self):
        Hip = (self.lado/2)/math.cos(math.pi/6)
        Opuesto = Hip*math.sin(math.pi/6)
        
        rectaADD(-self.lado/2,-Opuesto,0,Hip)
        rectaADD(0,Hip,self.lado/2,-Opuesto)
        rectaADD(self.lado/2,-Opuesto,-self.lado/2,-Opuesto)

       
        
        
def main():
    glfw.init()

    window = glfw.create_window(401*2,401*2,"0302",None,None)
    glfw.make_context_current(window)

    glClearColor(1,1,1,0) 

    gluOrtho2D(-1000*2,1000*2,-1000*2,1000*2)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(0,0,0) 
        glBegin(GL_POINTS)
        for i in range(-1000*2,1001*2):
            glVertex2i(i,0)
            glVertex2i(0,i)
        glEnd()

        glColor(1,0,0)
        triangulo = Triangulo(300*6)
        triangulo.trazar()
    
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()