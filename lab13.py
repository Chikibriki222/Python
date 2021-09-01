from tkinter import *    #плагин для интерфейса


class Menu:
    def __init__(self):
        self.but = Button(root)
        self.but["text"] = "Работать"
        self.but.bind("<Button-1>", self.printer)
        self.but.pack()

    def printer(self, event):
        print("я работаю")


root = Tk()
obj = Menu()
root.mainloop()
