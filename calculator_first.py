import tkinter as tk

calculation = ''

def add(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, 'end')
    text_result.insert(1.0, calculation)


def evaluate():
    global calculation
    try:
        result = str(eval(calculation))
        calculation = ''
        text_result.delete(1.0,'end')
        text_result.insert(1.0,result)
    except:
        clear()
        text_result.insert(1.0, "Error")



def clear():
    global calculation
    calculation = ''
    text_result.delete(1.0,'end')

root = tk.Tk()
root.geometry('400x500')
root.title("Calculator")
root.configure(bg='#2e2e2e')

text_result = tk.Text(root, height=2, width=20, font=('Arial', 24),bg="#333333", fg="white", bd=0 )
text_result.grid(columnspan=4, pady=20)

btn_style = {"width": 5, "height": 2, "font": ('Arial', 14), "bg": "#4caf50", "fg": "white", "bd": 0, "relief": "raised"}
buttons = [
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('/', 2, 3),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('*', 3, 3),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('-', 4, 3),
    ('0', 5, 1), ('.', 5, 0), ('=', 5, 2), ('+', 5, 3),
    ('C', 6, 0), ('(', 6, 1), (')', 6, 2), ('AC', 6, 3)
]

for (text, row, col) in buttons:
    if text == '=':
        action = evaluate
    elif text == 'C':
        action = lambda: add("")
    elif text == 'AC':
        action = clear
    else:
        action = lambda t=text: add(t)

    tk.Button(root, text=text, command=action, **btn_style).grid(row=row, column=col, padx=5, pady=5)

for widget in root.winfo_children():
    widget.grid_configure(padx=5, pady=5)

root.mainloop()


