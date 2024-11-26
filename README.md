# snake-leader-game
![game-gui](https://github.com/user-attachments/assets/0f74f390-c3ac-4e38-a9ff-3ac93ab1d0e4)
Explanation of the Code:
GUI Layout:

The game window uses Tkinter to create a simple GUI layout.
There’s a label to show which player’s turn it is, a button to roll the dice, and a label to display the player's current position.
Snakes and Ladders:

Snakes and Ladders are stored in dictionaries where the key is the starting square and the value is the ending square.
When a player lands on a snake or ladder, the app displays an informational popup using messagebox.showinfo.
Roll Dice:

The dice roll is simulated using random.randint(1, 6) which generates a random number between 1 and 6.
Turn Change:

After each roll, the turn alternates between Player 1 and Player 2.
After Player 1 rolls the dice, the game waits for Player 2 to roll, and vice versa.
Winning Condition:

The game checks if the player's position reaches or exceeds square 100, and if so, the game ends and the winner is displayed in a popup.
Reset Game:

After a winner is determined, the game resets to its initial state so it can be played again.
Running the Game:
Installation: You don’t need any extra installations for Tkinter if you're using standard Python.
Run the script: Save the script in a .py file and run it. The window will appear with the game interface.
Play: Click on the "Roll Dice" button to roll the dice and move along the board. The game alternates between Player 1 and Player 2.
Example Output:
Starting Message: "Player 1's Turn"
After Dice Roll: "Player 1 is at square X" (Player 1's position after rolling the dice).
Message Boxes:
If Player 1 hits a snake: "Player 1 got bitten by a snake! Going to square X."
If Player 1 hits a ladder: "Player 1 climbed a ladder! Going to square X."
Winner: When a player reaches or exceeds square 100, a popup will show "Player X wins!"
Customization Ideas:
Board Visualization: You could draw a more complex board with Tkinter's canvas for visual representation of the snakes and ladders.
Multiple Players: Extend the game to support more than two players.
Dice Animation: Create a dice roll animation to make the game more fun and interactive.


