from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()
#  Override the setting of the window
root.configure(bg='#000')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

center_frame = Frame(
    root,
    bg='green',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )

Cell.randomize_mines()
for c in Cell.all:
    print(c.is_mine)

#  Run the window
root.mainloop()
