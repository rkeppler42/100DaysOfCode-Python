# 🃏 Blackjack

This is the project for **Day 11** of the course  
**"100 Days of Code: The Complete Python Pro Bootcamp"**.

A simplified, console-based version of **Blackjack** (also known as 21). The player draws cards trying to get as close to 21 as possible without going over, then the dealer plays by the house rules, and the program decides the winner.

---

## 🧠 What I Learned

- Breaking a complex problem down into small, single-responsibility **functions**
- Writing **type hints** (`hand: list -> None`) and **docstrings** to document each function's purpose, parameters, and return value
- Mutating a list **in place** (passing the hand by reference and appending to it)
- Modeling an **infinite deck** by sampling from a weighted list where `10` appears four times (J, Q, K all count as 10)
- Handling the **Ace** logic: it starts as `11` and is converted to `1` only if the hand goes over 21
- Encapsulating game flow in dedicated turns (`player_turn`, `dealer_turn`) and separate display functions
- Implementing the dealer rule: **keep hitting while the score is below 17**
- Structuring a program with a `main()` function and the `if __name__ == "__main__"` guard
- Adding a **replay loop** so the user can keep playing until they choose to quit

---

## 🛠️ Requirements

The final program must:

1. Display the **Blackjack logo** and ask the user if they want to play.
2. Deal **two cards each** to the player and the dealer.
3. Show the player's full hand and score, plus only the dealer's **first card**.
4. Let the player **hit** (`y`) or **pass** (`n`):
   - Keep dealing while the player wants more cards and their score is under 21.
   - If the player **busts** (over 21), they lose immediately.
5. Once the player passes (and didn't bust), the **dealer draws** until reaching at least 17.
6. Reveal both final hands and decide the outcome:
   - Player over 21 → **lose**
   - Dealer over 21 → **win**
   - Equal scores → **draw**
   - Higher score wins
7. Ask the user if they want to **play again**, looping until they type `n`.

---

## 🃏 House Rules (Simplified)

| Rule       | Detail                                                 |
| ---------- | ------------------------------------------------------ |
| Card pool  | `[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]`         |
| Face cards | J, Q, K all count as **10**                            |
| Ace        | Starts as **11**, becomes **1** if the hand exceeds 21 |
| Deck       | **Infinite** — drawn cards are not removed             |
| Dealer     | Must keep drawing while the score is **below 17**      |

---

## 📝 Example Output

```
.------.            _     _            _    _            _
|A_  _ |.          | |   | |          | |  (_)          | |
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   <
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |
      `------'                           |__/

Do you want to play a game of Blackjack? Type 'y' or 'n':
y
Your cards: [10, 3], current score: 13
Computer's first card: 7
Type 'y' to get another card, type 'n' to pass:
y
Your cards: [10, 3, 5], current score: 18
Computer's first card: 7
Type 'y' to get another card, type 'n' to pass:
n
Your final hand: [10, 3, 5], final score: 18
Computer's final hand: [7, 10], final score: 17
You win 😃
Do you want to play a game of Blackjack? Type 'y' or 'n':
n
```

---

## 📦 Project Structure

```
Day 011 - Blackjack/
│── main.py
│── art.py
└── README.md
```

| File      | Purpose                                         |
| --------- | ----------------------------------------------- |
| `main.py` | Game logic, turns, scoring, and the replay loop |
| `art.py`  | ASCII art logo                                  |

---

## 🏁 Status

✅ Completed
