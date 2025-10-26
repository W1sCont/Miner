# інтерфейс
# гра
# створення кнопок
# надання кнопкам порядковийх номерів
# генерація випадкових мін
# добавлення мін
# гейм овер
# права кнопка миші
# відкривання пустих кнопок
# перемога

import tkinter as tk
import random
from random import shuffle



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


class MyButton(tk.Button):
    def __init__(self, master, x, y, number = 0, *args, **kwargs):
        super(MyButton, self).__init__(master, width=3, font="Colibri 15 bold")
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False
       

    

class Game:
    win = tk.Tk()
    
    ROW =10
    COLUMN = 7
    MINES = 2
    flags_count = 0
    flag_min = MINES


    def __init__(self):
        self.buttons = []
        
        
        for r in range(self.ROW + 2):
            temp = []
            for c in range(self.COLUMN + 2):
                btn = MyButton(self.win, x = r, y =c)
                btn.config(command=lambda button= btn: self.click(button))
                btn.bind("<Button-3>", self.right_click)
                temp.append(btn)
            self.buttons.append(temp)


    def click(self, clicked_button: MyButton):
        color = colors.get(clicked_button.count_bomb, "black")
        
        if clicked_button.is_mine:
            clicked_button.config(text="💣")
            clicked_button.is_open = True
            for r in range(1, self.ROW + 1): 
                for c in range(1, self.COLUMN + 1):
                    btn = self.buttons[r][c]
                    btn.config(state="disabled")  
                    clicked_button.config(relief=tk.SUNKEN)  
                    clicked_button.is_open = True     
                self.game_over()
        else:
            self.open_zero_buttons(clicked_button)
            # clicked_button.config(state="disabled") 
            # clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            # clicked_button.config(relief=tk.SUNKEN)
            clicked_button.is_open = True
            
            
    def open_zero_buttons(self, btn):
        memory = [btn]
        
        while memory:
            current_btn = memory.pop()
            
            if current_btn.is_open or current_btn.is_mine:
                continue
                
            color = colors.get(current_btn.count_bomb, "black")
            
            if current_btn.count_bomb:
                current_btn.config(text=current_btn.count_bomb, disabledforeground=color)
            else:
                current_btn.config(text="", disabledforeground=color)
            
            current_btn.config(state="disabled")
            current_btn.config(relief=tk.SUNKEN)
            current_btn.is_open = True

            if current_btn.count_bomb == 0:
                r = current_btn.x 
                c = current_btn.y
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if dr == 0 and dc == 0:
                            continue

                        next_btn = self.buttons[r+dr][c+dc]
                        if (not next_btn.is_open and 
                            1 <= next_btn.x <= self.ROW and 
                            1 <= next_btn.y <= self.COLUMN and 
                            next_btn not in memory):
                            memory.append(next_btn)

            
    def right_click(self, event):
        curent_btn = event.widget
        if curent_btn["state"] == "normal":
            if self.flags_count < self.MINES:
                curent_btn["state"] = "disabled"
                curent_btn["text"] = "🚩"
                curent_btn.is_open = True
                curent_btn.config(disabledforeground="red") 
                
                self.flags_count += 1
                self.mines_left_label.config(text=f"Мін залишилось: {self.MINES - self.flags_count}")
                self.check_win()
                
                
        elif curent_btn["text"] == "🚩":
                curent_btn["text"] = ""
                curent_btn["state"] = "normal"
                curent_btn.is_open = False
        
                self.flags_count -= 1
                self.mines_left_label.config(text=f"Мін залишилось: {self.MINES - self.flags_count}")
                

    def start(self):
        count = 1
        for r in range(1, self.ROW + 1): 
            for c in range(1, self.COLUMN + 1):
                btn = self.buttons[r][c]
                btn.number = count
                btn.grid(row=r, column=c, stick="NWES")
                count += 1
        self.create_menu()
        self.footer()
        self.add_bomb()
        self.count_mines()
        self.print_buttons()
        Game.win.mainloop()


    def game_over(self):
        for r in range(1, self.ROW + 1):
            for c in range(1, self.COLUMN + 1):
                btn = self.buttons[r][c]
                if btn.is_mine:
                    btn.config(text="💣", relief=tk.SUNKEN)


    def print_buttons(self):
        for r in range(1, self.ROW + 1):
            for c in range(1, self.COLUMN + 1):
                btn = self.buttons[r][c]
                if btn.is_mine:
                    print("*", end=" ")
                else:
                    print(btn.count_bomb, end=" ")
            print()


    def add_bomb(self):
        self.bomb_list = self.random_mines()
        print(self.bomb_list)
        for r in range(1, self.ROW + 1):
            for c in range(1, self.COLUMN + 1):
                btn = self.buttons[r][c]
                if btn.number in self.bomb_list:
                    # btn.config(text="*")
                    btn.is_mine =True
                # else:
                #     btn.config(text=f"{btn.number}")


    def count_mines(self):
        for r in range(1, self.ROW + 1):
            for c in range(1, self.COLUMN + 1):
                btn = self.buttons[r][c]
                self.count_bomb = 0
                if not btn.is_mine:
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            btn_quae = self.buttons[r+dr][c+dc]
                            if btn_quae.is_mine:
                                self.count_bomb += 1
                btn.count_bomb = self.count_bomb


    def create_menu(self):
        menubar = tk.Menu(self.win)
        self.win.config(menu=menubar)
        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label="Game", command=self.reload)
        settings_menu.add_command(label="Settings", command=self.settings_win)
        settings_menu.add_command(label="Exit", command=self.win.destroy)
        menubar.add_cascade(label="Menu", menu=settings_menu)


    def settings_win(self):
        win_settings = tk.Toplevel(self.win)
        win_settings.title("Налаштування")

        tk.Label(win_settings, text="К-сть рядків: "). grid(row=0, column=0, padx=20, pady=20)
        row_entry = tk.Entry(win_settings)
        row_entry.grid(row=1, column=1, padx=20, pady=20)
        row_entry.insert(0, str(self.ROW))

        tk.Label(win_settings, text="К-сть стовпців: "). grid(row=1, column=0, padx=20, pady=20)
        column_entry = tk.Entry(win_settings)
        column_entry.grid(row=0, column=1, padx=20, pady=20)
        column_entry.insert(0, str(self.COLUMN))

        tk.Label(win_settings, text="К-сть мін: "). grid(row=2, column=0, padx=20, pady=20)
        mines_entry = tk.Entry(win_settings)
        mines_entry.grid(row=2, column=1, padx=20, pady=20)
        mines_entry.insert(0, str(self.MINES))

        btn_ok = tk.Button(win_settings, text="ok", command=lambda: self.change_setting(row_entry, column_entry, mines_entry))
        btn_ok.grid(row=3, column=0, columnspan=4)


    def reload(self):
        global game
        for child in self.win.winfo_children():
            child.destroy()
        self.flags_count = 0
        game = Game()
        game.start()
        
       
    def change_setting(self, row_entry, column_entry, mines_entry):
        new_row = int(row_entry.get())
        new_column = int(column_entry.get())
        new_mines = int(mines_entry.get())
            
        Game.ROW = new_row
        Game.COLUMN = new_column
        Game.MINES = new_mines
        self.reload()
    

    def footer(self):
        footer_bar = tk.Frame(self.win, height=20)
        footer_bar.grid(row=self.ROW + 1, columnspan=self.COLUMN, padx=5, pady=5)

        self.mines_left_label = tk.Label(footer_bar, text=f"Мін залишилось: {self.MINES}", font="sans 12 bold")
        self.mines_left_label.grid(row=0, column=1)

    
    def check_win(self):
        if self.flags_count == self.MINES:
            correct_flags = 0
            for r in range(1, self.ROW + 1):
                for c in range(1, self.COLUMN + 1):
                    btn = self.buttons[r][c]
                    if btn["text"] == "🚩" and btn.is_mine:
                        correct_flags += 1
            if correct_flags == self.MINES:
                self.game_win()


    def game_win(self):
        for r in range(1, self.ROW + 1):
            for c in range(1, self.COLUMN + 1):
                btn = self.buttons[r][c]
                if btn.is_mine:
                    btn["text"] = "🚩"
                    btn["state"] = "disabled"
                    btn.config(disabledforeground="green", bg="lightgreen")
                btn.config(state="disabled")
        self.game_win_mess()


    def game_win_mess(self):
        message = tk.Toplevel(self.win)
        message.title("Перемога!")
        message.geometry("250x200+200+200")
        tk.Label(message, text="Ви виграли! 🎉", font="sans 20 bold").grid(row=3, column=3, padx=15, pady=10)
        tk.Button(message, text="Почати з початку", command=self.reload).grid(row=5, column=3, padx=15, pady=10) 
        tk.Button(message, text="Закрити", command=lambda: message.destroy()).grid(row=6, column=3, padx=15, pady=10) 


    def random_mines(self):
        random_numbers = list(range(1, Game.ROW * Game.COLUMN + 1))
        shuffle(random_numbers)
        # print(random_numbers[:Game.MINES])
        return random_numbers[:Game.MINES]



game = Game()
game.start()

