from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"/Users/asherjarvis/Desktop/build/assets/selection_asset")


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
    584.0,
    225.0,
    884.0,
    298.0,
    fill="#5F5F5F",
    outline="")

canvas.create_rectangle(
    211.0,
    439.0,
    511.0,
    512.0,
    fill="#5F5F5F",
    outline="")

canvas.create_rectangle(
    211.0,
    332.0,
    511.0,
    405.0,
    fill="#5F5F5F",
    outline="")

canvas.create_rectangle(
    584.0,
    439.0,
    884.0,
    512.0,
    fill="#5F5F5F",
    outline="")

canvas.create_rectangle(
    584.0,
    332.0,
    884.0,
    405.0,
    fill="#5F5F5F",
    outline="")

canvas.create_rectangle(
    211.0,
    225.0,
    511.0,
    298.0,
    fill="#5F5F5F",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1_cube clicked"),
    relief="flat"
)
button_1.place(
    x=204.0,
    y=220.0,
    width=298.0,
    height=66.0
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2_sphere clicked"),
    relief="flat"
)
button_2.place(
    x=577.0,
    y=220.0,
    width=298.0,
    height=66.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3_cuboid clicked"),
    relief="flat"
)
button_3.place(
    x=204.0,
    y=327.0,
    width=298.0,
    height=66.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4_cylinder clicked"),
    relief="flat"
)
button_4.place(
    x=204.0,
    y=434.0,
    width=298.0,
    height=66.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5_cone clicked"),
    relief="flat"
)
button_5.place(
    x=577.0,
    y=327.0,
    width=298.0,
    height=66.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6_pyramid clicked"),
    relief="flat"
)
button_6.place(
    x=577.0,
    y=434.0,
    width=298.0,
    height=66.0
)
window.resizable(False, False)
window.mainloop()
