import tkinter as tk
from tkinter import messagebox

# Track the current token and the game state
current_token = "X"

def create_images():
    """Load images after initializing the Tkinter root window."""
    empty_image = tk.PhotoImage(file="/Users/yukthapriya/Downloads/image/empty.gif").zoom(2, 2)  # Enlarge images
    x_image = tk.PhotoImage(file="/Users/yukthapriya/Downloads/image/x.gif").zoom(2, 2)
    o_image = tk.PhotoImage(file="/Users/yukthapriya/Downloads/image/o.gif").zoom(2, 2)
    return empty_image, x_image, o_image

class Cell(tk.Label):
    def __init__(self, master, row, col, images):
        super().__init__(master, image=images[0], relief='solid', borderwidth=2, width=120, height=120)  # Bigger cells
        self.row = row
        self.col = col
        self.token = " "  # " ", "X", or "O"
        self.images = images
        self.bind("<Button-1>", self.flip)

    def flip(self, event):
        global current_token
        if self.token == " " and current_token != "Over":
            self.token = current_token
            self.config(image=self.images[1] if current_token == "X" else self.images[2])
            if is_won():
                messagebox.showinfo("Game Over", f"Player {current_token} wins!")
                reset_game()
            elif is_full():
                messagebox.showinfo("Game Over", "It's a tie!")
                reset_game()
            else:
                current_token = "O" if current_token == "X" else "X"

def is_won():
    for i in range(3):
        # Check rows and columns
        if (cells[i][0].token == cells[i][1].token == cells[i][2].token != " " or
            cells[0][i].token == cells[1][i].token == cells[2][i].token != " "):
            return True

    # Check diagonals
    if (cells[0][0].token == cells[1][1].token == cells[2][2].token != " " or
        cells[0][2].token == cells[1][1].token == cells[2][0].token != " "):
        return True

    return False

def is_full():
    return all(cells[row][col].token != " " for row in range(3) for col in range(3))

def reset_game():
    global current_token
    current_token = "X"
    for row in range(3):
        for col in range(3):
            cells[row][col].token = " "
            cells[row][col].config(image=empty_image)

# Initialize the main Tkinter window
root = tk.Tk()
root.title("Tic-Tac-Toe")
root.geometry("600x600")  # Increased window size

# Load images after creating the root window
empty_image, x_image, o_image = create_images()

# Create the 3x3 grid of cells
cells = [[Cell(root, row, col, (empty_image, x_image, o_image)) for col in range(3)] for row in range(3)]
for row in range(3):
    for col in range(3):
        cells[row][col].grid(row=row, column=col, padx=10, pady=10)  # Add spacing between cells

# Run the main Tkinter loop
root.mainloop()
