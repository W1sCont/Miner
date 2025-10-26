# # x = 5
# # y = 5

# # for el_x in [-1, 0, 1]:
# #     for el_y in [-1, 0, 1]:
# #         if abs(el_x-el_y) == 1:
# #             print(x + el_x, y + el_y)


# # while list_count_zero:
# #     courent_coord = list_count_zero.pop()
#     # if courent_coord in random_mines_coords:
#     #     pass
#     # else:
#     #     pass


# # x = 5
# # y = 5

# # list_count_zero = []

# # for el in range(x):
# #     for i in range(y):
# #         list_count_zero.append([el, i])

# # print(list_count_zero)

# # list_count_zero = {}
# # count = 0

# # for el in range(x):
# #     for i in range(y):
# #         list_count_zero[(el, i)] = count
# #         count += 1

# # # print(list_count_zero)

# # for el in list_count_zero:
# #     print(el, end="")


# # curent_btn = (3,4)

# # x = curent_btn[0]
# # y = curent_btn[1]

# # print(curent_btn)
# # print(x)
# # print(y)

# else:
#         number = count_adjacent(row, col)
#         if number != 0:
#             color = colors.get(number, "black")
#             btn.config(text=number, bg="lightgray", state="disabled", disabledforeground=color, relief=tk.SUNKEN)
#         else:
#             color = colors.get(number, "black")
#             btn.config(text=number, bg="lightgray", state="disabled", disabledforeground=color, relief=tk.SUNKEN)



# def open_zero_btn(row, col):
#     memory = [(row, col)]
#     visited = set()
            
#     while memory:
#         current_row, current_col = memory.pop()
                
#         if (current_row, current_col) in visited:
#             continue
                
#         visited.add((current_row, current_col))
#         current_btn = buttons[(current_row, current_col)]
                
#         current_number = count_adjacent(current_row, current_col)
                
#         if current_number == 0:
#             current_btn.config(text="", bg="lightgray", state="disabled", relief=tk.SUNKEN)
                    
#             for dx in [-1, 0, 1]:
#                 for dy in [-1, 0, 1]:
#                     if dx == 0 and dy == 0: 
#                         continue
                            
#                 new_row = current_row + dx
#                 new_col = current_col + dy
                            

#                 if 0 <= new_row < row_in_win and 0 <= new_col < column_in_win:
#                     if (new_row, new_col) not in visited:
#                         next_btn = buttons[(new_row, new_col)]
#                         if next_btn["state"] == "normal":
#                             memory.append((new_row, new_col))
#                 else:
#                     color = colors.get(current_number, "black")
#                     current_btn.config(text=current_number, bg="lightgray", state="disabled", 
#                                      disabledforeground=color, relief=tk.SUNKEN)
                    




def check_win():
    """Перевіряє умови перемоги: всі міни з прапорцями АБО всі безпечні клітинки відкриті"""
    # Спосіб 1: Всі прапорці правильно розставлені
    if flags_count == mines:
        correct_flags = 0
        for row in range(rows):
            for col in range(cols):
                btn = buttons[row][col]
                if btn["text"] == "🚩" and field[row][col] == -1:
                    correct_flags += 1
        
        if correct_flags == mines:
            return True
    
    # Спосіб 2: Всі безпечні клітинки відкриті
    total_cells = rows * cols
    safe_cells = total_cells - mines
    opened_cells = 0
    
    for row in range(rows):
        for col in range(cols):
            btn = buttons[row][col]
            is_mine = field[row][col] == -1
            is_opened = btn["state"] == "disabled" and btn["text"] != "🚩"
            
            if not is_mine and is_opened:
                opened_cells += 1
    
    return opened_cells == safe_cells

def game_win():
    """Обробка перемоги"""
    # Відкриваємо всі міни із зеленими прапорцями
    for row in range(rows):
        for col in range(cols):
            btn = buttons[row][col]
            if field[row][col] == -1:
                btn["text"] = "🚩"
                btn["state"] = "disabled"
                btn.config(disabledforeground="green")
    
    messagebox.showinfo("Перемога! 🎉", f"Вітаємо! Ви виграли!\nЧас: {timer_seconds} секунд")
    
    # Блокуємо гру
    for row in buttons:
        for btn in row:
            btn.unbind("<Button-1>")
            btn.unbind("<Button-3>")
