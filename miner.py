import tkinter as tk
import time

# func 
#розміщення кнопок на полі
def add_bottom():
    for row in range(row_in_win):
        for col in range(column_in_win):
            tk.Button(window, text=f"{col}, {row}", command= "").grid(row = row, column = col)



# ===
# window

win_width = 700
win_height = 600

window = tk.Tk()
window.title("Сапер")
window.config(bg= "#e6f0ef")
window.geometry(f"{win_width}x{win_height}+500+100")
img_icon = tk.PhotoImage(file = "img_mine.png")
window.iconphoto(False, img_icon)

# ===
# змінні для к-сті кнопок на полі
column_in_win = 10
row_in_win = 10

# ===
add_bottom() # виклик функції для розміщення кнопок
window.mainloop()

# if __name__ == '__window__':  # перевірка, що файл запускається вручну
#     window()