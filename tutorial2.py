from tkinter import *


window =Tk()
window.title("Uppercase-Lowercase")

frame=Frame(window)

entry=Entry(frame)

def upperc():
    upp=entry.get()
    entry.delete(0,END)
    entry.insert(0,upp.upper())

def lowerc():
    low=entry.get()
    entry.delete(0,END)
    entry.insert(0,low.lower())


    


but1=Button(frame,text="UPPERCASE" ,command=upperc)
but2=Button(frame,text="lowercase",command=lowerc)

but1.pack(side="top")
entry.pack(side="top")
but2.pack(side="bottom")
frame.pack()








window.mainloop()
