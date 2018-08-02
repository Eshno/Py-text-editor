class Archivo:
    def __init__():
        self.nombreArchivo = None
    
    def nuevoArchivo():
        self.nombreArchivo
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


