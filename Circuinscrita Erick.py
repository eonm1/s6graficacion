#Erick Octavio Nolasco Machuca 17401029 C16
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
class Circunferencia:
    def __init__(self,radio):
        self.radio = radio
    def trazar(self):
        Tx = self.radio/(1/math.cos(math.pi/6))
        Ty = Tx*math.tan(math.pi/6)
        x = 0
        y = self.radio
        DPk = 3-2*self.radio
        glBegin(GL_POINTS)
        while x<=y:
            glVertex2i(x,y)
            glVertex2i(x,-y)
            glVertex2i(-x,y)
            glVertex2i(-x,-y)
            glVertex2i(y,x)
            glVertex2i(y,-x)
            glVertex2i(-y,x)
            glVertex2i(-y,-x)
            if DPk>=0:
                DPk += 4*(x-y)+10
                y-=1
            else:
                DPk += 4*x+6
            x+=1
        glEnd()
        rectaADD(-Tx,-Ty,0,self.radio)
        rectaADD(0,self.radio,Tx,-Ty)
        rectaADD(Tx,-Ty,-Tx,-Ty)
        
def main():
    glfw.init()

    window = glfw.create_window(401,401,"17 Circunferencia circuinscrita en un triangulo",None,None)
    glfw.make_context_current(window)

    glClearColor(1,1,1,0) 

    gluOrtho2D(-200,200,-200,200)

    while not glfw.window_should_close(window):
        glfw.poll_events()
        glClear(GL_COLOR_BUFFER_BIT)

        glColor(0,0,0) 
        glBegin(GL_POINTS)
        for i in range(-200,201):
            glVertex2i(i,0)
            glVertex2i(0,i)
        glEnd()

        glColor(1,0,0)
        Circunferencia1 = Circunferencia(100)
        Circunferencia1.trazar()
    
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()