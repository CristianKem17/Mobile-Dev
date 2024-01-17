import sqlite3
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\UniConPro\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def insert_into_db(name, email, password):
   try:
       c.execute("INSERT INTO users VALUES (NULL, ?, ?, ?)", (name, email, password))
       conn.commit()
       window.destroy()
       os.system('python SignIn.py')
   except Exception as e:
       print(f"An error occurred: {e}")


def run_signin():
    window.destroy()
    os.system('python SignIn.py')


def toggle_password():
    if entry_3['show'] == '*':
        entry_3.config(show='')
        button_toggle.config(image=hide_image)
    else:
        entry_3.config(show='*')
        button_toggle.config(image=see_image)


window = Tk()

window.geometry("375x812")
window.configure(bg="#253334")

canvas = Canvas(
    window,
    bg="#253334",
    height=812,
    width=375,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

conn = sqlite3.connect('UserDataBase.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS users
            (id INTEGER PRIMARY KEY, name text, email text, password text)''')

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_name.png"))
entry_bg_1 = canvas.create_image(
    187.75,
    363.0,
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
    y=348.0,
    width=305.5,
    height=28.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_email.png"))
entry_bg_2 = canvas.create_image(
    187.75,
    435.0,
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
    y=420.0,
    width=305.5,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_password.png"))
entry_bg_3 = canvas.create_image(
    187.75,
    507.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#253334",
    fg="#FFFFFF",
    font=15,
    highlightthickness=0

)
entry_3.place(
    x=35.0,
    y=492.0,
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
    y=528.0,
    width=29.0,
    height=30.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_AAsignin.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_signin,
    relief="flat"
)
button_1.place(
    x=60.0,
    y=640.0,
    width=256.0,
    height=24.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_signup.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: insert_into_db(entry_1.get(), entry_2.get(), entry_3.get()),
    relief="flat"
)
button_2.place(
    x=27.0,
    y=565.0,
    width=321.0,
    height=61.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_leaves.png"))
image_1 = canvas.create_image(
    210.0000142818222,
    751.1423950195312,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_smallLogo.png"))
image_2 = canvas.create_image(
    61.0,
    116.0,
    image=image_image_2
)

canvas.create_text(
    41.0,
    472.0,
    anchor="nw",
    text="Password",
    fill="#BEC2C2",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    41.0,
    400.0,
    anchor="nw",
    text="Email Address",
    fill="#BEC2C2",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    39.0,
    328.0,
    anchor="nw",
    text="Name",
    fill="#BEC2C2",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    35.0,
    181.0,
    anchor="nw",
    text="Sign Up",
    fill="#FFFFFF",
    font=("Alegreya Medium", 30 * -1)
)

canvas.create_text(
    35.0,
    226.0,
    anchor="nw",
    text="Sign up now for free and start meditating,",
    fill="#FFFFFF",
    font=("AlegreyaSans Regular", 18 * -1)
)

canvas.create_text(
    35.0,
    252.0,
    anchor="nw",
    text="and explore Medic.",
    fill="#FFFFFF",
    font=("AlegreyaSans Regular", 18 * -1)
)

window.resizable(False, False)
window.mainloop()

conn.close()
