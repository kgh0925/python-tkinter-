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