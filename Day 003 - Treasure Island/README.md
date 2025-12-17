# 🏝️ Treasure Island

This is the project for **Day 03** of the course  
**“100 Days of Code: The Complete Python Pro Bootcamp”**.

A simple **Choose Your Own Adventure** game where the player makes choices that lead to different outcomes — including **Game Over** endings and one winning path.

---

## 🧠 What I Learned

- Writing branching logic with `if`, `elif`, and `else`
- Comparing strings with `==`
- Handling user input reliably using `.lower()`
- Building nested decision trees (multiple layers of conditions)
- Using escape characters like `\'` inside strings
- Formatting input prompts with `\n` for cleaner UX
- Working with multi-line strings (ASCII art with triple quotes)

---

## 🛠️ Requirements

The final program must:

1. Start the game with a short intro (optional: ASCII art).
2. Ask the player to choose between **left** or **right**.
   - If they choose **right** (or anything other than *left*), the game ends (**Game Over**).
3. If they choose **left**, ask them to choose between **wait** or **swim**.
   - If they choose **swim** (or anything other than *wait*), the game ends (**Game Over**).
4. If they choose **wait**, ask them to pick a door color: **red**, **yellow**, or **blue**.
   - **Yellow** is the winning choice.
   - Any other choice ends the game (**Game Over**).
5. Inputs should be case-insensitive (e.g. `Left`, `LEFT`, `left` all work).

---

## 📝 Example Flow

```
You're at a crossroad. Where do you want to go? Type "left" or "right".

> left

You've come to a lake. Type "wait" to wait for a boat. Type "swim" to swim across.

> wait

There is a house with 3 doors: red, yellow, and blue. Which color do you choose?

> yellow

You found the treasure! You win!
```


---

## 📦 Project Structure

Day 03 - Treasure Island/
│── main.py
└── README.md

---

## 🏁 Status

✅ Completed
