from tkinter import *
from tkinter import filedialog
from texto import *

class App:
    nombreArchivo = None
    def __init__(self):
        self.root = Tk()
        self.root.title("Editor de Texto Python")
        self.root.minsize(width=400,height=400)
        self.root.maxsize(width=400,height=400)

        self.text = Texto(self.root)
        self.menubar = Menu(self.root)         
        App.generarMenu(self.menubar,self.root, self.text)   

        

        self.root.config(menu=self.menubar)
        self.root.mainloop()

    @classmethod
    def nuevoArchivo(cls, text):        
        cls.nombreArchivo = "Sin Titulo"
        text.delete(0.0, END)
    @classmethod
    def abrirArchivo(cls, text):
        f = filedialog.askopenfile(mode='r')
        t = f.read()
        text.delete(0.0,END)
        text.insert(0.0, t) 
    @classmethod
    def guardarArchivo(cls, text):        
        t = text.get(0.0, END)
        f = open(cls.nombreArchivo, 'w')
        f.write(t)
        f.close()
    @classmethod
    def guardarComo(cls, text):
        f = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
        t = text.get(0.0, END)
        try:
            f.write(t.rstrip())
        except:
            showerror(title="Error", message= "No se pudo guardar el archivo")
    
    def generarMenu(menubar,root,text):
        filemenu = Menu(menubar)
        edicionmenu = Menu(menubar)
        menufuente = Menu(menubar)
        menuparrafo = Menu(menubar)

        #Menu de Archivo
        filemenu.add_command(label="Nuevo", command=App.nuevoArchivo(text))
        filemenu.add_command(label="Abrir", command=App.abrirArchivo(text))
        filemenu.add_command(label="Guardar", accelerator="Ctrl+G",command=App.guardarArchivo(text))
        filemenu.add_command(label="Guardar Como", command=App.guardarComo(text))
        filemenu.add_separator()
        filemenu.add_command(label="Salir", accelerator="Alt+F4",command=root.quit)
        
        #Menu de Edicion
        edicionmenu.add_command(label="Deshacer", accelerator="Ctrl+Z", command = lambda: root.focus_get().event_generate('<<Undo>>'))
        edicionmenu.add_command(label="Rehacer", accelerator="Ctrl+Y", command = lambda: root.focus_get().event_generate('<<Redo>>'))
        edicionmenu.add_separator()
        edicionmenu.add_command(label="Copiar", accelerator="Ctrl+C", command = lambda: root.focus_get().event_generate('<<Copy>>'))
        edicionmenu.add_command(label="Cortar",  accelerator="Ctrl+X", command = lambda: root.focus_get().event_generate('<<Cut>>'))
        edicionmenu.add_command(label="Pegar", accelerator="Ctrl+V", command = lambda: root.focus_get().event_generate('<<Paste>>'))
        edicionmenu.add_command(label="Seleccionar Todo", accelerator="Ctrl+A", command = lambda: root.focus_get().event_generate('<<SelectAll>>'))
        
        #Menu de fuente
        menufuente.add_command(label="Negrita", accelerator="Ctrl+N" ,command=text.negrita)
        menufuente.add_command(label="Cursiva",accelerator="Ctrl+B" ,command=None)
        menufuente.add_command(label="Subrayado",accelerator="Ctrl+S" ,command=None)
        menufuente.add_separator()
        menufuente.add_command(label="Color", command=None)
        menufuente.add_command(label="Fuente", command=None)
        menufuente.add_command(label="Tamaño", command=None)

        # #Menu de parrafo
        menuparrafo.add_command(label="Alinear Centro", command=text.justificar_centro)
        menuparrafo.add_command(label="Alinear Derecha", command=text.justificar_derecha)
        menuparrafo.add_command(label="Alinear Izquierda", command=text.justificar_izquierda)
        


        #Agregar los menus al menubar
        menubar.add_cascade(label = "Archivo", menu=filemenu)
        menubar.add_cascade(label = "Edicion", menu=edicionmenu)
        menubar.add_cascade(label = "Fuente", menu=menufuente)
        menubar.add_cascade(label = "Parrafo", menu=menuparrafo)
        


#Menu de Archivo

asd = App()



    

