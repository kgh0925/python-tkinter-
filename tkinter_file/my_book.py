"""
[~1day]

import tkinter

window=tkinter.Tk()
window.title("Kim Geun Ho")
window.geometry("400x400+100+100")
window.resizable(False, False)

hcount = 0
mcount = 0
def hup():
  global hcount
  if hcount < 24 :
    hcount += 1
    label1.config(text = str(hcount) + "h")
  else :
    pass

def mup():
  global hcount
  global mcount
  if mcount < 59 :
    mcount += 1
    label2.config(text = str(mcount) + "m")
  elif mcount == 59 and hcount != 24 :
    hcount +=1
    mcount = 0
    label1.config(text = str(hcount) + "h")
    label2.config(text = str(mcount) + "m")
  else :
    pass

def hdown():
  global hcount
  if hcount > 0 :
    hcount -= 1
    label1.config(text = str(hcount) + "h")
  else :
    pass

def mdown():
  global hcount
  global mcount
  if mcount > 0 :
    mcount -= 1
    label2.config(text = str(mcount) + "m")
  elif mcount == 0 and hcount != 0 :
    hcount -= 1
    mcount = 59
    label1.config(text = str(hcount) + "h")
    label2.config(text = str(mcount) + "m")
  
  else :
    pass

    

def m10u():
  global hcount
  global mcount
  if mcount < 49 :
    mcount += 10
    label2.config(text = str(mcount) + "m")
  elif mcount >= 50 and hcount != 24 :
    hcount +=1
    mcount = mcount - 50
    label1.config(text = str(hcount) + "h")
    label2.config(text = str(mcount) + "m")
  else :
    pass

def m10d ():
  global hcount
  global mcount
  if mcount > 9 :
    mcount -= 10
    label2.config(text = str(mcount) + "m")
  elif hcount != 0 and mcount <= 9  :
    hcount -= 1
    mcount += 50
    label1.config(text = str(hcount) + "h")
    label2.config(text = str(mcount) + "m")
  else :
    pass


button1 = tkinter.Button(window, text = "Up / h", width=8, height=1,command =hup)

button2 = tkinter.Button(window, text = "Down / h", width=8, height=1,command =hdown)

button3 = tkinter.Button(window, text = "Up / m", width=8, height=1,command =mup)

button4 = tkinter.Button(window, text = "Down / m", width=8, height=1, command =mdown)

b5 = tkinter.Button(window, text = "Up / 10m", width = 8, height = 1, command = m10u)

b6 = tkinter.Button(window, text = "Down / 10m", width = 8, height = 1, command = m10d)

label1 = tkinter.Label(window, text = "00 h")
label2 = tkinter.Label(window, text = "00 m")

label1.place(x = 160, y = 190)
label2.place(x = 200, y = 190)


button1.place(x = 20 , y = 30)
button3.place(x = 20, y = 340)
button2.place(x = 300 , y = 30)
button4.place(x = 300, y = 340)
b5.place(x = 20, y = 190)
b6.place(x = 300, y = 190)

window.mainloop()

[day2]

from tkinter import *

window = Tk()
window.title("Kim Geun Ho")
window.geometry("400x400+100+100")
rad = IntVar()
rad1 = Radiobutton(window, text ="chioce1", variable = rad, value = 1)
rad2 = Radiobutton(window, text ="chioce2", variable = rad, value = 2)
rad3 = Radiobutton(window, text ="chioce3", variable = rad, value = 3)
rad1.place(x = 50,y = 10)
rad2.place(x = 50,y = 30)
rad3.place(x = 50,y = 50)

chk = IntVar()
chkb1 = Checkbutton(window, text = "checkbox", variable = chk)
chkb1.place(x = 150, y=10)

listbox = Listbox(window, selectmode = 'extended', height = 0)
# selctmod => extended, single
listbox.insert(0, "Dog")
listbox.insert(1, "Snake")
listbox.insert(2, "Tiger")
listbox.insert(3, "Cat")
listbox.insert(4, "Rabbit")
listbox.place(x = 150, y = 50)
window.mainloop()

[day3]
from tkinter import *


def process():
    temperature = float(e1.get())
    mytemp = (temperature - 32) * 5 / 9
    e2.insert(0, str(mytemp))


def pro():
    temperature = float(e2.get())
    mytemp = (temperature * 1.8) + 32
    e1.insert(0, str(mytemp))

    
window = Tk()


l1 = Label(window, text = "℉", font = "helvetica 16 italic")     
l2 = Label(window, text = "℃", font = "helvetica 16 italic")
l1.grid(row = 0, column = 0)
l2.grid(row = 1, column = 0)

e1 = Entry(window, bg = "yellow", fg = "green")     
e2 = Entry(window, bg = "yellow", fg = "green")
e1.grid(row = 0, column = 1)
e2.grid(row = 1, column = 1)

b1 = Button(window, text = "℉->℃", command = process)
b2 = Button(window, text = "℃->℉", command = pro)
b1.grid(row = 2, column = 0)
b2.grid(row = 2, column = 1)


window.mainloop()

"""