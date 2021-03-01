from tkinter import *
def info():
    name_info=name.get()
    lb=Label(text=name_info).pack()
    
screen=Tk()
screen.title("IIITB RESTAURANT")
head=Label(text="NAME")
head.place(x=10,y=20)

name=StringVar()

name_entry=Entry(textvariable=name)

name_entry.place(x=10,y=50)

join=Button(text="JOIN",command=info,bg="black",fg="white"
join.place(x=10,y=90)
screen.mainloop()