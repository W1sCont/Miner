import tkinter as tk
import time
from random import shuffle

# ===
# window

win_width = 1200
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
mines = 5

# func 


#розміщення кнопок на полі
def create_bottoms():
    for el_row in range(row_in_win):
        for el_col in range(column_in_win):
            btn = buttons[el_row][el_col]
            btn.grid(row=el_row, column=el_col)


def start():
    create_bottoms()
    window.mainloop()


# випадкові числа для мін в зрізі вказаному користувачем
def random_index_for_mines():
    btn_index = list(range(1, column_in_win * row_in_win + 1))
    shuffle(btn_index)
    return btn_index[:mines]
        
        
# перетворити кнопку на бомбу
def is_mine():
    pass


def main():
    start()


# розміщення бомб
def insert_mines():
    pass

# ===



# створення вкладеного списку для кнопок
buttons = []
count = 1
num_of_btn = False
index_mines = random_index_for_mines()
print(index_mines)
for el_row in range(row_in_win):
    temp = []
    for el_col in range(column_in_win):
        if count in index_mines:
            num_of_btn = True
            btn = tk.Button(window,text=f"{el_row}, {el_col}, #{count}, {num_of_btn}" , width=10, font='sans-serif 12 bold', bg="red")
            temp.append(btn)
            count += 1
        else:
            num_of_btn = False
            btn = tk.Button(window,text=f"{el_row}, {el_col}, #{count}, {num_of_btn}" , width=10, font='sans-serif 12 bold')
            temp.append(btn)
            count += 1
    buttons.append(temp)

# грід кнопок на полі def create_bottoms()
# for el_row in range(row_in_win):
#     for el_col in range(column_in_win):
#         btn = buttons[el_row][el_col]
#         btn.grid(row=el_row, column=el_col)


# ===


if __name__ == '__main__':
    main()
