import tkinter as tk
import time
from random import shuffle

# по індексах тупо,
# треба по коорденатах
# функція старт лишня



# window

win_width = 600
win_height = 600

window = tk.Tk()
window.title("Сапер")
window.config(bg= "#e6f0ef")
window.geometry(f"{win_width}x{win_height}+100+100")
img_icon = tk.PhotoImage(file = "img_mine.png")
window.iconphoto(False, img_icon)
# ===

# змінні для к-сті кнопок на полі
column_in_win = 10
row_in_win = 10
mines = 25
buttons = {}

# func 


#розміщення кнопок на полі
def create_bottoms():
    for row_el in range(row_in_win):
        for col_el in range(column_in_win):
            btn = tk.Button(window, width=4, height=2, font="sans 12 bold", command=lambda row_el=row_el, col_el=col_el: click(row_el, col_el))
            btn.grid(row=row_el, column=col_el)
            buttons[(row_el, col_el)] = btn


# випадкові числа для мін в зрізі вказаному користувачем
def random_mines_coords():
    btn_index = [(row, col) for row in range(row_in_win) for col in range(column_in_win)]
    shuffle(btn_index)
    return set(btn_index[:mines])

# присвоєння змінній рандомного списку
random_mines = random_mines_coords()


def click(row, col):
    btn = buttons[(row, col)]
    if (row, col) in random_mines:
        btn.config(text="*", bg="red")
        game_over()
    else:
        btn.config(text=count_adjacent(row, col), bg="lightgray", state="disabled")


def game_over():
    for (row_el, col_el), btn in buttons.items():
        if (row_el, col_el) in random_mines:
            btn.config(text="*", bg="red")
        btn.config(state="disabled")


def count_adjacent(row, col):
    count = 0
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if (i, j) in random_mines:
                count += 1
    return count


def main():
    create_bottoms()
    window.mainloop()


# ===







# ===


if __name__ == '__main__':
    main()