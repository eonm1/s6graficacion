'''
Erick Octavio Nolasco Machuca
17401029
Practica 33
'''
import glfw
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
import time

class Figura:
    def __init__(self):
        puntos = []
        puntos.append([4,-4,4])
        puntos.append([6,-4,4])
        puntos.append([6,-4,-4])
        puntos.append([4,-4,-4])
        puntos.append([4,2,-4])
        puntos.append([-4,2,-4])
        puntos.append([-4,4,-4])
        puntos.append([-4,4,4])
        puntos.append([-4,2,4])
        puntos.append([4,2,4])
        puntos.append([4,-4,4])
        puntos.append([6,-4,4])
        puntos.append([6,4,4])

        puntos.append([-4,4,4])
        puntos.append([-4,4,-4])
        puntos.append([6,4,-4])
        puntos.append([6,4,4])
        puntos.append([6,4,-4])
        puntos.append([6,-4,-4])
        puntos.append([4,-4,-4])
        puntos.append([-4,2,-4])
        puntos.append([-4,2,4])
        puntos.append([4,-4,4])
        puntos.append([4,-4,-4])

            
        self.vertices_figura = np.array(puntos,dtype=np.float32)
        print(self.vertices_figura)
        #np.savetxt('figura_figura.csv',self.vertices_figura,delimiter=',')
      
        #self.vertices_figura = np.array(np.genfromtxt('figura.csv',delimiter=';'),dtype=np.float32)
        
     
    def dibuja(self):
        glColor(0.2,0.2,0.1)
        glBegin(GL_LINE_LOOP)
        for v in self.vertices_figura:
            glVertex3fv(v)
        glEnd()

    def escalar(self,sx,sy,sz):
        S = np.matrix([[sx,0,0,0],
                       [0,sy,0,0],
                       [0,0,sz,0],
                       [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_figura)):
            P = np.matrix([[self.vertices_figura[i][0]],
                            [self.vertices_figura[i][1]],
                            [self.vertices_figura[i][2]],
                            [1]],dtype=np.float32)
            Pp = S*P
            self.vertices_figura[i][0] = Pp[0]
            self.vertices_figura[i][1] = Pp[1]
            self.vertices_figura[i][2] = Pp[2]
  
  #**************************************METODOS********************************************
  
    def T(self,tx,ty,tz):
        S = np.matrix([[1,0,0,tx],[0,1,0,ty],[0,0,1,tz],[0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_figura)):
            P = np.matrix([[self.vertices_figura[i][0]],
                            [self.vertices_figura[i][1]],
                            [self.vertices_figura[i][2]],
                            [1]],dtype=np.float32)
            Pp = S*P
            self.vertices_figura[i][0] = Pp[0]
            self.vertices_figura[i][1] = Pp[1]
            self.vertices_figura[i][2] = Pp[2]
    def S(self,sx,sy,sz,xf,yf,zf):
        S=np.matrix([[sx,0,0,(-xf*sx)+xf],[0,sy,0,(-yf*sy)+yf],[0,0,sz,(-zf*sz)+zf],[0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_figura)):
            P = np.matrix([[self.vertices_figura[i][0]],
                            [self.vertices_figura[i][1]],
                            [self.vertices_figura[i][2]],
                            [1]],dtype=np.float32)
            Pp = S*P
            self.vertices_figura[i][0] = Pp[0]
            self.vertices_figura[i][1] = Pp[1]
            self.vertices_figura[i][2] = Pp[2]
    def Rz(self,theta,xr,yr,zr):
        S=np.matrix([[np.cos(theta),-np.sin(theta),0,(-xr*np.cos(theta))+(yr*np.sin(theta))+xr],
                     [np.sin(theta),np.cos(theta),0,(-xr*np.sin(theta))-(yr*np.cos(theta))+yr],
                     [0,0,1,0],
                     [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_figura)):
            P = np.matrix([[self.vertices_figura[i][0]],
                            [self.vertices_figura[i][1]],
                            [self.vertices_figura[i][2]],
                            [1]],dtype=np.float32)
            Pp = S*P
            self.vertices_figura[i][0] = Pp[0]
            self.vertices_figura[i][1] = Pp[1]
            self.vertices_figura[i][2] = Pp[2]
    
    def Rx(self,theta,xr,yr,zr):
        S=np.matrix([[1,0,0,0],
                     [0,np.cos(theta),-np.sin(theta),-yr*np.cos(theta)+zr*np.sin(theta)+yr],
                     [0,np.sin(theta),np.cos(theta),-yr*np.sin(theta)-zr*np.cos(theta)+zr],
                     [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_figura)):
            P = np.matrix([[self.vertices_figura[i][0]],
                            [self.vertices_figura[i][1]],
                            [self.vertices_figura[i][2]],
                            [1]],dtype=np.float32)
            Pp = S*P
            self.vertices_figura[i][0] = Pp[0]
            self.vertices_figura[i][1] = Pp[1]
            self.vertices_figura[i][2] = Pp[2]
    def Ry(self,theta,xr,yr,zr):
        S=np.matrix([[np.cos(theta),0,np.sin(theta),-xr*np.cos(theta)-zr*np.sin(theta)+xr],
                     [0,1,0,0],
                     [-np.sin(theta),0,np.cos(theta),xr*np.sin(theta)-zr*np.cos(theta)+zr],
                     [0,0,0,1]],dtype=np.float32)
        for i in range(len(self.vertices_figura)):
            P = np.matrix([[self.vertices_figura[i][0]],
                            [self.vertices_figura[i][1]],
                            [self.vertices_figura[i][2]],
                            [1]],dtype=np.float32)
            Pp = S*P
            self.vertices_figura[i][0] = Pp[0]
            self.vertices_figura[i][1] = Pp[1]
            self.vertices_figura[i][2] = Pp[2]
        
def dibuja_ejes():
    glColor(1,0,0)
    glBegin(GL_LINES)
    glVertex3i(-10,0,0)
    glVertex3i(10,0,0)
    glEnd()
    glColor(0,1,0)
    glBegin(GL_LINES)
    glVertex3i(0,-10,0)
    glVertex3i(0,10,0)
    glEnd()
    glColor(0,0,1)
    glBegin(GL_LINES)
    glVertex3i(0,0,10)
    glVertex3i(0,0,-10)
    glEnd()
   
def main():
    if not glfw.init():
        return

    window = glfw.create_window(500,500,"17401029",None,None)
    if not window:
        glfw.terminate()
        return
    
    glfw.make_context_current(window)
    glClearColor(1,1,1,0)

    #glViewport(0,0,500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-12,12,-12,12,1,50) #(left,right,buttom,top,near,far) Paralelo
    glMatrixMode(GL_MODELVIEW) 
    glLoadIdentity() 
    gluLookAt(10,10,10,0,0,0,0,1,0) #(eyeX,eyeY,eyeZ,centerX,centerY,centerZ,upX,upY,upZ)
    
    figura = Figura()
   

    x,z = 10,10
    r = np.sqrt(x**2+z**2)
    t = np.arctan(z/x)
    
    #figura.T(4,0,4)
    #figura.S(1.5,1.5,1.5,0,0,0)
    
    
    
    while not glfw.window_should_close(window):
        glfw.poll_events()
        
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glEnable(GL_DEPTH_TEST) #Para no dibujar lo "oculto" a vista
        #glPolygonMode(GL_FRONT_AND_BACK,GL_LINE)#GL_LINE alambrico GL_FILL superficie

        dibuja_ejes()
        figura.dibuja()
        
        time.sleep(0.1)
        #figura.Rz(0.1,5,5,5)
        figura.Ry(0.1,0,0,0)
        #figura.Rx(0.1,4,4,4)
        #glMatrixMode(GL_MODELVIEW) 
        #glLoadIdentity()
        #gluLookAt(r*np.cos(t),10,r*np.sin(t),0,0,0,0,1,0)
        #t += 0.04
        
        glfw.swap_buffers(window)
    
    glfw.terminate()

if __name__ == "__main__":
    main()