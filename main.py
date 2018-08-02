from Tkinter import *
from tkFileDialog import *

nombreArchivo = None

def nuevoArchivo():
    global nombreArchivo
    nombreArchivo = "Sin Titulo"
    text.delete(0.0, END)

    
def abrirArchivo():
    f = askopenfile(mode='r')
    t = f.read()
    text.delete(0.0,END)
    text.insert(0.0, t)

def guardarArchivo():
    global nombreArchivo
    t = text.get(0.0, END)
    f = open(nombreArchivo, 'w')
    f.write(t)
    f.close()

def guardarComo():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error", message= "No se pudo guardar el archivo")

#Instanciacion de Tk
root = Tk()
root.title("Editor Python")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

text = Text(root, width = 400, height = 400)
text.pack()
menubar = ""
menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Nuevo", command=nuevoArchivo)
filemenu.add_command(label="Abrir", command=abrirArchivo)
filemenu.add_command(label="Guardar", command=guardarArchivo)
filemenu.add_command(label="Guardar Como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir", command=root.quit)
menubar.add_cascade(label = "Archivo", menu=filemenu)

root.config(menu=menubar)
root.mainloop()
