# 🔨 Blind Auction

This is the project for **Day 09** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

A **blind auction** program where multiple bidders enter their bids privately, and the program reveals the winner with the highest bid at the end.

---

## 🧠 What I Learned

- Creating and populating **dictionaries** with user input
- Using `float()` to store bids as decimal numbers
- Looping through a dictionary to **find the maximum value**
- Using a `while` loop to keep collecting bids until the user is done
- Importing and using variables from a **separate module**
- Formatting output with **f-strings** and `:.2f` for currency display

---

## 🛠️ Requirements

The final program must:

1. Display the **auction logo** on start.
2. Ask each bidder for their **name** and **bid amount**.
3. Store every bid in a **dictionary** with the name as the key and the bid as the value.
4. After each bid, ask if there are **any other bidders**:
   - If **yes** → collect the next bid.
   - If **no** → find and announce the winner.
5. Loop through the dictionary to determine who placed the **highest bid**.
6. Print the winner's name and their bid amount.

---

## 📝 Example Output

```
What is your name?:  Angela
What is your bid?:  $123
Are there any other bidders? Type 'yes' or 'no'.
yes
What is your name?:  John
What is your bid?:  $45
Are there any other bidders? Type 'yes' or 'no'.
no
The winner is Angela with a bid of $123.00.
```

---

## 📦 Project Structure

```
Day 009 - Blind Auction/
│── main.py
│── art.py
└── README.md
```

| File | Purpose |
|------|---------|
| `main.py` | Auction logic and bidding loop |
| `art.py` | ASCII art gavel logo |

---

## 🏁 Status

✅ Completed