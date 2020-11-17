import tkinter as tk
from time import strftime as time

rel = tk.Label(text=time("%H:%M:%S"), font="Arial 50 bold")
rel.pack()


def clock():
    now = time("%H:%M:%S")
    if rel["text"] != now:
        rel["text"] = now
    rel.after(100, clock)


clock()
rel.mainloop()
