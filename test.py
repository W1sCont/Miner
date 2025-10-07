import tkinter as tk

win_width = 300
win_height = 400

def say_hello():
    print("Hello")


def add_label():
    label = tk.Label(win, text = "new")
    label.pack()


win = tk.Tk()
win.title("Сапер")
win.config(bg= "#e6f0ef")
win.geometry(f"{win_width}x{win_height}+1000+100") # задаєьбся розміри вікна та додаткові параметри відступу вікна при відкриванні (початкове значення верхній лівий кут)
win.resizable(False, False)  # можливість змінювати розмірми вікна
win.minsize(300, 400) 
win.maxsize(600, 800)
photo = tk.PhotoImage(file = "img_mine.png")
win.iconphoto(False, photo)

label_1 = tk.Label(win, text = "Start",                 # перший параметр де буде відображатись, другий що саме
                    bg = "#11d646",                         
                    fg = "white",
                    font = ("erial", 15, "bold"),
                    padx = 5,
                    pady = 5,
                    width = 5,
                    height = 2,
                    anchor = "nw",                      # розміщення тексту 
                    relief=tk.RAISED,                   # рамка
                    bd = 2,                           # розмір рамки
                    justify = tk.CENTER)                # вирівнювання тексту (CENTER - значеня за замовчуванням)        
label_1.pack()  # метод для розположення лейбла на вікні

btn1 = tk.Button(win, text="Hello", command = say_hello) # функція без виклику (), сама кнопка її викличе
btn2 = tk.Button(win, text="Label", command = add_label)
btn3 = tk.Button(win, text="Label lambda", command = 
                 lambda: tk.Label(win, text = "New Lambda").pack())

btn1.pack() # добавляє кнопку на форму
btn2.pack()
btn3.pack()



win.mainloop()