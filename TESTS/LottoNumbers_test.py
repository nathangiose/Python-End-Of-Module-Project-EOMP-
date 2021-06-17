# Nathan John Giose- Group2

from tkinter import *
import random

root = Tk()
root.geometry("500x500")
root.title("LOTTERY GAME")
root.config(bg='#069edb')
root.resizable(0, 0)

# INSERT IMAGE

class lottery:
    mylotto = []
    for x in range(6):
        x = random.randint(1, 49)
        mylotto.append(x)
        mylotto.sort()
    print("Your lotto numbers are as follows: ")
    print(mylotto)

lbl1 = Label(root, text="Test Loop")
lbl1.pack()
lbl1entry = Entry(root, text='', textvariable=lbl1)
lbl1entry.pack()
lbl1btn = Button(root, text="Execute", command=lottery)
lbl1btn.pack()

root.mainloop()







