from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from pathlib import Path
from tkinter import Tk, Canvas, PhotoImage
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\user\Desktop\UniConPro\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


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

logo_image = PhotoImage(
    file=relative_to_assets("image_Logo.png"))
image_2 = canvas.create_image(
    187.0,
    405.0,
    image=logo_image
)

progress_label = Label(window, text="Loading...", font=("AlegreyaSans Medium", 13, "bold"), fg="#FFFFFF", bg="#253334")
progress_label.place(x=131.0, y=670)

progress = ttk.Style()
progress.theme_use('clam')
progress.configure("red.Horizontal.TProgressbar", bg="#253334")
progress = Progressbar(window, orient=HORIZONTAL, length=200, mode='determinate', style="red.Horizontal.TProgressbar")
progress.place(x=85, y=700)


def top():
    window.withdraw()
    window.destroy()
    os.system('python WelcomeScreen.py')


i = 0


def load():
    global i
    if i <= 10:
        txt = 'Loading...' + (str(10 * i) + '%')
        progress_label.config(text=txt)
        progress_label.after(300, load)
        progress['value'] = 10 * i
        i += 1
    else:
        top()


load()
window.resizable(False, False)
window.mainloop()
