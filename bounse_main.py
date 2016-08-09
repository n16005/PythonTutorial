from tkinter import *

tk = TK()
tk.title("GAME")
tk.resisable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400,bd=0, highlightthicness=0)
canvas.pack()
tk.update()

tk.mainloop()