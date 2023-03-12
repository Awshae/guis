from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/asherjarvis/Desktop/build/assets/sphere_asset")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("3DSCAPE")

window.geometry("1080x720")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 720,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    540.0,
    360.0,
    image=image_image_1
)

canvas.create_rectangle(
    374.0,
    184.0,
    707.0,
    536.0,
    fill="#A0A0A0",
    outline="")

canvas.create_rectangle(
    380.0,
    191.0,
    700.0,
    529.0,
    fill="#393939",
    outline="")

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    541.0,
    259.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#B8B8B8",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=404.0,
    y=244.0,
    width=274.0,
    height=28.0
)

canvas.create_text(
    404.0,
    215.0,
    anchor="nw",
    text="Enter the radius of the sphere:",
    fill="#FFFFFF",
    font=("Inter", 19 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=470.0,
    y=493.0,
    width=141.0,
    height=28.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    541.0,
    118.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
