import tkinter as tk
import time
from random import shuffle

# словник кольорів, 8 це максимальна к-сть "сусідів" у кнопки
colors = {
    1: "#3498eb",
    2: "#34eb4c",
    3: "#a234eb",
    4: "#eb9f34",
    5: "#eb3468",
    6: "#eb4634",
    7: "#2f2f5e",
    8: "#9c4fa8"
}


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
            btn.bind("<Button-3>", right_click) # event, function


# функція для правої кнп миші щоб втановити або зняти прапорець 
def right_click(event):
    curent_btn = event.widget
    if curent_btn["state"] == "normal":
        curent_btn["state"] = "disabled"
        curent_btn["text"] = "🚩"
    elif curent_btn["text"] == "🚩":
        curent_btn["text"] = ""
        curent_btn["state"] = "normal"


# випадкові числа для мін в зрізі вказаному користувачем
def random_mines_coords():
    btn_index = [(row, col) for row in range(row_in_win) for col in range(column_in_win)]
    shuffle(btn_index)
    return set(btn_index[:mines])


# присвоєння змінній рандомного списку
random_mines = random_mines_coords()


# логіка при натисканні на кнопку
def click(row, col):
    btn = buttons[(row, col)]
    if (row, col) in random_mines:
        btn.config(text="*", bg="red")
        game_over()
    else:
        number = count_adjacent(row, col)
        color = colors.get(number, "black")
        btn.config(text=number, bg="lightgray", state="disabled", disabledforeground=color)
        

# функція меню завепшення гри
def game_over():
    for (row_el, col_el), btn in buttons.items():
        if (row_el, col_el) in random_mines:
            btn.config(text="*", bg="red")
        btn.config(state="disabled")


# лічильник для відображення ближайших мін
def count_adjacent(row, col):
    count = 0
    for row_el in range(row-1, row+2):
        for col_el in range(col-1, col+2):
            if (row_el, col_el) in random_mines:
                count += 1
    return count


# функція меню reload, перезапуск гри з поправленим перестворенням мін і поля
def reload():
    global random_mines, buttons
    for child in window.winfo_children():
        child.destroy()
    buttons.clear()
    
    create_menu()
    random_mines = random_mines_coords()
    create_bottoms()


# функція меню settings
def settings_win():
    win_settings = tk.Toplevel(window)
    win_settings.title("Налаштування")

    tk.Label(win_settings, text="К-сть рядків: "). grid(row=0, column=0, padx=20, pady=20)
    row_in_win_entry = tk.Entry(win_settings)
    row_in_win_entry.grid(row=1, column=1, padx=20, pady=20)
    row_in_win_entry.insert(0, str(row_in_win))

    tk.Label(win_settings, text="К-сть стовпців: "). grid(row=1, column=0, padx=20, pady=20)
    column_in_win_entry = tk.Entry(win_settings)
    column_in_win_entry.grid(row=0, column=1, padx=20, pady=20)
    column_in_win_entry.insert(0, str(column_in_win))

    tk.Label(win_settings, text="К-сть мін: "). grid(row=2, column=0, padx=20, pady=20)
    mines_entry = tk.Entry(win_settings)
    mines_entry.grid(row=2, column=1, padx=20, pady=20)
    mines_entry.insert(0, str(mines))

    btn_ok = tk.Button(win_settings, text="ok", command=lambda: change_setting(row_in_win_entry, column_in_win_entry, mines_entry))
    btn_ok.grid(row=3, column=0, columnspan=2)


# try except перевірити чи не викливає помилку коли ввели не число
def change_setting(row_in_win_entry, column_in_win_entry, mines_entry):
    global row_in_win, column_in_win, mines, random_mines, buttons
    row_in_win = int(row_in_win_entry.get())
    column_in_win = int(column_in_win_entry.get())
    mines = int(mines_entry.get())
    reload()


# функція створення меню
def create_menu():
    menubar = tk.Menu(window)
    window.config(menu=menubar)
    settings_menu = tk.Menu(menubar, tearoff=0)
    settings_menu.add_command(label="Game", command=reload)
    settings_menu.add_command(label="Settings", command=settings_win)
    settings_menu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="Menu", menu=settings_menu)


def main():
    create_menu()
    create_bottoms()
    window.mainloop()


# ===
# window

# win_width = 600
# win_height = 600

window = tk.Tk()
window.title("Сапер")
window.config(bg= "#e6f0ef")
# window.geometry(f"{win_width}x{win_height}+100+100")
img_icon = tk.PhotoImage(file = "img_mine.png")
window.iconphoto(False, img_icon)

# window






# ===


if __name__ == '__main__':
    main()