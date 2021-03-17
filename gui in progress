from tkinter import *
import time
from queuesimulation import Queue
q = Queue()

customers_list =[]
reciption = Tk()
reciption.title("Registration")

#backgroung image
bg = PhotoImage(file = "download.png")
label1 = Label( reciption, image = bg)
label1.place(x = 0, y = 0,relwidth=1, relheight=1)

#Clock
def clock():
  hour = time.strftime("%I")
  minute =time.strftime("%M")
  second =time.strftime("%S")
  am_pm = time.strftime("%p")
  lbl.config(text = hour +":" + minute +":"+second + " "+am_pm)
  lbl.after(1000,clock)
lbl = Label(reciption,text = "",font = ("Helvetica",48),fg = "red",bg = "black")
lbl.place(x=0, y=0)
clock()

#entry
def add_customer():
  name_var = customers_name.get()
  customers_list.append(name_var)
  t = 1
  q.num_in_q += 1
  name_entry.delete(0, END)

for_entry = Label(reciption, text="For entry")
for_entry.place(x=400, y=200)

customers_name = StringVar()
name_entry = Entry(reciption, textvariable=customers_name)
name_entry.place(x=400, y=220)

join = Button(text="JOIN", command=add_customer, bg="black", fg="white")
join.place(x=400, y=250)


reciption.mainloop()

