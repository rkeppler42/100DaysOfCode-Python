# 🔐 Password Generator

This is the project for **Day 05** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

The program generates a secure random password based on the number of **letters**, **symbols**, and **numbers** chosen by the user.

---

## 🧠 What I Learned

- Using `for` loops with `range()` to repeat actions
- Using `random.choice()` to pick a random item from a list
- Building strings incrementally with `+=`
- Storing characters in a list and converting back to a string
- Using `random.shuffle()` to randomize the order of a list
- The difference between an **Easy Level** (sequential) and **Hard Level** (fully randomized) approach

---

## 🛠️ Requirements

The final program must:

1. Ask the user for:
   - How many **letters** they want in the password
   - How many **symbols** they want
   - How many **numbers** they want

2. Use pre-defined lists of:
   - Uppercase and lowercase letters
   - Common symbols (`!`, `@`, `#`, etc.)
   - Digits (`0`–`9`)

3. **Easy Level**: Generate the password in order — letters first, then symbols, then numbers.

4. **Hard Level**: Generate the password with all characters in a **completely random order** using `random.shuffle()`.

5. Print the final generated password.

---

## 📝 Example Output

```
Welcome to the PyPassword Generator!
How many letters would you like in your password?
> 8
How many symbols would you like?
> 3
How many numbers would you like?
> 4
Your password is: 3kB!r#9Xm2@tAn7
```

---

## 🔀 Easy vs Hard Level

| Level | Description |
|-------|-------------|
| ✅ Easy | Characters added in sequence: letters → symbols → numbers |
| 💪 Hard | All characters shuffled into a fully random order |

---

## 📦 Project Structure

```
Day 005 - Password Generator/
│── main.py
└── README.md
```

---

## 🏁 Status

✅ Completed