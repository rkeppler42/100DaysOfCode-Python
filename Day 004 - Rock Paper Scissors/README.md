# ✊✋✌️ Rock Paper Scissors

This is the project for **Day 04** of the course  
**“100 Days of Code: The Complete Python Pro Bootcamp”**.

A simple **Rock, Paper, Scissors** game where you play against the computer.  
You choose a number (**0 = rock**, **1 = paper**, **2 = scissors**) and the computer randomly picks one too.  
The program then prints the ASCII art for both choices and announces the result.

---

## 🧠 What I Learned

- Importing and using the `random` module
- Generating random integers with `random.randint()`
- Storing related values in a list and accessing them by index
- Converting user input to integers with `int()`
- Writing game logic with `if`, `elif`, and `else`
- Handling invalid inputs safely (numbers outside 0–2)
- Using ASCII art with triple-quoted strings (`""" ... """`)

---

## 🛠️ Requirements

The final program must:

1. Ask the player:

   `What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.`

2. Convert the user input to an integer.
3. Generate the computer choice randomly between **0 and 2**.
4. Print the ASCII art of:
   - The player's choice
   - The computer's choice
5. Determine the result based on the rules:
   - Rock beats Scissors
   - Scissors beats Paper
   - Paper beats Rock
   - Same choice = Draw
6. If the user types an invalid number (e.g. `-1`, `3`, `99`):
   - Print an error message (e.g. `You typed an invalid number, you lose.`)
   - Do **not** crash the program.

---

## 📝 Example Output

```
What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.

> 2

(Scissors ASCII Art)

Computer chose:

(Rock ASCII Art)

You lose.
```

---

## 🏁 Status

✅ Completed
