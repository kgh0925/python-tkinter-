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