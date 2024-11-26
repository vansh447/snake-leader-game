import tkinter as tk
import random
from tkinter import messagebox

class SnakeAndLadderGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Snake and Ladder Game")
        self.root.geometry("500x500")
        
        self.players = {"Player 1": 1, "Player 2": 1}  # Player positions
        self.current_player = "Player 1"  # Start with Player 1
        
        # Define the snakes and ladders
        self.snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
        self.ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
        
        # Create UI elements
        self.info_label = tk.Label(root, text="Player 1's Turn", font=("Arial", 16))
        self.info_label.pack(pady=10)
        
        self.dice_button = tk.Button(root, text="Roll Dice", font=("Arial", 16), command=self.roll_dice)
        self.dice_button.pack(pady=20)

        self.player_position_label = tk.Label(root, text="Player 1 is at square 1", font=("Arial", 14))
        self.player_position_label.pack(pady=10)

    def roll_dice(self):
        dice_roll = random.randint(1, 6)  # Simulate a dice roll
        self.update_position(dice_roll)
        
        # Update the player information
        self.info_label.config(text=f"{self.current_player}'s Turn")
        
        # After the current player moves, check for a winner
        if self.players[self.current_player] >= 100:
            messagebox.showinfo("Game Over", f"{self.current_player} wins!")
            self.reset_game()

    def update_position(self, dice_roll):
        current_pos = self.players[self.current_player]
        new_pos = current_pos + dice_roll
        
        # If the new position exceeds 100, the player stays at the current position
        if new_pos > 100:
            new_pos = current_pos
        else:
            # Check for snakes or ladders
            if new_pos in self.snakes:
                new_pos = self.snakes[new_pos]
                messagebox.showinfo("Snake!", f"{self.current_player} got bitten by a snake! Going to square {new_pos}.")
            elif new_pos in self.ladders:
                new_pos = self.ladders[new_pos]
                messagebox.showinfo("Ladder!", f"{self.current_player} climbed a ladder! Going to square {new_pos}.")
        
        # Update player position
        self.players[self.current_player] = new_pos
        self.update_ui()
        
        # Change turn
        if self.current_player == "Player 1":
            self.current_player = "Player 2"
        else:
            self.current_player = "Player 1"
    
    def update_ui(self):
        # Update the UI to show the player's position
        self.player_position_label.config(text=f"{self.current_player} is at square {self.players[self.current_player]}")

    def reset_game(self):
        # Reset the game to initial positions
        self.players = {"Player 1": 1, "Player 2": 1}
        self.current_player = "Player 1"
        self.update_ui()
        self.info_label.config(text="Player 1's Turn")


# Main function to start the game
def main():
    root = tk.Tk()
    game = SnakeAndLadderGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
