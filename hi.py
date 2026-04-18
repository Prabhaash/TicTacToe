import tkinter as tk

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = []

for i in range(3):
    row = []
    for j in range(3):
        btn = tk.Button(root, text="", width=10, height=3)
        btn.grid(row=i, column=j)
        row.append(btn)
    buttons.append(row)

root.mainloop()