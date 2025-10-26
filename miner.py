import tkinter as tk
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
mines = 2
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
    global flags_count
    curent_btn = event.widget
    
    if curent_btn["state"] == "normal":
        
        if flags_count < mines:
            curent_btn["state"] = "disabled"
            curent_btn["text"] = "🚩"
            curent_btn.config(disabledforeground="red")
            flags_count += 1
            mines_left_label.config(text=f"Мін залишилось: {mines - flags_count}")
            check_win()
            
    elif curent_btn["text"] == "🚩":
        curent_btn["text"] = ""
        curent_btn["state"] = "normal"
        flags_count -= 1
        mines_left_label.config(text=f"Мін залишилось: {mines - flags_count}")


# випадкові числа для мін в зрізі вказаному користувачем
def random_mines_coords():
    btn_index = [(row, col) for row in range(row_in_win) for col in range(column_in_win)]
    shuffle(btn_index)
    return set(btn_index[:mines])


# логіка при натисканні на кнопку
def click(row, col):
    btn = buttons[(row, col)]
    if (row, col) in random_mines:
        btn.config(text="💣", bg="red", disabledforeground="black")
        game_over()
    else:
        # number = count_adjacent(row, col)
        # if number != 0:
        #     color = colors.get(number, "black")
        #     btn.config(text=number, bg="lightgray", state="disabled", disabledforeground=color, relief=tk.SUNKEN)
        # else:
        #     color = colors.get(number, "black")
        #     btn.config(text="", bg="lightgray", state="disabled", disabledforeground=color, relief=tk.SUNKEN)
        open_zero_btn(row, col)

    print(count_adjacent(row, col))


# авто відкривання пустих кнопок через чергу найближчих пустих
def open_zero_btn(row, col):
    memory = [(row, col)]
    visited = set()

    while memory:
        current_row, current_col = memory.pop()
                
        if (current_row, current_col) in visited:
            continue
                
        
        visited.add((current_row, current_col))
        current_btn = buttons[(current_row, current_col)]
        if  not current_btn.config(text="💣"):
                
            current_number = count_adjacent(current_row, current_col)

            color = colors.get(current_number, "black")
            current_btn.config(text=current_number, bg="lightgray", state="disabled", disabledforeground=color, relief=tk.SUNKEN)
                
            if current_number == 0:
                current_btn.config(text="", bg="lightgray", state="disabled", relief=tk.SUNKEN)
                    
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not abs(dx - dy) == 1: 
                            continue
                            
                        new_row = current_row + dx
                        new_col = current_col + dy
                        print(new_row, new_col)
                            

                        if 0 <= new_row < row_in_win and 0 <= new_col < column_in_win:
                            if (new_row, new_col) not in visited:
                                next_btn = buttons[(new_row, new_col)]
                                if next_btn["state"] == "normal":
                                    memory.append((new_row, new_col))
                
                    
# функція меню завершення гри
def game_over():
    for (row_el, col_el), btn in buttons.items():
        if (row_el, col_el) in random_mines:
            btn.config(text="💣", bg="red", disabledforeground="black")
        btn.config(state="disabled")
    game_over_mess()


def game_over_mess():
    
    message = tk.Toplevel(window)
    message.title("Game over")
    message.geometry("250x200+200+200")
    tk.Label(message, text="Гру завершено", font="sans 20 bold").grid(row=3, column=2, padx=15, pady=10)
    tk.Button(message, text="Почати з початку", command=reload).grid(row=5, column=2, padx=15, pady=10) 
    tk.Button(message, text="Закрити", command=lambda: message.destroy()).grid(row=6, column=2, padx=15, pady=10) 


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
    global random_mines, buttons, flags_count
    for child in window.winfo_children():
        child.destroy()
    buttons.clear()
    
    create_menu()
    footer()
    random_mines = random_mines_coords()
    flags_count = 0
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


def footer():
    global mines_left_label, flags_count

    footer_bar = tk.Frame(window, bg="lightblue", height=20)
    footer_bar.grid(row=row_in_win + 1, columnspan=column_in_win, padx=5, pady=5, sticky="ew")

    mines_left_label = tk.Label(footer_bar, text=f"Мін залишилось: {mines}", bg="lightblue", font="sans 12 bold")
    mines_left_label.grid(row=0, column=1, padx=20)


# реалізація перевірки перемоги
def check_win():
    if flags_count == mines:
        correct_flags = 0
        for dx in range(row_in_win):
            for dy in range(column_in_win):
                btn = buttons[(dx, dy)]

                if btn["text"] == "🚩" and (dx, dy) in random_mines:
                    correct_flags += 1
        
        if correct_flags == mines:
            game_win()
        

# функція обробки перемоги
def game_win():
    global random_mines, flags_count

    for (row_el, col_el), btn in buttons.items():
        if (row_el, col_el) in random_mines:
            btn["text"] = "🚩"
            btn["state"] = "disabled"
            btn.config(disabledforeground="green", bg="lightgreen")
        btn.config(state="disabled")

    random_mines = random_mines_coords()
    flags_count = 0
    game_win_mess()


def game_win_mess():
    message = tk.Toplevel(window)
    message.title("Перемога!")
    message.geometry("250x200+200+200")
    tk.Label(message, text="Ви виграли! 🎉", font="sans 20 bold").grid(row=3, column=3, padx=15, pady=10)
    tk.Button(message, text="Почати з початку", command=reload).grid(row=5, column=3, padx=15, pady=10) 
    tk.Button(message, text="Закрити", command=lambda: message.destroy()).grid(row=6, column=3, padx=15, pady=10) 


def main():
    create_menu()
    footer()
    create_bottoms()
    window.mainloop()


# присвоєння змінній рандомного списку
random_mines = random_mines_coords()

flags_count = 0

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

# продумати логіку перемоги у грі коли всі прапорці будуть на мінах

# ідею зупинки і запуску гри поки відкладу, мало часу

# добавити авто відкривання пустих кнопок

# доробити обмеження на к-сть прапорців

# добавити ефект кнопки після натискання

# ===


if __name__ == '__main__':
    main()