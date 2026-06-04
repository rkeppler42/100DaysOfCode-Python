# 🧮 Calculator

This is the project for **Day 10** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

A console **calculator** that performs the four basic operations (`+`, `-`, `*`, `/`) on floating-point numbers. After each result, the user can keep calculating with the previous answer or start a brand new calculation.

---

## 🧠 What I Learned

- Defining functions for each operation (`add`, `subtract`, `multiply`, `divide`)
- Storing **functions as values** inside a dictionary (without the `()`, since we store the reference, not the call)
- Triggering a function through a dictionary lookup: `operations[operation](a, b)`
- Looping through a dictionary to print its keys as the menu of available operators
- Converting input to `float` so the calculator handles decimals
- Building a readable equation with an **f-string**: `f"{a} {operation} {b} = {c}"`
- Using a `while True` loop with a `first_operation` flag to control whether to **accumulate** the previous result or restart
- Clearing the terminal in a **cross-platform** way with `os.name` + `os.system("cls"/"clear")`

---

## 🛠️ Requirements

The final program must:

1. Ask the user for the **first number**.
2. Display the available operators (`+`, `-`, `*`, `/`) and ask the user to **pick an operation**.
3. Ask for the **next number**.
4. Convert both inputs into **floats**.
5. Select the correct function from the `operations` dictionary using the chosen symbol as the key, then compute the result.
6. Print the full equation and result, e.g. `5.0 * 3.0 = 15.0`.
7. Ask the user to:
   - Type **`y`** → keep calculating, using the previous result as the first number.
   - Type **`n`** → start a new calculation from scratch.
8. Loop until the user decides to stop.

---

## 📝 Example Output

```
What's the first number?: 5
+
-
*
/
Pick an operation: *
What's the next number?: 3
5.0 * 3.0 = 15.0
Type 'y' to continue calculating with 15.0, or type 'n' to start a new calculation: y
+
-
*
/
Pick an operation: +
What's the next number?: 5
15.0 + 5.0 = 20.0
Type 'y' to continue calculating with 20.0, or type 'n' to start a new calculation: n
```

---

## 📦 Project Structure

```
Day 010 - Calculator/
│── main.py
└── README.md
```

| File      | Purpose                                                            |
| --------- | ------------------------------------------------------------------ |
| `main.py` | Operation functions, dictionary dispatch, and the calculation loop |

---

## 🏁 Status

✅ Completed
