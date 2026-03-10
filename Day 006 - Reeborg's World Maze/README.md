# 🤖 Reeborg's World Maze

This is the project for **Day 06** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

A maze-solving algorithm written for **Reeborg's World**, where a robot must navigate to the goal regardless of its random starting position and direction.

---

## 🧠 What I Learned

- Using `while` loops to repeat actions until a condition is met
- Writing `if`, `elif`, and `else` statements for decision-making
- Thinking in terms of **algorithms** — defining a hierarchy of instructions
- Implementing the **right-hand wall-following** algorithm
- Identifying and debugging **infinite loops** caused by edge cases
- Testing code against multiple scenarios to ensure robustness

---

## 🛠️ Requirements

The final program must:

1. Work no matter where the robot **starts** in the maze or which **direction** it faces.
2. Use the **right-hand wall-following** algorithm:
   - If the **right side is clear** → turn right and move forward
   - Else if the **front is clear** → move forward
   - Else → turn left
3. Define a `turn_right()` function (since only `turn_left()` is built in).
4. Keep repeating the logic in a `while` loop until `at_goal()` is `True`.
5. Handle the **edge case** where the robot starts with no wall on its right side (which causes an infinite loop), by first seeking out a wall.

---

## 🔀 Algorithm: Right-Hand Wall Following

The robot follows a simple priority hierarchy at every step:

| Priority | Condition | Action |
|----------|-----------|--------|
| 1st | Right side is clear | Turn right, then move |
| 2nd | Front is clear | Move forward |
| 3rd | Neither is clear | Turn left |

---

## 🐛 Edge Case & Fix

If the robot starts in an open area with no wall on its right, it will loop
endlessly turning right. The fix is to add a preliminary loop:

1. Move forward until a wall is found in front.
2. Turn left — this places the wall on the robot's right side.
3. Now enter the main maze-solving loop safely.

---

## 📝 Example Code Structure

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# Edge case fix: find a wall first
while front_is_clear():
    move()
turn_left()

# Main maze-solving loop
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
```

---

## 📦 Project Structure

```
Day 006 - Reeborg's World Maze/
│── main.py
└── README.md
```

---

## 🏁 Status

✅ Completed