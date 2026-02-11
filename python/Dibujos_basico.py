from tkinter import *
from Main_basico import *

class perilla():
    def __init__(self,parent,color,x,y,move_1):
        self.lienzo = Canvas( parent, width=130 , height=130 , bg=color , highlightbackground=color,)
        self.lienzo.place(x=x,y=y)
        j = 0
        k = 0
        self.lienzo.create_oval(j+2,k+2,j+131,k+131,width=2,fill="lightgrey")
        selector_1 = 0
        selector_2 = 0
        
        if move_1 == 1: #selector pos1
                self.lienzo.delete(selector_2)
                selector_1 =self.lienzo.create_polygon(j+25,k+10,j+5,k+30,j+105,k+130,j+125,k+110,width=2)
        if move_1 == 0:#barra selector pos2
                self.lienzo.delete(selector_1)
                selector_2 = self.lienzo.create_polygon(j+105,k+10,j+125,k+30,j+25,k+130,j+5,k+110,width=2)
   
        
class barra():
    def __init__(self,parent,largo,alto,color,x,y,move_1,move_2,move_3,move_4):
        self.lienzo = Canvas( parent, width=largo , height=alto , bg=color , highlightbackground=color,)
        self.lienzo.place(x=x,y=y)
# Barra 1
        a = 10
        b = 10
        c = 30
        d = 170
        l1 = [a,b,c,b]
        l2 = [c,b,c,d]
        l3 = [c,d,a,d]
        l4 = [a,d,a,b]
        points_f = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_f, outline='black', fill='grey', width=2)
        l1 = [a,move_1,c,move_1]
        l2 = [c,move_1,c,d]
        l3 = [c,d,a,d]
        l4 = [a,d,a,move_1]
        points_in = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_in, outline='black', fill='blue', width=2)
            
# Barra 2
        l1 = [a+30,b,c+30,b]
        l2 = [c+30,b,c+30,d]
        l3 = [c+30,d,a+30,d]
        l4 = [a+30,d,a+30,b]
        points_f = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_f, outline='black', fill='grey', width=2)

        l1 = [a+30,move_2,c+30,move_2]
        l2 = [c+30,move_2,c+30,d]
        l3 = [c+30,d,a+30,d]
        l4 = [a+30,d,a+30,move_2]
        points_in = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_in, outline='black', fill='blue', width=2)
        
# Barra 3
        l1 = [a+60,b,c+60,b]
        l2 = [c+60,b,c+60,d]
        l3 = [c+60,d,a+60,d]
        l4 = [a+60,d,a+60,b]
        points_f = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_f, outline='black', fill='grey', width=2)

        l1 = [a+60,move_3,c+60,move_3]
        l2 = [c+60,move_3,c+60,d]
        l3 = [c+60,d,a+60,d]
        l4 = [a+60,d,a+60,move_3]
        points_in = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_in, outline='black', fill='blue', width=2)

# Barra 3
        l1 = [a+90,b,c+90,b]
        l2 = [c+90,b,c+90,d]
        l3 = [c+90,d,a+90,d]
        l4 = [a+90,d,a+90,b]
        points_f = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_f, outline='black', fill='grey', width=2)

        l1 = [a+90,move_4,c+90,move_4]
        l2 = [c+90,move_4,c+90,d]
        l3 = [c+90,d,a+90,d]
        l4 = [a+90,d,a+90,move_4]
        points_in = [l1,l2,l3,l4]
        self.barra_fondo = self.lienzo.create_polygon(points_in, outline='black', fill='blue', width=2)
        