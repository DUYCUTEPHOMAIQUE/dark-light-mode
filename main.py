from tkinter import *
from tkinter import ttk

tit = "Dark and Light mod"
Bg = '#000000'
Fg = '#ffffff'


class Win():
    def __init__(self, root):
        self.root = root
        self.root.title(tit)
        self.root.geometry('500x500')
        self.root.resizable(0, 0)
        self.root.config(bg=Fg)

        self.lab = Label(self.root, text=tit, font='Arial 20 bold', bg=Bg, fg=Fg, pady=20)
        self.lab.place(x=0, y=0, relwidth=1)

        self.var = StringVar()
        self.como = ttk.Combobox(self.root, font='Arial 20 bold', state='readonly', textvariable=self.var)
        self.como['values'] = ('dark', 'light')
        self.como.current(1)
        self.como.place(x=0, y=100, width=100)
        self.como.bind('<<ComboboxSelected>>', self.The)

    def The(self, event=None):
        self.The = self.var.get()

        if self.The == 'dark':
            self.root.config(bg=Bg)
            # self.lab.config(bg='#ffffff', fg='#000000')
            self.lab.config(bg='#000000', fg='#ffffff')

        elif self.The == 'light':
            self.root.config(bg=Fg)
            # self.lab.config(bg='#000000', fg='#ffffff')
            self.lab.config(bg='#ffffff', fg='#000000')


root = Tk()
App = Win(root)
root.mainloop()
