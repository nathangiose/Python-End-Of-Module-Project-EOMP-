# Codes to be running for Lotto_GUI.py


from tkinter import *
from tkinter import messagebox
from datetime import datetime, timedelta
import rsaidnumber


class Authentication:

    def __init__(self, master):
    name_lbl = self.name_lbl
    name_entry = self.name_entry
    address_lbl = self.address_lbl
    identity_lbl = self.identity_lbl


from datetime import datetime

id_no = input('please enter your id number: ')

birth_year = int(id_no[0:2])
birthdate = int(id_no[2:4])
birth_month = int(id_no[4:6])
current_date = datetime.today()

year = birth_year.strftime("%y")
user_age = datetime(birth_year, birthdate, birth_month)
age = current_date - user_age


print(user_age)

