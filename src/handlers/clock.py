from time import strftime
from tkinter import *
from tkinter.ttk import *

top =Tk()
top.title("Digital watch")
def none():
    time=strftime('%H:%M:%S:%p \n %a')
    if int(strftime('%H')) > 12:
        time =strftime('%H:%M:%S Hrs \n %a')
        lbl.config(text=time)
        lbl.after(1000,none)
    else:
        lbl.config(text=time)
        lbl.after(1000,none)
lbl=Label(top,font=('digital-7', 35, 'bold'),
          background='white',
          foreground='black',
          )
lbl.pack(anchor='center')
none()
mainloop()
