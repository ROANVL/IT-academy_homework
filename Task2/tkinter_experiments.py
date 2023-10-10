import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


from time_formatting import convert_time_to_spoken_word as cur_time
from validation import validate_time_format

wrong_input_count = 0
max_wrong_inputs = 3


def convert_time(event=None):
    # Получаем введенное пользователем время
    time_input = entry.get()

    if validate_time_format(time_input):
        # Если формат времени корректный, преобразуем и выводим результат
        formatted_time = cur_time(time_input)
        result_label.configure(text=formatted_time,
                               foreground="green", font=("Helvetica", 24))
        add_to_history(formatted_time)
        update_history_text()
        entry_var.set("")
    else:
        # Если формат времени некорректный, выводим сообщение об ошибке
        result_label.configure(text="Неверный формат времени или недопустимые "
                               "значения.\nПопробуйте снова",
                               foreground="red", font=("Helvetica", 12))
        add_to_history("Неверный ввод")
        update_history_text()
        entry_var.set("")  # Очищаем ячейку ввода

        global wrong_input_count
        wrong_input_count += 1
        if wrong_input_count >= max_wrong_inputs:
            finish_program()
        else:
            wrong_input_count = 0  # Сбрасываем счетчик неверных вводов


def finish_program():
    # Завершение программы по запросу пользователя
    messagebox.showinfo(
        "Спасибо", "Спасибо, что воспользовались нашей программой!")
    window.destroy()


def add_to_history(formatted_time):
    # Добавление времени в историю
    history.append(formatted_time)
    if len(history) > 5:
        history.pop(0)


def update_history_text():
    # Обновление текста истории
    history_text.configure(state="normal")
    history_text.delete("1.0", tk.END)
    for time in reversed(history):
        history_text.insert(tk.END, time + "\n")
    history_text.configure(state="disabled")


def validate_input(char):
    # Валидация вводимых символов
    if char.isdigit() or char == ":":
        return True
    return False


WINDOW_WIDTH = 650
WINDOW_HEIGHT = 400

window = tk.Tk()
window.title("Программа Конвертация Времени. Версия 1.0.0")
window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

style = ttk.Style()
style.configure("TFrame", background="#f0f0f0")
style.configure("TLabel", background="#f0f0f0", font=("Helvetica", 12))
style.configure("TEntry", fieldbackground="#ffffff", font=("Helvetica", 32))

frame = ttk.Frame(window, padding="20")
frame.pack()

label = ttk.Label(
    frame, text="Введите время в формате ЧЧ:ММ (24-часовой формат).",
    font=("Helvetica", 12))
label.pack(pady=5)

entry_var = tk.StringVar()
entry = ttk.Entry(frame, textvariable=entry_var,
                  font=("Helvetica", 24), justify="center")
entry.pack(pady=5)
entry_var.set("")

# Применение маски ввода для поля ввода времени
entry.config(validate="key", validatecommand=(
    entry.register(validate_input), '%S'))

window.bind('<Return>', convert_time)

result_label = ttk.Label(frame, text="", font=(
    "Helvetica", 14), wraplength=WINDOW_WIDTH)
result_label.pack(pady=10)

history_frame = ttk.Frame(window, padding="20")
history_frame.pack(pady=10)

history_label = ttk.Label(
    history_frame, text="История выводов", font=("Helvetica", 12))
history_label.pack()

history_text = tk.Text(history_frame, font=(
    "Helvetica", 12), height=5, state="disabled")
history_text.pack(fill="both", expand=True)

button_finish = ttk.Button(window, text="Завершить", command=finish_program)
button_finish.pack(side=tk.BOTTOM, pady=5)

history = []

for child in frame.winfo_children():
    child.pack_configure(padx=5, pady=5)

window.mainloop()
