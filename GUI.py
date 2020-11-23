import tkinter as tk
from src.leboncoinbot.leboncoinbot import LeboncoinBot
root= tk.Tk()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def GUI ():  
    LeboncoinBot()
    
button1 = tk.Button(text='Run',command=hello, bg='brown',fg='white')
canvas1.create_window(150, 150, window=button1)

root.mainloop()