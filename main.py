# from tkinter import *
#
# root = Tk()
# root.title("Приложение на Tkinter")
#
# root.geometry("300x250")
#
# label = Label(text="Hello РУКОН ЦЕЛЬ")
# label.pack()
#
# root.mainloop()


# Счетчик суммы и разности
# import tkinter as tk
#
#
# def increment_counter():
#     global counter
#     counter += 1
#     counter_label.config(text=f"Сумма: {counter}")
#
#
# def decrement_counter():
#     global counter
#     counter -= 1
#     counter_label.config(text=f"Разность: {counter}")
#
#
# counter = 0
#
# window = tk.Tk()
# window.title("Счетчик суммы и разности")
# window.geometry("350x100")
#
# counter_label = tk.Label(window, text="Счетчик: 0")
# counter_label.pack()
#
# increment_button = tk.Button(window, text="Сумма", command=increment_counter)
# increment_button.pack()
#
# decrement_button = tk.Button(window, text="Сумма", command=decrement_counter)
# decrement_button.pack()
#
# window.mainloop()



# #Задача: Создать кнопку "Нажми меня" и при нажатии на неё выводить сообщение "Привет, мир!" в консоль.

# import tkinter as tk
#
# def show_message():
#     print("Привет, мир!")
#
# root = tk.Tk()
# button = tk.Button(root, text="Нажми на меня", command=show_message)
# button.pack()
# root.mainloop()


# #Задача: Создать поле для ввода текста и при нажатии кнопки "Вывести" выводить введенный текст в консоль.
# import tkinter as tk
#
# def display_text():
#     input_text = entry.get()
#     print(input_text)
#
# root = tk.Tk()
# entry = tk.Entry(root)
# entry.pack()
# button = tk.Button(root, text="Вывести", command=display_text)
# button.pack()
# root.mainloop()


# #Задача: Создать две кнопки "Включить" и "Выключить", меняющие текст на них при каждом нажатии.

# import tkinter as tk
#
#
# def toggle_button_state():
#     if button["text"] == "Включить":
#         button["text"] = "Выключить"
#     else:
#         button["text"] = "Включить"
#
#
# root = tk.Tk()
# button = tk.Button(root, text="Включить", command=lambda: toggle_button_state())
# button.pack()
# root.mainloop()


# #Задача: Создать окно с изображением.
# import tkinter as tk
# from PIL import ImageTk, Image
#
# root = tk.Tk()
# image = ImageTk.PhotoImage(Image.open("image.jpg"))
# label = tk.Label(root, image=image)
# label.pack()
# root.mainloop()

# #Задача: Создать список с несколькими элементами и при выборе элемента выводить его значение в консоль
# import tkinter as tk
#
# def on_select(event):
#     selected_item = listbox.get(listbox.curselection())
#     print(selected_item)
#
# root = tk.Tk()
# listbox = tk.Listbox(root)
# listbox.insert(0, "Элемент 1")
# listbox.insert(1, "Элемент 2")
# listbox.insert(2, "Элемент 3")
# listbox.bind("<<ListboxSelect>>", on_select)
# listbox.pack()
# root.mainloop()
#
# #Задача: Создать окно с несколькими радиокнопками и при выборе радиокнопки выводить её значение в консоль.
# import tkinter as tk
#
# def on_select():
#     selected_value = var.get()
#     print(selected_value)
#
# root = tk.Tk()
# var = tk.StringVar()
# radio_button1 = tk.Radiobutton(root, text="Радиокнопка 1", variable=var, value="1", command=on_select)
# radio_button2 = tk.Radiobutton(root, text="Радиокнопка 2", variable=var, value="2", command=on_select)
# radio_button1.pack()
# radio_button2.pack()
# root.mainloop()
#
# #Задача: Создать простое меню с несколькими пунктами и при выборе пункта выводить его значение в консоль. Решение:
# import tkinter as tk
#
# def on_select(value):
#     print(value)
#
# root = tk.Tk()
# menu = tk.Menu(root)
# root.config(menu=menu)
# submenu = tk.Menu(menu)
# menu.add_cascade(label="Пункты", menu=submenu)
# submenu.add_command(label="Пункт 1", command=lambda: on_select("Пункт 1"))
# submenu.add_command(label="Пункт 2", command=lambda: on_select("Пункт 2"))
# submenu.add_command(label="Пункт 3", command=lambda: on_select("Пункт 3"))
# root.mainloop()









