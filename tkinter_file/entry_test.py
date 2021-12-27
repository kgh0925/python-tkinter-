import tkinter
i = 1
a = 20
b = 110
def gugu():
  c = int(entry.get())
  i = 1
  a = 20
  b = 120
  for i in range ( i < 9) :
    d = (int(entry.get()) * (i + 1))
    e = (str(c) + " x " + str(i + 1) + " =  " + str(d))
    label=tkinter.Label(win, text=e , width=10, height=1, fg="red", relief="flat")
    label.place(x = a, y = b)
    b += 30

    

win=tkinter.Tk()
win.title("gugudan")
win.geometry("600x400")

label=tkinter.Label(win, text="gugudan",font=("", 20))
label.place(x=20,y=10)


entry=tkinter.Entry(width=50)
entry.place(x=20, y=50)

button=tkinter.Button(text="result", command=gugu)
button.place(x=20, y=80)

win.mainloop()