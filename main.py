from tkinter import *
from tkinter import filedialog
from texto import *
from color import *

nombreArchivo = None

def nuevoArchivo():
    global nombreArchivo
    nombreArchivo = "Sin Titulo"
    text.delete(0.0, END)
    
def abrirArchivo():
    f = filedialog.askopenfile(mode='r')
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
    f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Error", message= "No se pudo guardar el archivo")

def yo():
    print("Albert Vasquez")



#Instanciacion de Tk
root = Tk()
root.title("Editor de Texto Python")
#Tamaño de ventana
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)

text = Text(root, width = 400, height = 400)
text.pack()
text.insert(END, "Textazo man")
# text.tag_add('highlightline', 0.0,END)
# text.tag_configure('highlightline', background='yellow',justify="center", font='helvetica 14 bold', relief='raised')
# text.tag_remove('highlightline', 0.0,END)
# text.delete(0.0,END)

def justificar_izquierda():
    text.tag_delete('just-der')
    text.tag_delete('just-cent')

    text.tag_add('just-izq',0.0,END)
    text.tag_configure('just-izq', justify="left")

def justificar_derecha():
    text.tag_delete('just-cent')
    text.tag_delete('just-izq')

    text.tag_add('just-der',0.0,END)
    text.tag_configure('just-der', justify="right")

def justificar_centro():
    text.tag_delete('just-der')
    text.tag_delete('just-izq')

    text.tag_add('just-cent',0.0,END)
    text.tag_configure('just-cent', justify="center")

def negrita():
    text.tag_add('negrita',0.0,END)
    text.tag_configure('negrita', font='helvetica 12 bold')

def italic():
    text.tag_add('italic',0.0,END)
    # text.tag_configure('italic', font='helvetica 12 italics')

def underline():
    
    return
    

    
    

menubar = Menu(root) #Declaracion del menu

#Menu de Archivo
filemenu = Menu(menubar)
filemenu.add_command(label="Nuevo", command=nuevoArchivo)
filemenu.add_command(label="Abrir", command=abrirArchivo)
filemenu.add_command(label="Guardar", accelerator="Ctrl+G",command=guardarArchivo)
filemenu.add_command(label="Guardar Como", command=guardarComo)
filemenu.add_separator()
filemenu.add_command(label="Salir", accelerator="Alt+F4",command=root.quit)
menubar.add_cascade(label = "Archivo", menu=filemenu)

#Menu de Edicion
edicionmenu = Menu(menubar)
edicionmenu.add_command(label="Deshacer", accelerator="Ctrl+Z", command = lambda: root.focus_get().event_generate('<<Undo>>'))
edicionmenu.add_command(label="Rehacer", accelerator="Ctrl+Y", command = lambda: root.focus_get().event_generate('<<Redo>>'))
edicionmenu.add_separator()
edicionmenu.add_command(label="Copiar", accelerator="Ctrl+C", command = lambda: root.focus_get().event_generate('<<Copy>>'))
edicionmenu.add_command(label="Cortar",  accelerator="Ctrl+X", command = lambda: root.focus_get().event_generate('<<Cut>>'))
edicionmenu.add_command(label="Pegar", accelerator="Ctrl+V", command = lambda: root.focus_get().event_generate('<<Paste>>'))
edicionmenu.add_command(label="Seleccionar Todo", accelerator="Ctrl+A", command = lambda: root.focus_get().event_generate('<<SelectAll>>'))
menubar.add_cascade(label = "Edicion", menu=edicionmenu)

#Menu de Fuente
menufuente = Menu(menubar)
menufuente.add_command(label="Negrita", accelerator="Ctrl+N" ,command=negrita)
menufuente.add_command(label="Cursiva",accelerator="Ctrl+B" ,command=None)
menufuente.add_command(label="Subrayado",accelerator="Ctrl+S" ,command=None)
menufuente.add_separator()
menufuente.add_command(label="Color", command=None)
menufuente.add_command(label="Fuente", command=None)
menufuente.add_command(label="Tamaño", command=None)
menubar.add_cascade(label = "Fuente", menu=menufuente)

#Menu de Parrafo
menuparrafo = Menu(menubar)

menuparrafo.add_command(label="Alinear Centro", command=justificar_centro)
menuparrafo.add_command(label="Alinear Derecha", command=justificar_derecha)
menuparrafo.add_command(label="Alinear Izquierda", command=justificar_izquierda)
menubar.add_cascade(label = "Parrafo", menu=menuparrafo)


acerca = Menu(menubar)
acerca.add_command(label="Albert", command=yo)
menubar.add_cascade(label = "Acerca", menu=acerca)


root.config(menu=menubar)
root.mainloop()
