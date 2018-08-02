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