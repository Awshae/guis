from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/asherjarvis/Desktop/build/assets/cuboid_asset")


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
    373.0,
    195.0,
    706.0,
    621.0,
    fill="#A0A0A0",
    outline="")

canvas.create_rectangle(
    379.0,
    203.0,
    699.0,
    612.0,
    fill="#393939",
    outline="")

canvas.create_text(
    395.0,
    393.0,
    anchor="nw",
    text="Enter the height of the cuboid:",
    fill="#FFFFFF",
    font=("Inter", 19 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    538.5,
    255.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#B8B8B8",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=394.0,
    y=240.0,
    width=289.0,
    height=28.0
)

canvas.create_text(
    394.0,
    306.0,
    anchor="nw",
    text="Enter the breadth of the cuboid:",
    fill="#FFFFFF",
    font=("Inter", 19 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    538.5,
    346.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#B8B8B8",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=394.0,
    y=331.0,
    width=289.0,
    height=28.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    538.5,
    437.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#B8B8B8",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=394.0,
    y=422.0,
    width=289.0,
    height=28.0
)

canvas.create_text(
    394.0,
    214.0,
    anchor="nw",
    text="Enter the length of the cuboid:",
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
    x=466.0,
    y=578.0,
    width=141.0,
    height=28.0
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    537.0,
    122.0,
    image=image_image_2
)
window.resizable(False, False)
window.mainloop()
