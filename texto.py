from tkinter import *
from tkinter import filedialog

class Texto:  
    def __init__(self, root):
        self.text = Text(root, width = 400, height = 400)
        self.text.pack()
        self.text.insert(END, "Textazo man")

    def justificar_izquierda(self):
        self.text.tag_delete('just-der')
        self.text.tag_delete('just-cent')

        self.text.tag_add('just-izq',0.0,END)
        self.text.tag_configure('just-izq', justify="left")

    def justificar_derecha(self):
        self.text.tag_delete('just-cent')
        self.text.tag_delete('just-izq')

        self.text.tag_add('just-der',0.0,END)
        self.text.tag_configure('just-der', justify="right")

    def justificar_centro(self):
        self.text.tag_delete('just-der')
        self.text.tag_delete('just-izq')

        self.text.tag_add('just-cent',0.0,END)
        self.text.tag_configure('just-cent', justify="center")

    def negrita(self):
        self.text.tag_add('negrita',0.0,END)
        self.text.tag_configure('negrita', font='helvetica 12 bold')
    
    def nuevoArchivo(self):        
        App.nombreArchivo = "Sin Titulo"
        self.text.delete(0.0, END)
    
    def abrirArchivo(self):
        f = filedialog.askopenfile(mode='r')
        t = f.read()
        self.text.delete(0.0,END)
        self.text.insert(0.0, t) 
    
    def guardarArchivo(self):        
        t = text.get(0.0, END)
        f = open(App.nombreArchivo, 'w')
        f.write(t)
        f.close()
    
    def guardarComo(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        t = self.text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Error", message= "No se pudo guardar el archivo")