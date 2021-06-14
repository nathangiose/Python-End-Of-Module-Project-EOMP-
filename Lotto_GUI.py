# Nathan John Giose
# I will import everything from tkinter


from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("LOTTERY GAME")
window.config(bg='#069edb')
window.resizable(0, 0)

# INSERT IMAGE


img = PhotoImage(file="powerball.png")
canvas = Canvas(window, width=391, height=129)
canvas.create_image(0, 0, anchor=NW, image=img)
canvas.pack()

# Inserting the labels and entry boxes


name_lbl = Label(window, text="Please enter your name", font=('Arial', 12))
name_lbl.place(x=53, y=150)
name_entry = Entry(window)
name_entry.place(x=280, y=150)

email_lbl = Label(window, text="Please enter your email", font=('Arial', 12))
email_lbl.place(x=53, y=200)
email_entry = Entry(window)
email_entry.place(x=280, y=200)

identity_lbl = Label(window, text="Please enter your ID number", font=('Arial', 12))
identity_lbl.place(x=53, y=250)
identity_entry = Entry(window)
identity_entry.place(x=280, y=250)

confirm_btn = Button(window, text="Confirm")
confirm_btn.place(x=215, y=300)

window.mainloop()
