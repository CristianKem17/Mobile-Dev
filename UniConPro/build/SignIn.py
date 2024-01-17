import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\UniConPro\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def run_signup():
    window.destroy()
    os.system('python SignUp.py')

def toggle_password():
  if entry_1['show'] == '*':
      entry_1.config(show='')
      button_toggle.config(image=hide_image)
  else:
      entry_1.config(show='*')
      button_toggle.config(image=see_image)

def run_login():
 email = entry_2.get()
 password = entry_1.get()

 # Connect to the SQLite database
 conn = sqlite3.connect('UserDataBase.db')
 cursor = conn.cursor()

 # Define the SQL query to fetch user data
 query = f"SELECT * FROM Users WHERE email = '{email}' AND password = '{password}';"

 # Execute the SQL query
 cursor.execute(query)

 # Fetch all the rows returned by the query
 result = cursor.fetchall()

 # Check if the result is empty
 if result:
     print("Login successful!")
 else:
     print("Invalid username or password.")

 # Close the database connection
 conn.close()


window = Tk()

window.geometry("375x812")
window.configure(bg = "#253334")

canvas = Canvas(
    window,
    bg = "#253334",
    height = 812,
    width = 375,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_login.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_login,
    relief="flat"
)
button_1.place(
    x=27.0,
    y=521.0,
    width=321.0,
    height=61.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_password.png"))
entry_bg_1 = canvas.create_image(
    187.75,
    452.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#253334",
    fg="#FFFFFF",
    font=15,
    highlightthickness=0
)
entry_1.place(
    x=35.0,
    y=437.0,
    width=305.5,
    height=28.0
)

see_image = PhotoImage(file=relative_to_assets("button_see.png"))
hide_image = PhotoImage(file=relative_to_assets("button_hide.png"))

button_toggle = Button(
    image=hide_image,
    borderwidth=0,
    highlightthickness=0,
    command=toggle_password,
    relief="flat"
)

button_toggle.place(
   x=35.0,
   y=484.0,
   width=29.0,
   height=30.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_email.png"))
entry_bg_2 = canvas.create_image(
    187.75,
    380.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#253334",
    fg="#FFFFFF",
    font=15,
    highlightthickness=0
)
entry_2.place(
    x=35.0,
    y=365.0,
    width=305.5,
    height=28.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_NAsignup2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_signup,
    relief="flat"
)
button_2.place(
    x=66.0,
    y=598.0,
    width=243.0,
    height=26.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_leaves.png"))
image_1 = canvas.create_image(
    210.00000097696687,
    748.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_smallLogo.png"))
image_2 = canvas.create_image(
    61.0,
    120.0,
    image=image_image_2
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_ForgotPass.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=247.0,
    y=484.0,
    width=94.0,
    height=17.0
)

canvas.create_text(
    45.0,
    405.0,
    anchor="nw",
    text="Password",
    fill="#BEC2C2",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    45.0,
    333.0,
    anchor="nw",
    text="Email Address",
    fill="#BEC2C2",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    35.0,
    226.0,
    anchor="nw",
    text="Sign in now to access your conversions.",
    fill="#FFFFFF",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    35.0,
    181.0,
    anchor="nw",
    text="Sign In",
    fill="#FFFFFF",
    font=("Alegreya Medium", 30 * -1)
)
window.resizable(False, False)
window.mainloop()


