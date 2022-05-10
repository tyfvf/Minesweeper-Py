from sys import exit
from ctypes import windll
from tkinter import Button, Label
from random import sample
import settings


class Cell:
    all = []
    cell_count = settings.CELL_COUNT - settings.MINES_COUNT
    cell_count_label_object = None

    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=3,
            height=1,
            font=('', 24)

        )
        btn.bind('<Button-1>', self.left_click_actions)  # Left Click
        btn.bind('<Button-3>', self.right_click_actions)  # Right Click
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
        label = Label(
            location,
            bg='black',
            fg='white',
            text=f'Cells Left: {Cell.cell_count}',
            font=("Times new Roman", 30)
        )
        Cell.cell_count_label_object = label

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    if cell_obj.surrounded_cells_mines_length == 0:
                        for c in cell_obj.surrounded_cells:
                            if c.surrounded_cells_mines_length == 0:
                                for ce in c.surrounded_cells:
                                    ce.show_cell()
                            c.show_cell()
                    cell_obj.show_cell()
            self.show_cell()

            if Cell.cell_count == 0:
                windll.user32.MessageBoxW(0, 'Congratulations! You won the game!', 'You won!', 0)

        # Cancel Left and Right click events if cell is already opened
        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def get_cell_by_axis(self, x, y):
        # Return a cell object based on the value of x, y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surrounded_cells(self):
        # Get surrounded_cells
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]

        # Eliminate places that have no cell is certain surrounding
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1

            self.cell_btn_object.configure(
                text=self.surrounded_cells_mines_length
            )

            if self.surrounded_cells_mines_length == 1:
                self.cell_btn_object.configure(
                    fg='#0100FC'
                )
            elif self.surrounded_cells_mines_length == 2:
                self.cell_btn_object.configure(
                    fg='#037F01'
                )
            elif self.surrounded_cells_mines_length == 3:
                self.cell_btn_object.configure(
                    fg='#FC0100'
                )
            elif self.surrounded_cells_mines_length == 4:
                self.cell_btn_object.configure(
                    fg='#010080'
                )
            elif self.surrounded_cells_mines_length == 5:
                self.cell_btn_object.configure(
                    fg='#7E0301'
                )
            elif self.surrounded_cells_mines_length == 6:
                self.cell_btn_object.configure(
                    fg='#02807F'
                )
            elif self.surrounded_cells_mines_length == 7:
                self.cell_btn_object.configure(
                    fg='#000101'
                )
            elif self.surrounded_cells_mines_length == 8:
                self.cell_btn_object.configure(
                    fg='#808080'
                )

            # Replace the text of cell count label with the newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(text=f'Cells Left: {Cell.cell_count}')

            # If mine candidate change the background color
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )

        # Mark the cell as opened
        self.is_opened = True

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game Over', 0)
        exit()

    def right_click_actions(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(bg='orange')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(bg='SystemButtonFace')
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = sample(Cell.all, settings.MINES_COUNT)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'
