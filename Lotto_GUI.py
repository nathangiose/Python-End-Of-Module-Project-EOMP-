# Nathan John Giose
# I will import everything from tkinter


from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import rsaidnumber

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
class Authentication:

    def __init__(self):
        name_lbl = Label(window, text="Please enter your name", font=('Arial', 12))
        name_lbl.place(x=53, y=150)
        name_entry = Entry(window)
        name_entry.place(x=280, y=150)

        email_lbl = Label(window, text="Please enter your email", font=('Arial', 12))
        email_lbl.place(x=53, y=200)
        email_entry = Entry(window)
        email_entry.place(x=280, y=200)

        address_lbl = Label(window, text="Please enter your address", font=('Arial', 12))
        address_lbl.place(x=53, y=250)
        address_entry = Entry(window)
        address_entry.place(x=280, y=250)

        identity_lbl = Label(window, text="Please enter your ID number", font=('Arial', 12))
        identity_lbl.place(x=53, y=300)
        identity_entry = Entry(window)
        identity_entry.place(x=280, y=300)

    def identity(self):
        id_number = rsaidnumber.parse(self.id_no_entry.get())
        age = str((datetime.today() - id_number.date_of_birth) // timedelta(days=365))
        try:
            if int(age) >= 18:
                messagebox.showinfo("Congratulations!", "You qualify to play")
            elif int(age) < 18:
                ages = str(int(age) - 18)
                messagebox.showerror("Error", "You're not of age to Gamble")
        except ValueError:
            messagebox.showerror("Error", "Enter a Valid ID number")



confirm_btn = Button(window, text="Confirm", command=Authentication)
confirm_btn.place(x=215, y=350)
Authentication()
window.mainloop()
