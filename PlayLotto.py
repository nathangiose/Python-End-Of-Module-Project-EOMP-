# Nathan John Giose- Group2

from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("LOTTERY GAME")
root.config(bg='#069edb')
root.resizable(0, 0)

# INSERT IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(root, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.place(x=55, y=0)

# Label Frame Board A

Powerball = LabelFrame(root, text="Board A", bg='#069edb', bd=4, width=391)
Powerball.place(x=55, y=150)
btn1 = Button(Powerball, textvariable='', width=1, text="1")
btn1.place(x=10, y=10)

'''
btn2 = Button(Powerball, textvariable='', width=1, text="2")
btn2.pack(side=LEFT)
btn3 = Button(Powerball, textvariable='', width=1, text="3")
btn3.pack(side=LEFT)
btn4 = Button(Powerball, textvariable='', width=1, text="4")
btn4.pack(side=LEFT)
btn5 = Button(Powerball, textvariable='', width=1, text="5")
btn5.pack(side=LEFT)
btn6 = Button(Powerball, textvariable='', width=1, text="6")
btn6.pack(side=LEFT)
btn7 = Button(Powerball, textvariable='', width=1, text="7")
btn7.pack(side=LEFT)
btn8 = Button(Powerball, textvariable='', width=1, text="8")
btn8.pack(side=LEFT)
btn9 = Button(Powerball, textvariable='', width=1, text="9")
btn9.pack(side=LEFT)
btn10 = Button(Powerball, textvariable='', width=1, text="10")
btn10.pack(side=LEFT)
btn1 = Button(Powerball, textvariable='', width=1, text="1")
btn1.pack(side=LEFT)
btn2 = Button(Powerball, textvariable='', width=1, text="2")
btn2.pack(side=LEFT)
btn3 = Button(Powerball, textvariable='', width=1, text="3")
btn3.pack(side=LEFT)
btn4 = Button(Powerball, textvariable='', width=1, text="4")
btn4.pack(side=LEFT)
btn5 = Button(Powerball, textvariable='', width=1, text="5")
btn5.pack(side=LEFT)
btn6 = Button(Powerball, textvariable='', width=1, text="6")
btn6.pack(side=LEFT)
btn7 = Button(Powerball, textvariable='', width=1, text="7")
btn7.pack(side=LEFT)
btn8 = Button(Powerball, textvariable='', width=1, text="8")
btn8.pack(side=LEFT)
btn9 = Button(Powerball, textvariable='', width=1, text="9")
btn9.pack(side=LEFT)
btn10 = Button(Powerball, textvariable='', width=1, text="10")
btn10.pack(side=LEFT)
'''



root.mainloop()
