class Texto:
    def __init__(self):
        self.texto
    
    def justificar_izquierda():
        self.text.tag_add('just-izq',0.0,END)
        self.text.tag_configure('just-izq', justify="left")

    def justificar_derecha():
        self.text.tag_add('just-der',0.0,END)
        self.text.tag_configure('just-der', justify="right")

    def justificar_centro():
        self.text.tag_add('just-cent',0.0,END)
        self.text.tag_configure('just-cent', justify="center")

    def negrita():
        self.text.tag_add('negrita',0.0,END)
        self.text.tag_configure('negrita', font='helvetica 12 bold')