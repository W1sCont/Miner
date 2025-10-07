import tkinter as tk
import time

# func 




# ===
# window

win_width = 700
win_height = 600

window = tk.Tk()
window.title("Mine")
window.config(bg= "#e6f0ef")
window.geometry(f"{win_width}x{win_height}+500+100")
img_icon = tk.PhotoImage(file = "img_mine.png")
window.iconphoto(False, img_icon)

# ===



# ===

window.mainloop()

# if __name__ == '__window__':  # перевірка, що файл запускається вручну
#     window()