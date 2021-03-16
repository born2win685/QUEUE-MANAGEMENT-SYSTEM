from tkinter import *
l=[]
def info():
    name_info=name.get()
    l.append(name_info)   #list to store the inputs
    name_entry.delete(0,END)
screen=Tk()
screen.title("IIITB BANK")
head=Label(text="NAME")
head.place(x=10,y=20)

name=StringVar()

name_entry=Entry(textvariable=name)

name_entry.place(x=10,y=50)

join=Button(text="JOIN",command=info,bg="black",fg="white")
join.place(x=10,y=90)
screen.mainloop()
