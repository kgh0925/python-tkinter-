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
  global mcount
  if mcount > 0 :
    mcount -= 1
    label2.config(text = str(mcount) + "m")
  else :
    pass


button1 = tkinter.Button(window, text = "Up / h", width=5, height=1,command =hup)

button2 = tkinter.Button(window, text = "down / h", width=5, height=1,command =hdown)

button3 = tkinter.Button(window, text = "Up / m", width=5, height=1,command =mup)

button4 = tkinter.Button(window, text = "down / m", width=5, height=1, command =mdown)



label1 = tkinter.Label(window, text = "00 h")
label2 = tkinter.Label(window, text = "00 m")

label1.place(x = 160, y = 190)
label2.place(x = 200, y = 190)


button1.place(x = 20 , y = 30)
button2.place(x = 20, y = 340)
button3.place(x = 300 , y = 30)
button4.place(x = 300, y = 340)

window.mainloop()