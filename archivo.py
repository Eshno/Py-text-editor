from tkinter import *
from tkinter import filedialog


class Archivo:
    # nombreArchivo = None
    def __init__(self):
        self.nombreArchivo = None
    
    def nuevoArchivo(self):        
        self.nombreArchivo = "Sin Titulo"
        text.delete(0.0, END)
    
    def abrirArchivo(self):
        f = askopenfile(mode='r')
        t = f.read()
        text.delete(0.0,END)
        text.insert(0.0, t) 
    
    def guardarArchivo(self):        
        t = text.get(0.0, END)
        f = open(self.nombreArchivo, 'w')
        f.write(t)
        f.close()
    
    def guardarComo(self):
        f = asksaveasfile(mode='w', defaultextension='.txt')
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Error", message= "No se pudo guardar el archivo")


