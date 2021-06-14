# Nathan John Giose

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x500")
root.title("LOTTERY GAME")
root.config(bg='#069edb')
root.resizable(0, 0)

# INSERT IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(root, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# Label Frame
spin_boardA = LabelFrame(root, text="Board A", bg='#069edb')
spin_boardA.pack(fill="both")
spin_boardB = LabelFrame(root, text="Board B", bg='#069edb')
spin_boardB.pack(fill="both")






# Spinbox


current_value = StringVar(value=0)
spin_box = Spinbox(spin_boardA, from_=1, to=49, textvariable=current_value, wrap=True, width=2)
spin_box.place(x=20)
''''
current_value = StringVar(value=0)
spin_box1 = Spinbox(spin_boardA, from_=1, to=49, textvariable=current_value, wrap=True, width=2)
'''


spin_box.pack()
root.mainloop()
