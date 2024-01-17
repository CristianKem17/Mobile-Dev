from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\UniConPro\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def run_signup():
    window.destroy()
    os.system('python SignUp.py')


def run_signin():
    window.destroy()
    os.system('python SignIn.py')


window = Tk()

window.geometry("375x812")
window.configure(bg="#FFFFFF")

canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=812,
    width=375,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
bg_image = PhotoImage(
    file=relative_to_assets("image_1B.png"))
image_1 = canvas.create_image(
    599.0,
    300.0,
    image=bg_image
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_signin.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=run_signin,
    relief="flat"
)
button_1.place(
    x=27.0,
    y=624.0,
    width=321.0,
    height=61.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_NAsignup.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=run_signup,
    relief="flat"
)
button_2.place(
    x=68.0,
    y=703.0,
    width=240.0,
    height=18.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_Logo.png"))
image_2 = canvas.create_image(
    201.0,
    286.0,
    image=image_image_2
)

canvas.create_text(
    33.0,
    457.0,
    anchor="nw",
    text="Make your student’s life easier in one click.",
    fill="#FFFFFF",
    font=("AlegreyaSans Medium", 17 * -1)
)

canvas.create_text(
    95.0,
    480.0,
    anchor="nw",
    text="Think positive, think converter.",
    fill="#FFFFFF",
    font=("AlegreyaSans Medium", 15 * -1)
)

canvas.create_text(
    87.0,
    411.0,
    anchor="nw",
    text="CONVERTIFY",
    fill="#FFFFFF",
    font=("Alegreya Bold", 34 * -1)
)
window.resizable(False, False)
window.mainloop()
