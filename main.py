from tkinter import *
from tkinter import ttk
from ttkthemes import ThemedTk

class Player:

    def __init__(self):
        
        #JANELA
        self.window = ThemedTk(theme="equilux")
        self.window.title("Music Player")
        self.window.resizable(0, 0)
        self.window.geometry("300x410+500+100")
        self.window.config(bg="#444444")

        self.img_add = PhotoImage(file="assets/add.png")
        self.img_next = PhotoImage(file="assets/next.png")
        self.img_pause = PhotoImage(file="assets/pause.png")
        self.img_play = PhotoImage(file="assets/play.png")
        self.img_previus = PhotoImage(file="assets/previus.png")
        self.img_remove = PhotoImage(file="assets/remove.png")

        self.list = Listbox(self.window, bg="#333333", height=14)
        self.list.pack(fill=X, padx=10, pady=10)

        self.frame = ttk.Frame(self.window)
        self.frame.pack(pady=10)
        
        self.add = ttk.Button(self.frame, image=self.img_add)
        self.add.grid(row=0, column=0, padx=2)

        self.remove = ttk.Button(self.frame, image=self.img_remove)
        self.remove.grid(row=0, column=1, padx=2)

        self.frame2 = ttk.Frame(self.window)
        self.frame2.pack(pady=10)

        self.previus = ttk.Button(self.frame2, image=self.img_previus)
        self.previus.grid(row=0, column=0)

        self.play = ttk.Button(self.frame2, image=self.img_play)
        self.play.grid(row=0, column=1)

        self.next = ttk.Button(self.frame2, image=self.img_next)
        self.next.grid(row=0, column=2)

        self.volume = ttk.Scale(self.window)
        self.volume.pack(fill=X, padx=10)


        self.window.mainloop()

Player()