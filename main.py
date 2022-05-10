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
    bg='#000',
    width=settings.WIDTH,
    height=utils.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=utils.width_prct(30), y=50
)

left_frame = Frame(
    root,
    bg='#000',
    width=utils.width_prct(25),
    height=utils.height_prct(75)
)
left_frame.place(x=0, y=utils.height_prct(25))

instructions1 = Label(
    left_frame,
    bg='black',
    fg='white',
    text='Left click to reveal cell',
    font=('', 16)
)

instructions1.place(x=0, y=utils.height_prct(55))

instructions2 = Label(
    left_frame,
    bg='black',
    fg='white',
    text='Right click to mark cell',
    font=('', 16)
)

instructions2.place(x=0, y=utils.height_prct(60))

center_frame = Frame(
    root,
    bg='#000',
    width=utils.width_prct(75),
    height=utils.height_prct(75)
)
center_frame.place(x=utils.width_prct(25), y=utils.height_prct(25))

for x in range(settings.GRID_SIZE + 2):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

#  Run the window
root.mainloop()
