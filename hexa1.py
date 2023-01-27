import sys
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math
red=1.0
green=0.0
blue=0.0
red1=1.0
green1=0.0
blue1=0.0
tx = 0.0
ty = 0.0
theta = 0.0
tx1 = 0.0
ty1 = 0.0
theta1 = 0.0
tx2 = 0.15
ty2 = 1.7
theta2 = -35
poly=0
def hexa1():
    glColor3f(red, green, blue)
    glBegin(GL_POLYGON)
    glVertex2f(0.9, 2.0)
    glVertex2f(0.1, 1.2)
    glVertex2f(0.3, 0.2)
    glVertex2f(1.5, 0.2)
    glVertex2f(1.7, 1.2)

    glEnd()
def hexa2():
    glColor3f(red1, green1, blue1)
    glBegin(GL_POLYGON)
    glVertex2f(0.9+1.45, 2.0)
    glVertex2f(0.13+1.45, 1.5)
    glVertex2f(0.13+1.45, 0.5)
    glVertex2f(1.2+1.45, 0.0)
    glVertex2f(2.0+1.45, 0.55)
    glVertex2f(1.9+1.45, 1.6)
    glEnd()
    glFlush()

def myDisplay():
    glClear(GL_COLOR_BUFFER_BIT)
    # Translate hexa1
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glTranslatef(tx1,ty1,0.0)
    glRotatef(theta1, 0.0, 0.0, 1.0)
    hexa1()
    glPopMatrix()
    # Translate hexa2
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glTranslatef(tx2,ty2,0.0)
    glRotatef(theta2, 0.0, 0.0, 1.0)
    hexa2()
    glPopMatrix()
    glFlush()
    glutSwapBuffers()







def myInit():

   glClearColor(1.0, 1.0, 1.0, 0.0)
   glColor3f(1.0, 1.0, 1.0)
   glMatrixMode(GL_PROJECTION)
   glLoadIdentity()
   gluOrtho2D(0.0, 4.0, 0.0, 3.0)


def menu(key,x,y):
    
    global red, green, blue,red1, green1, blue1
    global poly,tx,ty,theta,poly1,tx1,ty1,theta1,poly2,tx2,ty2,theta2
    if key == b'0':
        poly=0
    if key == b'1':
        poly=1
    if key == b'2':
        poly=2
    if key== GLUT_KEY_UP:
        if poly ==1:
            ty1+=0.05
        if poly ==2:
            ty2+=0.05
        if poly ==0:
            ty1+=0.05
            ty2+=0.05
        
    elif key == GLUT_KEY_DOWN:
        if poly ==1:
            ty1-=0.05
        if poly ==2:
            ty2-=0.05
        if poly ==0:
            ty1-=0.05
            ty2-=0.05
    elif key== GLUT_KEY_RIGHT:
        if poly ==1:
            tx1+=0.05
        if poly ==2:
            tx2+=0.05
        if poly ==0:
            tx1+=0.05
            tx2+=0.05
    elif key == GLUT_KEY_LEFT:
        if poly ==1:
            tx1-=0.05
        if poly ==2:
            tx2-=0.05
        if poly ==0:
            tx1-=0.05
            tx2-=0.05
    elif key == b'r':
        if poly ==1:
            red = 1.0
            green = 0.0
            blue = 0.0
        if poly ==2:
            red1 = 1.0
            green1 = 0.0
            blue1 = 0.0
        if poly ==0:
            red = 1.0
            green = 0.0
            blue = 0.0
            red1 = 1.0
            green1 = 0.0
            blue1 = 0.0
            
        
    elif key == b'g':
        if poly ==1:
            red = 0.0
            green = 1.0
            blue = 0.0
        if poly ==2:
            red1 = 0.0
            green1 = 1.0
            blue1 = 0.0
        if poly ==0:
            red = 0.0
            green = 1.0
            blue = 0.0
            red1 = 0.0
            green1 = 1.0
            blue1 = 0.0
        
        
    elif key == B'b':
        if poly ==1:
            red = 0.0
            green = 0.0
            blue = 1.0
        if poly ==2:
            red1 = 0.0
            green1 = 0.0
            blue1 = 1.0
        if poly ==0:
            red = 0.0
            green = 0.0
            blue = 1.0
            red1 = 0.0
            green1 = 0.0
            blue1 = 1.0
    elif key == GLUT_KEY_F12:
        if poly == 1:
            theta1 -= 5.0
        if poly == 2:
            theta2 -= 5.0
        if poly == 0:
            theta1 -= 5.0
            theta2 -= 5.0

    elif key == GLUT_KEY_F9:
        if poly == 1:
            theta1 += 5.0
        if poly == 2:
            theta2 += 5.0
        if poly == 0:
            theta1 += 5.0
            theta2 += 5.0

    elif key == GLUT_KEY_HOME:
        glLoadIdentity()
        hexa1()

    glutPostRedisplay()


def setupmenu():
    ms = glutCreateMenu(menuColor)
    glutAddMenuEntry("red", 1)
    glutAddMenuEntry("green", 2)
    glutAddMenuEntry("blue", 3)
    ms2 = glutCreateMenu(menuColor)
    glutAddMenuEntry("red", 4)
    glutAddMenuEntry("green", 5)
    glutAddMenuEntry("blue", 6)
    ms3 = glutCreateMenu(menuColor)
    glutAddMenuEntry("red", 7)
    glutAddMenuEntry("green", 8)
    glutAddMenuEntry("blue", 9)
    ms1 = glutCreateMenu(menuColor)
    glutAddSubMenu("Both shapes", ms3)
    glutAddSubMenu("Pentagon", ms)
    glutAddSubMenu("Hexagon", ms2)

    glutCreateMenu(menuColor)
    glutAddSubMenu("shape", ms1)
    glutAddMenuEntry("exit", 4)
    glutAttachMenu(GLUT_RIGHT_BUTTON)

def menuColor(color):
    global red, green, blue,red1, green1, blue1
    if color == 1:
        red = 1.0
        green = 0.0
        blue = 0.0
    elif color == 2:
        red = 0.0
        green = 1.0
        blue = 0.0
    elif color == 3:
        red1 = 0.0
        green1 = 0.0
        blue1 = 1.0
    elif color == 4:
        red1 = 1.0
        green1 = 0.0
        blue1 = 0.0
    elif color == 5:
        red1 = 0.0
        green1 = 1.0
        blue1 = 0.0
    elif color == 6:
        red1 = 0.0
        green1 = 0.0
        blue1 = 1.0
    elif color == 7:
        red = 1.0
        green = 0.0
        blue = 0.0
        red1 = 1.0
        green1 = 0.0
        blue1 = 0.0
    elif color == 8:
        red = 0.0
        green = 1.0
        blue = 0.0
        red1 = 0.0
        green1 = 1.0
        blue1 = .0
    elif color == 9:
        red = 0.0
        green = 0.0
        blue = 1.0
        red1 = 0.0
        green1 = 0.0
        blue1 = 1.0

    glutPostRedisplay()
    return color

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(750, 450)
    glutInitWindowPosition(0, 0)
    glutCreateWindow("LAB 7 - Abdullah Alahmadi")

    glutDisplayFunc(myDisplay)
    glutSpecialFunc(menu)
    glutKeyboardFunc(menu)
    setupmenu()
    myInit()

    glutMainLoop()

main()
