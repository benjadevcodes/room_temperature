import sys
from tkinter import *
from Comunication_basico import *
import time

class myFunc():
	def __init__(self,ventMain):
		"hola"


	def pulsador(self,text,digito,x,y):
		self.boton = Button(self.ventMain)
		self.boton.config(command= lambda num=digito: C_plc.botones(self,num),
		text=text,font=('Verdana',10,'bold'),borderwidth=6, relief="raised",)
		self.boton.place(x=x,y=y)
