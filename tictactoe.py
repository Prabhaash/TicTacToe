import tkinter as tk
from tkinter import messagebox

# Create window
root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("320x380")
root.configure(bg="#222")  # dark background

current_player = "X"
board = [""] * 9

# Title label
title = tk.Label(root, text="Tic Tac Toe", font=("Arial", 18, "bold"),
                 bg="#222", fg="white")
title.pack(pady=10)

# Status label
status = tk.Label(root, text="Player X Turn", font=("Arial", 14),
                  bg="#222", fg="lightgreen")
status.pack()

# Frame for grid
frame = tk.Frame(root, bg="#222")
frame.pack(pady=10)

# Winner check
def check_winner():
    win_patterns = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]
    for a,b,c in win_patterns:
        if board[a] == board[b] == board[c] and board[a] != "":
            return board[a]
    return None

# Hover effect
def on_enter(e):
    e.widget['bg'] = "#555"

def on_leave(e):
    e.widget['bg'] = "#333"

# Click function
def on_click(index):
    global current_player
    
    if board[index] == "":
        board[index] = current_player
        
        color = "cyan" if current_player == "X" else "orange"
        buttons[index].config(text=current_player, fg=color)
        
        winner = check_winner()
        
        if winner:
            status.config(text=f"Player {winner} Wins!", fg="yellow")
            messagebox.showinfo("Winner", f"Player {winner} wins!")
            reset_game()
        elif "" not in board:
            status.config(text="It's a Draw!", fg="red")
            messagebox.showinfo("Draw", "It's a draw!")
            reset_game()
        else:
            current_player = "O" if current_player == "X" else "X"
            status.config(text=f"Player {current_player} Turn")

# Reset game
def reset_game():
    global board, current_player
    board = [""] * 9
    current_player = "X"
    status.config(text="Player X Turn", fg="lightgreen")
    
    for btn in buttons:
        btn.config(text="", bg="#333")

# Buttons
buttons = []

for i in range(9):
    btn = tk.Button(frame, text="", font=("Arial", 20, "bold"),
                    width=5, height=2, bg="#333", fg="white",
                    activebackground="#666",
                    command=lambda i=i: on_click(i))
    
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    
    # Hover binding
    btn.bind("<Enter>", on_enter)
    btn.bind("<Leave>", on_leave)
    
    buttons.append(btn)

# Reset button
reset_btn = tk.Button(root, text="Restart Game", font=("Arial", 12), bg="red", fg="white", command=reset_game)
reset_btn.pack(pady=10)

root.mainloop()