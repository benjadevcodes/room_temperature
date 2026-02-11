import sys
from tkinter import *
from Comunication_basico import *
from Etiquetas_basico import *
import time
from Dibujos_basico import *

# Creacion de ventana principal + conexion a plc


class app():
    def __init__(self, ventMain):
        self.ventMain = ventMain
        self.ventMain.title("Proyecto Temp Sala")
        self.ventMain.geometry('900x600')
        self.ventMain.wm_attributes("-topmos", True)
        self.ventMain.resizable(width=True, height=True)
        host_sim = '127.0.0.1'    ### Simulacion Machine Expert Basic
        # host_sim = '192.168.0.50'   ### Simulacion Modbus Slave
        
        self.PLC = C_plc(host=host_sim, port=502)  # 
        self.canvas = Canvas(width=900, height=900, bg='lightgrey')
        self.canvas.pack(expand=NO, fill=BOTH)
        
## dibujo estructura edificio
        sala1 = self.canvas.create_rectangle(10, 10, 250, 250)
        sala2 = self.canvas.create_rectangle(250, 10, 500, 250)
        sala3 = self.canvas.create_rectangle(250, 250, 500, 500)
        tablero = self.canvas.create_rectangle(550, 320, 850, 580)
        
        self.x1 = Label(self.canvas)
        self.x1.place(x=15, y=15)
        self.x1.config(text="Sala 1")

        self.y2 = Label(self.canvas)
        self.y2.place(x=265, y=15)
        self.y2.config(text="Sala 2")
        
        self.y2 = Label(self.canvas)
        self.y2.place(x=260, y=260)
        self.y2.config(text="Sala 3")
        
        

# etiqueta
        self.etiqueta_1 = Label(self.ventMain)
        self.etiqueta_1.place(x=520, y=265)

        self.etiqueta_2 = Label(self.ventMain)
        self.etiqueta_2.place(x=580, y=265)

        self.etiqueta_3 = Label(self.ventMain)
        self.etiqueta_3.place(x=640, y=265)

# deslizadores
# Sala 1
        self.sala_1 = Scale(ventMain, from_=10000, to=0,
                            length=250, orient="vertical")
        self.sala_1.place(x=520, y=10)
# Sala 2
        self.sala_2 = Scale(ventMain, from_=10000, to=0,
                            length=250, orient="vertical")
        self.sala_2.place(x=580, y=10)
# Sala 3     
        self.sala_3 = Scale(ventMain, from_=10000, to=0,
                            length=250, orient="vertical")
        self.sala_3.place(x=640, y=10)



# luces (por coil)

# luz 1
        dimens_L1 = 70  # dimension luz
        self.lienzo_luz_1 = Canvas(self.ventMain, width=dimens_L1+5,
                                   height=dimens_L1+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_luz_1.place(x=90, y=80)
        self.luz_1 = self.lienzo_luz_1.create_oval(
            8, 8, dimens_L1, dimens_L1, width=6)
# luz 2
        dimens_L2 = 70  # dimension luz
        self.lienzo_luz_2 = Canvas(self.ventMain, width=dimens_L2+5,
                                   height=dimens_L2+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_luz_2.place(x=340, y=80)
        self.luz_2 = self.lienzo_luz_2.create_oval(
            8, 8, dimens_L2, dimens_L2, width=6)

# luz 2
        dimens_L3 = 70  # dimension luz
        self.lienzo_luz_3 = Canvas(self.ventMain, width=dimens_L3+5,
                                   height=dimens_L3+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_luz_3.place(x=340, y=330)
        self.luz_3 = self.lienzo_luz_3.create_oval(
            8, 8, dimens_L3, dimens_L3, width=6)
        
# Baliza
        dimens_Baliza = 70  # dimension luz
        self.lienzo_baliza = Canvas(self.ventMain, width=dimens_Baliza+5,
                                   height=dimens_Baliza+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_baliza.place(x=120, y=280)
        self.baliza = self.lienzo_baliza.create_oval(
            8, 8, dimens_Baliza, dimens_Baliza, width=6)

##### Luces Tablero ####         
# luz tablero 1
        L1_tablero = 70  # dimension luz
        self.lienzo_luz_tabero_1 = Canvas(self.ventMain, width=L1_tablero+5,
                                   height=L1_tablero+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_luz_tabero_1.place(x=570, y=340)
        self.luz_1_tablero = self.lienzo_luz_tabero_1.create_oval(
            8, 8, L1_tablero, L1_tablero, width=6)

# luz tablero 2
        L2_tablero = 70  # dimension luz
        self.lienzo_luz_tabero_2 = Canvas(self.ventMain, width=L2_tablero+5,
                                   height=L2_tablero+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_luz_tabero_2.place(x=665, y=340)
        self.luz_2_tablero = self.lienzo_luz_tabero_2.create_oval(
            8, 8, L2_tablero, L2_tablero, width=6)

# luz tablero 3
        L3_tablero = 70  # dimension luz
        self.lienzo_luz_tabero_3 = Canvas(self.ventMain, width=L3_tablero+5,
                                   height=L3_tablero+5, bg="lightgrey", highlightbackground="lightgrey")
        self.lienzo_luz_tabero_3.place(x=750, y=340)
        self.luz_3_tablero = self.lienzo_luz_tabero_3.create_oval(
            8, 8, L3_tablero, L3_tablero, width=6)             
        
        
# Botones     
    #boton 1
        self.boton_1 = Button(self.ventMain,text="Reconocer Alarma")
        self.boton_1.place(x=650,y=530)

        

        self.ventMain.after(100, self.Actualizar)


###################################### ACTUALIZAR ##############################

    def Actualizar(self):
        self.bits = self.PLC.leerCoil()

  # config luz 1
        if (self.bits[1]):
            colorL1 = "orange"
        else:
            colorL1 = "lightgreen"
        self.lienzo_luz_1.itemconfig(self.luz_1, fill=colorL1)

  # config luz 2
        if (self.bits[2]):
            colorL2 = "orange"
        else:
            colorL2 = "lightgreen"
        self.lienzo_luz_2.itemconfig(self.luz_2, fill=colorL2)
        
# config luz 3
        if (self.bits[3]):
            colorL3 = "orange"
        else:
            colorL3 = "lightgreen"
        self.lienzo_luz_3.itemconfig(self.luz_3, fill=colorL3)

# config luz tablero 1
        if (self.bits[1]):
            color_tablero_1 = "orange"
        else:
            color_tablero_1 = "lightgreen"
        self.lienzo_luz_tabero_1.itemconfig(self.luz_1_tablero, fill=color_tablero_1)

# config luz tablero 2
        if (self.bits[2]):
            color_tablero_2 = "orange"
        else:
            color_tablero_2 = "lightgreen"
        self.lienzo_luz_tabero_2.itemconfig(self.luz_2_tablero, fill=color_tablero_2)

# config luz tablero 3
        if (self.bits[3]):
            color_tablero_3 = "orange"
        else:
            color_tablero_3 = "lightgreen"
        self.lienzo_luz_tabero_3.itemconfig(self.luz_3_tablero, fill=color_tablero_3)

# config baliza
        if (self.bits[4]):
            color_baliza = "red"
        else:
            color_baliza = "lightgrey"
        self.lienzo_baliza.itemconfig(self.baliza, fill=color_baliza)


# accion botones
        
        self.boton_1.config(command =lambda: self.PLC.escribirCoil(0, 1))

# lectura analoga
        analog_1 = int("".join(map(str, self.PLC.leerAnalogo(0))))
        self.etiqueta_1.config(text=f"{round(analog_1/83.2)}°C")

        analog_2 = int("".join(map(str, self.PLC.leerAnalogo(1))))
        self.etiqueta_2.config(text=f"{round(analog_2/83.2)}°C")
        
        analog_3 = int("".join(map(str, self.PLC.leerAnalogo(2))))
        self.etiqueta_3.config(text=f"{round(analog_3/83.2)}°C")


# valor deslizador
# Sala 1
        self.PLC.escribir_analog(0, [self.sala_1.get()])
# Sala 2
        self.PLC.escribir_analog(1, [self.sala_2.get()])
# Sala 3
        self.PLC.escribir_analog(2, [self.sala_3.get()])







        self.ventMain.after(100, self.Actualizar)

def main(args):
    root = Tk()
    aplicacion = app(root)
    root.mainloop()
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
